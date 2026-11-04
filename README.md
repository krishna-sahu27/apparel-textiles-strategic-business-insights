# Apparel & Textiles Strategic Business Insights — Week 6

**Internship capstone | End-to-end business analytics**

This project synthesizes data collection, cleaning, exploratory data analysis, integration, visualization and forecasting for a fictional apparel business, ThreadLine Apparel.

> **Data integrity:** All included data and numerical outputs are synthetic and illustrative. They are not actual company records, verified market research or operational forecasts.

## Business question
How can ThreadLine improve demand planning, inventory availability, marketing allocation and product decisions while reducing excess stock?

## Workflow
1. Collect sales, product, inventory, marketing and customer data.
2. Validate records, standardize fields and handle missing/duplicate values.
3. Explore sales, margin, seasonality, category and channel patterns.
4. Integrate source tables at a consistent grain.
5. Visualize KPIs and interpret business meaning.
6. Build a baseline forecast and evaluate it on a chronological holdout.
7. Convert findings into prioritized actions and measurable KPIs.

## Structure
- data/: data documentation and generated synthetic dataset
- src/: reproducible Python workflow
- docs/: methodology and strategic report
- output/: generated charts, cleaned data and forecast results

## Run locally
Install dependencies with: pip install -r requirements.txt
Then run: python src/run_analysis.py

## Assumptions
Fictional multi-channel apparel business; INR currency; 36 monthly observations; four apparel categories; online and retail channels. Forecasts are educational baselines only. Replace synthetic data with approved real data before business use.

## Author
Krishna Sahu | Week 6 Final Internship Task
