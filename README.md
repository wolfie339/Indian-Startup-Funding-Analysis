# Indian-Startup-Funding-Analysis

📌 Overview

This project analyzes startup funding data to uncover insights and trends in the Indian startup ecosystem.
It processes raw funding data, cleans and standardizes it, and produces visualizations for:

* *Funding trends over time*
* *Top funded sectors*
* *City-wise funding hotspots*
* *Most active investors*
* *Popular investment types*

The project also generates *recommendations* for both investors and startup founders.



🗂 Dataset

* *File used:* startup_funding.csv
* *Expected Columns:*

  * Date DD/MM/YYYY → Funding date
  * Startup Name → Name of the funded startup
  * Industry Vertical → Sector of the startup
  * City  Location → City where the startup is based
  * Investors Name → Investor(s) involved
  * InvestmentnType → Type of investment (e.g., Seed, Series A, etc.)
  * Amount in USD → Funding amount



⚙ Features

1. *Data Cleaning*

   * Standardizes column names
   * Converts date column to datetime format
   * Handles missing values
   * Cleans numeric funding amounts

2. *Visualizations*

   * *Line Chart:* Funding trends over time
   * *Bar Charts:*

     * Top 10 sectors by funding count
     * Top 10 cities by funding count
     * Top 10 startups by funding count
     * Top 10 investors by investment frequency
   * *Count Plot:* Distribution of investment types

3. *Recommendations*

   * Insights for investors and startup founders


 📦 Requirements

Install the following Python libraries before running the script:

bash
pip install pandas matplotlib seaborn




🚀 How to Run

1. Place your dataset (startup_funding.csv) in the correct path.
2. Run the Python script:

bash
python main.py


3. View the printed insights in the console and the generated charts.



📈 Sample Insights Generated

* *Top Sectors:* Displays the most popular industries for funding.
* *Hotspot Cities:* Shows cities with the highest startup activity.
* *Investment Trends:* Reveals the months/years with peak funding.
* *Investor Activity:* Identifies the most active investors.



📌 Future Improvements

* Add interactive dashboards using *Plotly* or *Streamlit*.
* Enable filtering by year, sector, or city.
* Predict future funding trends using machine learning models.

