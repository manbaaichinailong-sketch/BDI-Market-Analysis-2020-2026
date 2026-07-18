# BDI Data Dictionary

## Source fields

File: `excel/Baltic Dry Index Historical Data.csv`

| Field | Description |
|---|---|
| Date | Monthly observation date |
| Price | Monthly BDI index value used as the analysis series |
| Open | First quoted value for the period |
| High | Highest quoted value for the period |
| Low | Lowest quoted value for the period |
| Vol. | Volume field supplied by the source; generally blank for this index |
| Change % | Source-reported percentage change |

## Python-generated fields

File: `data/BDI_Analysis_Output.csv`

| Field | Description |
|---|---|
| MoM | Month-over-month percentage return |
| MA_3M | Three-month moving average |
| MA_12M | Twelve-month moving average |
| Running_Peak | Highest BDI value observed up to that date |
| Drawdown | Percentage decline from the running peak |
| Year | Calendar year used for annual aggregation |

File: `data/BDI_Annual_Summary.csv`

| Field | Description |
|---|---|
| Average_BDI | Mean monthly BDI for the year |
| Minimum / Maximum | Lowest and highest monthly observations |
| Monthly_Volatility | Standard deviation of monthly returns |
| Worst_Drawdown | Largest peak-to-trough decline observed in the year |
| Observations | Number of monthly records available |
| Annual_Average_YoY | Change in annual average versus the prior year |

## Scope note

BDI is a broad dry-bulk market indicator. It should not be used as a direct
proxy for container spot rates, individual vessel earnings or a causal
estimate of a single event's impact.
