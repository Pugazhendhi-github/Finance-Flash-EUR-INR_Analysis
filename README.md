# Yahoo_Finance_currency_analysis

# EUR/INR Currency Data Analysis
This repository contains code and data for analyzing historical exchange rates between the Euro (EUR) and the Indian Rupee (INR). We’ll use Python libraries such as NumPy, Pandas, and Matplotlib to explore the data, visualize trends, and draw insights.

# Project Structure
data/: Contains historical EUR/INR exchange rate data (CSV files).
notebooks/: Jupyter notebooks for data analysis.
scripts/: Python scripts for data manipulation and visualization.
README.md: This file.
Getting Started
Clone the Repository:
git clone https://github.com/pugazhendhi-github/Yahoo_Finance_currency_analysis.git
cd EUR-INR-currency-analysis

# Install Dependencies:
pip install numpy pandas matplotlib

# Explore the Data:
Load the EUR/INR exchange rate data.
Clean and preprocess the data (handle missing values, outliers, etc.).
# Analyze Trends:
Calculate statistical measures (mean, median, variance, etc.).
Identify patterns or anomalies.
# Visualize Results:
Create line plots, scatter plots, or bar charts.
Use Matplotlib to visualize exchange rate trends over time.
# Notebooks
EUR_INR_Analysis.ipynb: Jupyter notebook with step-by-step analysis.
Feel free to create additional notebooks for specific analyses.
Contributing
Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.
# Moving Averages (MA):
Simple Moving Average (SMA): Calculates the average price over a specified period (e.g., 50 days). A bullish signal occurs when the current price crosses above the SMA, and a bearish signal when it crosses below.
Exponential Moving Average (EMA): Similar to SMA but gives more weight to recent prices. EMA crossovers can indicate buy or sell opportunities.

# Relative strength index

Relative Strength Index (RSI):
RSI measures the strength and speed of price movements. Values above 70 indicate overbought conditions (potential sell signal), while values below 30 suggest oversold conditions (potential buy signal).
# Bollinger Bands:
Consists of an upper band (standard deviation above the moving average) and a lower band (standard deviation below). Price crossing the bands can signal buy or sell opportunities.
