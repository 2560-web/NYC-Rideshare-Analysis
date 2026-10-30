# Car Sales Data Analytics

**Python · Pandas · Exploratory Data Analysis · Data Cleaning · Visualisation**

## Overview
This repository reconstructs an MSc data analytics coursework project exploring car sales data, including vehicle prices, customer incomes and vehicle categories. Earlier coursework records describe approximately 23,906 records; the original CSV and submitted notebook are not currently available to verify that figure.

## Questions explored
- What does the dataset contain, and where are values missing or duplicated?
- How are numeric features distributed?
- Which numeric attributes correlate with one another?
- How can the data be prepared for further business or predictive analysis?

## Workflow
1. Load the original CSV and inspect data types and missing values.
2. Identify and remove exact duplicate rows, preserving a cleaned copy.
3. Summarise numeric and categorical columns.
4. Generate distributions and a numeric correlation heatmap.
5. Save analysis outputs for review.

## Run locally
Install Python 3.10+ and run:

```bash
pip install -r requirements.txt
python src/analyze.py --input data/car_sales.csv
```

The script writes `results/summary.txt`, `results/cleaned_data.csv`, and charts (when numeric columns exist).

## Repository structure
- `src/analyze.py` — reproducible analysis pipeline
- `notebooks/car_sales_analysis.ipynb` — Jupyter workflow
- `data/README.md` — data requirements and provenance
- `results/README.md` — output explanations
- `index.html` — browser project overview (not a live analysis engine)

## Provenance and limitations
**This is a reconstructed portfolio project, not the original submitted coursework.** The original data and notebook have not been recovered. No numerical findings or charts are represented as original results. Running the code on the authentic CSV will generate independently checkable outputs. Verify dataset permissions before publishing the raw data.

**Author:** Prem Armstrong D  
**Academic background:** MSc Internet of Things and Future Networks, Queen Mary University of London
