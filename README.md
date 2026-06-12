# 🚗 Australian Vehicle Registrations Pipeline
### March 2026 | End-to-end Data Engineering Project

## Project Overview
An end-to-end data pipeline that ingests, cleans, transforms and visualises 
Australian vehicle registration data for March 2026 using modern data engineering tools.

## Architecture
Raw CSV → Python Cleaning → BigQuery (Bronze) → dbt (Silver/Gold) → Power BI

## Dashboard
![Dashboard](dashboard.png)

## Key Findings
- **Toyota** was the #1 selling brand with ~4,000 units registered
- **BYD** placed 2nd — Chinese EVs are gaining significant market share in Australia
- **White** was the most popular colour at 36% of all registrations
- Almost every brand's most popular colour was white except Chery (grey)

## Tech Stack
| Tool | Purpose |
|---|---|
| Python + RapidFuzz | Data cleaning, fuzzy brand name matching |
| Google BigQuery | Cloud data warehouse (bronze layer) |
| dbt Core | Data transformation (silver + gold layers) |
| Power BI Desktop | Dashboard and visualisation |

## Pipeline Layers
- **Bronze** — raw CSV uploaded to BigQuery as-is
- **Silver** — dbt staging model, column renaming and cleaning
- **Gold** — dbt analytical models ready for reporting

## dbt Models
| Model | Layer | Description |
|---|---|---|
| `stg_vehicles` | Silver | Cleaned and renamed raw data |
| `top_makes` | Gold | Total units registered per brand |
| `colour_trends` | Gold | Most popular colours across all registrations |
| `top_make_colour` | Gold | Most popular colour per brand using window functions |

## Data Quality
- 5 dbt tests passing (not_null checks on all key columns)
- Brand name inconsistencies fixed using RapidFuzz fuzzy matching
- 158 raw brand codes cleaned to 141 standardised brand names

## How to Run
1. Clone this repo
2. Install dependencies: `pip install pandas rapidfuzz`
3. Run cleaning script: `python clean_vehicles.py`
4. Upload `cleaned_veh_data.csv` to BigQuery
5. Set up dbt profile pointing to BigQuery
6. Run `dbt run` and `dbt test`

## Dashboard
Built in Power BI Desktop connected to BigQuery in Import mode.

Visuals:
- Top 10 brands bar chart
- Colour distribution donut chart  
- Top colour per brand table
- Total units scorecard (29K)
