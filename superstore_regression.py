"""Superstore: repair dates, then model how discount drives profit margin.
Usage: python superstore_regression.py path/to/supermarket_data_analysis.xlsx
"""
import sys, warnings
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score, roc_auc_score, accuracy_score
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

path = sys.argv[1]
raw = pd.read_excel(path, sheet_name="Raw_Data")
d = raw.copy()

# Date repair: cells stored as real dates were read day/month swapped; text cells are m/d/yyyy.
def fix(s):
    out = []
    for v in s:
        if isinstance(v, str):
            out.append(pd.to_datetime(v, format="%m/%d/%Y"))
        else:
            out.append(pd.Timestamp(v.year, v.day, v.month) if v.day <= 12 else pd.Timestamp(v))
    return pd.Series(out)
d["Order Date"], d["Ship Date"] = fix(raw["Order Date"]), fix(raw["Ship Date"])
gap = (d["Ship Date"] - d["Order Date"]).dt.days
assert gap.between(0, 14).all(), "date repair failed"
d.to_csv("superstore_dates_repaired.csv", index=False)

d["Margin"] = d["Profit"] / d["Sales"]
d["Loss"] = (d["Profit"] < 0).astype(int)
d = d.rename(columns={"Sub-Category": "SubCat", "Ship Mode": "ShipMode"})

print(f"rows {len(d)}, sales {d.Sales.sum():,.0f}, profit {d.Profit.sum():,.0f}")
print("annual:\n", d.groupby(d["Order Date"].dt.year)[["Sales", "Profit"]].sum().round(0))
m = d.groupby(d["Order Date"].dt.to_period("M"))[["Sales", "Profit"]].sum()
print("top sales month:", m.Sales.idxmax(), round(m.Sales.max()), "| top profit month:", m.Profit.idxmax(),
      round(m.Profit.max()), "| worst profit month:", m.Profit.idxmin(), round(m.Profit.min()))
hi = d[d.Discount > 0.2]; lo = d[d.Discount <= 0.2]
print(f"loss-making lines: discount>20% {int(hi.Loss.sum())}/{len(hi)} = {hi.Loss.mean():.2%}; "
      f"<=20% {int(lo.Loss.sum())}/{len(lo)} = {lo.Loss.mean():.2%}")
print("corr(discount, profit) =", round(d.Discount.corr(d.Profit), 3),
      "| corr(discount, margin) =", round(d.Discount.corr(d.Margin), 3))

# Model 1: OLS on profit margin (interpretable), 80/20 holdout
f1 = "Margin ~ Discount + C(SubCat) + C(Region) + C(Segment) + C(ShipMode)"
tr, te = train_test_split(d, test_size=0.2, random_state=42)
ols = smf.ols(f1, data=tr).fit()
print("\nMODEL 1 OLS margin: train R2 %.3f, holdout R2 %.3f" % (ols.rsquared, r2_score(te.Margin, ols.predict(te))))
b, ci = ols.params["Discount"], ols.conf_int().loc["Discount"]
print("Discount coef %.3f (95%% CI %.3f to %.3f), p=%.2g -> +10pp discount = %.1f pp margin"
      % (b, ci[0], ci[1], ols.pvalues["Discount"], b * 10))
simple = smf.ols("Margin ~ Discount", data=tr).fit()
print("Discount alone holdout R2 %.3f" % r2_score(te.Margin, simple.predict(te)))

# Model 2: logistic regression, probability a line loses money
X = pd.get_dummies(d[["Discount", "SubCat", "Region", "Segment", "ShipMode"]], drop_first=True).astype(float)
Xtr, Xte, ytr, yte = train_test_split(X, d.Loss, test_size=0.2, random_state=42, stratify=d.Loss)
lg = LogisticRegression(max_iter=2000).fit(Xtr, ytr)
p = lg.predict_proba(Xte)[:, 1]
print("\nMODEL 2 logistic (line makes a loss): holdout AUC %.3f, accuracy %.3f (base rate %.3f)"
      % (roc_auc_score(yte, p), accuracy_score(yte, p > .5), 1 - yte.mean()))

# Break-even discount by sub-category (margin fitted on discount, per sub-category)
rows = []
for s, g in d.groupby("SubCat"):
    r = smf.ols("Margin ~ Discount", data=g).fit()
    be = -r.params["Intercept"] / r.params["Discount"] if r.params["Discount"] < 0 else np.nan
    rows.append((s, len(g), r.params["Intercept"], r.params["Discount"], be))
be = pd.DataFrame(rows, columns=["SubCat", "n", "margin_at_0", "slope", "breakeven_discount"]).sort_values("breakeven_discount")
be.round(3).to_csv("breakeven_by_subcategory.csv", index=False)
print("\nBreak-even discount by sub-category (simple fit):\n", be.round(3).to_string(index=False))

# Chart
fig, ax = plt.subplots(figsize=(7, 4))
g = d.groupby("Discount")["Margin"].mean() * 100
ax.bar([f"{int(x*100)}%" for x in g.index], g.values, color=["#1f6f43" if v >= 0 else "#b3261e" for v in g.values])
ax.axhline(0, color="k", lw=.8); ax.set_xlabel("Discount level"); ax.set_ylabel("Average line margin (%)")
ax.set_title("Superstore: margin turns negative above ~20% discount"); plt.tight_layout(); plt.savefig("margin_by_discount.png", dpi=150)
