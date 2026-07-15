# Dry Bulk Shipping Market Analysis Based on BDI Index (2020-2026)

## Project Overview

This project analyzes the Baltic Dry Index (BDI) from 2020 to 2026 and studies the relationship between freight rate changes, cargo demand, vessel supply and external events.

The purpose of this project is to understand dry bulk shipping market cycles and explore how global economic conditions, supply-demand balance and unexpected events influence freight rate fluctuations.

---

## Data Source

- Source: Investing.com
- Index: Baltic Dry Index (BDI)
- Frequency: Monthly
- Period: 2020-2026

---

## Project Structure

```text
Shipping Market Data Analysis

├── data
│   └── Raw BDI historical data

├── excel
│   ├── BDI market analysis workbook
│   └── Monthly BDI historical dataset

├── images
│   ├── BDI_trend_analysis.png
│   ├── key_events_analysis.png
│   └── bdi_trend_python.png

├── python
│   ├── bdi_analysis.py
│   └── requirements.txt

├── report
│   └── BDI_Market_Analysis_Report_2020_2026.pdf

└── README.md
```

---

## Analysis Process

### 1. Data Collection

Collected monthly BDI historical data from 2020 to 2026 and organized the dataset, including index prices and market fluctuations.

### 2. Excel Data Analysis

Used Excel to:

- Organize and review monthly BDI data
- Create a trend chart covering 2020 to 2026
- Identify major market turning points
- Summarize key events and market drivers
- Develop personal insights into shipping market cycles

### 3. Key Events Analysis

Analyzed major market events affecting BDI movements, including:

- COVID-19 pandemic impact
- Global economic recovery
- Supply-demand imbalance
- Interest rate changes
- Energy crisis and geopolitical events
- Changes in port congestion and vessel efficiency

### 4. Market Insights

Studied the relationship between:

- Cargo demand
- Vessel supply
- Economic cycles
- Port congestion
- External shocks
- Policy and regulatory changes

to understand the reasons behind freight rate fluctuations.

### 5. Python Data Analysis

Used Python to improve the reproducibility of the data cleaning and visualization process.

The Python script:

- Uses `pandas` to read the original CSV dataset
- Converts the date field into datetime format
- Removes commas from price values and converts them into numeric data
- Removes invalid or missing date and price values
- Sorts the dataset chronologically
- Uses `matplotlib` to generate a monthly BDI trend chart
- Saves the generated chart automatically in the `images` folder

The script successfully processed 79 monthly observations covering January 2020 to July 2026.

---

## Key Findings

- The dry bulk shipping market shows strong cyclical characteristics.
- Freight rate fluctuations are mainly influenced by the balance between cargo demand and vessel supply.
- The 2021 BDI increase was supported by stronger commodity demand, port congestion and reduced effective vessel capacity.
- The market correction after 2021 reflected weaker global demand, tighter financial conditions and improved vessel availability.
- External events such as pandemics, energy crises and geopolitical conflicts can significantly disrupt market equilibrium.
- Because vessel supply adjusts slowly, sudden demand changes can create large freight rate movements.

---

## Visualization

### Excel BDI Trend Analysis

![Excel BDI Trend Analysis](images/BDI_trend_analysis.png)

---

### Key Events Analysis

![Key Events Analysis](images/key_events_analysis.png)

---

### Python-Generated BDI Trend Chart

![Python-Generated BDI Trend Chart](images/bdi_trend_python.png)

---

## Tools Used

- Microsoft Excel
- Python
- pandas
- matplotlib
- GitHub

---

## Project Limitations

This project mainly focuses on the BDI itself and therefore provides a broad market-level analysis.

Future analysis could include:

- China iron ore import volume
- Global coal and grain trade volumes
- Dry bulk fleet growth
- New vessel deliveries
- Port congestion data
- Vessel turnaround efficiency

These indicators could provide more direct evidence of changes in cargo demand and vessel supply.

---

## Conclusion

Through analyzing BDI data from 2020 to 2026, this project improved my understanding of dry bulk shipping market cycles.

The analysis shows that shipping markets are not driven by a single factor. Freight rate changes result from the interaction between global economic conditions, cargo demand, vessel supply, port efficiency and external events.

Excel was used for structured analysis, event interpretation and visual presentation. Python was used to automate data cleaning and trend-chart generation, improving the reproducibility of the project.

This project demonstrates how Excel and basic Python tools can be applied to maritime market research and shipping data analysis.
