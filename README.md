# Superstore Sales & Profitability Analysis

**Tools:** Microsoft Excel  
**Project Type:** Exploratory Data Analysis  
**Analysis Period:** January 2014 – December 2017

## 1. Problem Statement

The objective of this project was to analyse Superstore's sales and profitability across customer segments, product categories, sub-categories, regions and time periods.

The analysis focused on identifying the major revenue and profit drivers, understanding poorly performing products, evaluating the relationship between discounting and profitability, and identifying opportunities to improve business performance.

## 2. Dataset Overview

The analysis was performed on a Superstore retail transactions dataset containing:

| Metric | Value |
| Total records | 9,994 |
| Distinct orders | 5,009 |
| Analysis period | Jan 2014 – Dec 2017 |
| Total Sales | 2,297,201 |
| Total Profit | 286,397 |
| Overall Profit Margin | 12.5% |

**Key fields:** Order ID, Order Date, Ship Date, Customer ID, Segment, Region, Category, Sub-Category, Product Name, Sales, Quantity, Discount and Profit.

## 3. Data Cleaning & Methodology

### Data Cleaning
- Checked important fields, including Customer ID, Order Date, Sales and Profit, for data-quality issues.
- Standardised Order Date and Ship Date formats.
- Standardised category and region names.
- Verified that Sales, Profit, Quantity and Discount were numeric.
- Checked unusual values and outliers.
- Used Order Date consistently for monthly and annual sales analysis to attribute transactions to the period in which orders were placed, rather than the period in which they were shipped.

### Analysis Techniques
- Excel formulas for calculations and summary metrics.
- PivotTables and charts for segment, regional, category and time-based analysis.
- Profit margin calculations using Total Profit ÷ Total Sales.
- Correlation analysis to examine the relationship between discounts and profit.
- Conditional probability to compare unprofitability across discount levels.
- Sub-category and product-level drill-downs to investigate profitability.

## 4. Key Findings

### A. Revenue and Customer Performance

**1. Customer Segment**

The Consumer segment contributes 52% of total store revenue, making it the largest revenue-generating customer segment.

![Sales by segment](images/segment_sales_chart.png)

**2. Regional Performance**

The West region leads regional performance with:
- Sales: 725,458
- Profit: 108,418
- Distinct Orders: 1,611
- Profit Margin: 14.9%

It contributes approximately 31.6% of total store revenue. The Central region has the lowest regional profit margin at approximately 7.9%, indicating an opportunity to investigate its profitability.

![Region share chart](images/region_pie_chart.png)

### B. Category and Sub-category Profitability

**3. Category Performance**

Technology contributes 51% of total store profit, making it the largest contributor to overall profitability.

![Technology profit by sub-category](images/technology_profit_pie.png)

**4. Technology Drill-down**

The Technology category shows a difference between revenue and profit leaders:

| Sub-category | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| Copiers | 149,528 | 55,618 | 37.2% |
| Phones | 330,007 | 44,516 | 13.5% |

Copiers generate the highest profit despite substantially lower sales, while Phones generate the highest sales. This highlights the importance of evaluating products using profitability as well as revenue.

**5. Loss-making Sub-categories**

Three sub-categories operate at negative profit margins:

| Sub-category | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| Tables | 206,966 | -17,725 | -8.6% |
| Bookcases | 114,880 | -3,473 | -3.0% |
| Supplies | 46,674 | -1,189 | -2.5% |

Tables record the largest absolute loss among these sub-categories.

**6. High-sales, Low-margin Sub-categories**

Some sub-categories generate substantial revenue but relatively low profit margins:

| Sub-category | Sales | Profit | Profit Margin |
|---|---:|---:|---:|
| Machines | 189,239 | 3,385 | 1.8% |
| Chairs | 328,449 | 26,590 | 8.1% |
| Storage | 223,844 | 21,279 | 9.5% |

Machines are particularly worth investigating because they generate 189,239 in sales but only 3,385 in profit.

**7. High-margin Sub-categories**

Labels, Paper and Copiers demonstrate strong profitability, with margins of 44.4%, 43.4% and 37.2%, respectively.

### C. Discount and Profitability Analysis

**8. Discounting and Profitability**

Approximately 96.77% of records/orders receiving discounts above 20% were unprofitable, compared with approximately 6.08% at discounts of 20% or less.

This indicates a strong association between higher discounts and unprofitability. However, the analysis does not establish that discounts alone caused the losses.

The overall correlation between Discount and Profit was approximately -0.20, indicating a weak negative linear relationship.

### D. Time-Based Performance

**9. Annual Sales and Profit Trend**

Sales increased significantly after 2015. The monthly data indicates the following annual performance:

- 2014: Sales of approximately 484,248.
- 2015: Sales of approximately 470,532.
- 2016: Sales of approximately 609,204.
- 2017: Sales of approximately 733,213.

The strongest annual growth occurred in 2016, followed by further growth in 2017. Annual profit also increased over the period.

**10. Monthly Performance**

- November 2017 recorded the highest monthly sales at approximately 118,448.
- December 2016 recorded the highest monthly profit at approximately 17,885.
- January 2015 recorded the largest monthly loss, approximately -3,281.

The difference between the highest-sales month and highest-profit month demonstrates that revenue growth does not necessarily translate into proportionate profit growth.

## 5. Summary Business Metrics

![Excel dashboard](images/dashboard.png)

| Metric | Result |
|---|---:|
| Average Order Value | 458.61 |
| Overall Profit Margin | 12.5% |
| Loss-making Order Rate | 20.4% |
| Average Discount | 15.6% |
| Revenue per Unit | 60.66 |

**Metric definitions:**
- Average Order Value = Total Sales ÷ Distinct Order Count.
- Profit Margin = Total Profit ÷ Total Sales.
- Loss-making Order Rate = Orders with negative aggregated profit ÷ Total Distinct Orders.
- Average Discount = Average of the Discount column.
- Revenue per Unit = Total Sales ÷ Total Quantity.

## 6. Business Recommendations

1. Review discounting strategy: Investigate discounts above 20% and consider approval controls or product-specific discount limits to reduce unprofitable transactions.

2. Address loss-making sub-categories: Investigate Tables, Bookcases and Supplies by reviewing pricing, discounts and product costs.

3. Improve low-margin performance: Review Machines, Chairs and Storage to identify opportunities to improve margins without sacrificing sales.

4. Prioritise profitable Technology products: Evaluate opportunities to grow Copiers while investigating the relatively lower profitability of Phones.

5. Investigate regional profitability: Examine why Central has a lower profit margin than other regions and identify practices that could improve its performance.

6. Plan around sales trends: Use historical monthly sales patterns to support inventory and promotional planning, while monitoring profit alongside revenue.

## 7. Limitations & Further Analysis

- The analysis identifies associations and patterns but does not establish causation.
- Product-level investigation is required to identify the specific products driving losses within poorly performing sub-categories.
- Further analysis could examine category-wise discount impact, regional product mix and monthly profit trends.
- Additional cost and operational data could help explain the underlying reasons for low product profitability.
