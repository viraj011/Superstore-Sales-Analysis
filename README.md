# Superstore: how much does discounting cost profit?

Question: how strongly does discount level drive profit margin, and where does it turn negative?
Data: Superstore retail order lines (9,994 rows, 2014-2017), from the supplied Excel workbook (sheet Raw_Data).
Method: repaired mixed-format dates (see below), then OLS regression of line profit margin on discount plus sub-category, region, segment and ship mode (80/20 holdout), and a logistic regression for "line makes a loss". Break-even discount fitted per sub-category.

Results (from run_output.txt)
- 96.8% of lines with discount above 20% lost money (1,348 of 1,393), against 6.1% at 20% or less (523 of 8,601).
- Each extra 10 points of discount lowers margin by about 19.9 points (95% CI 19.7 to 20.2), holding sub-category, region, segment and ship mode fixed. Holdout R2 0.81; discount alone gets 0.75.
- Logistic model flags loss-making lines with holdout AUC 0.985 (accuracy 0.942 vs 0.813 base rate).
- Fitted break-even discount is lowest for Appliances (~12%), Bookcases (~15%), Storage (~16%), Tables (~16%); highest for Paper, Envelopes, Labels (70%+). Simple per-category fits, treat as indicative.
- Limits: this shows association in observed data, not a controlled effect of discounting; there is no cost data.

Date repair: in the raw sheet 4,042 order dates were stored as real dates with day and month swapped, and the rest as m/d/yyyy text. After repair every ship date is 0-7 days after its order date. Annual totals were unaffected; monthly figures change.

Run: pip install -r requirements.txt && python superstore_regression.py supermarket_data_analysis.xlsx
Stack: Python, pandas, statsmodels, scikit-learn, matplotlib.
