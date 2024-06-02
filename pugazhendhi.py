import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing dataset
yahoo_fin = pd.read_csv('EURINR=X.csv', index_col='Date', parse_dates=True)
# Remove NULL values
yahoo_fin.dropna(inplace=True)
# Extract 'Closing Price' column and convert to DataFrame
yahoo_fin = yahoo_fin['Closing Price'].to_frame()

# One day Moving Average (SMA)
yahoo_fin['Simple Moving Average'] = yahoo_fin['Closing Price'].rolling(window=2).mean()
yahoo_fin['STD'] = statistics.stdev(yahoo_fin['Closing Price'])
yahoo_fin[['Closing Price', 'Simple Moving Average']].plot(figsize=(16, 8))
plt.title("EUR/INR moving average for one day")

# One day Bollinger Band
yahoo_fin['Upper Band'] = yahoo_fin['Closing Price'].rolling(window=2).mean() + 2 * yahoo_fin['STD']
yahoo_fin['Lower Band'] = yahoo_fin['Closing Price'].rolling(window=2).mean() - 2 * yahoo_fin['STD']
yahoo_fin[['Closing Price', 'Simple Moving Average', 'Upper Band', 'Lower Band']].plot(figsize=(16, 8))
plt.title("EUR/INR Bollinger Band for one day")
plt.xlabel("Date")
plt.ylabel("EUR/INR stock price")
plt.legend()
plt.show()

# One week Moving Average (SMA)
yahoo_fin['Simple Moving Average'] = yahoo_fin['Closing Price'].rolling(window=7).mean()
yahoo_fin['STD'] = statistics.stdev(yahoo_fin['Closing Price'])

# One week Bollinger Band
yahoo_fin['UpperBand'] = yahoo_fin['Closing Price'].rolling(window=7).mean() + 2 * yahoo_fin['STD']
yahoo_fin['LowerBand'] = yahoo_fin['Closing Price'].rolling(window=7).mean() - 2 * yahoo_fin['STD']
yahoo_fin[['Closing Price', 'Simple Moving Average', 'UpperBand', 'LowerBand']].plot(figsize=(16, 8))
plt.title("EUR/INR Bollinger Band for one week")
yahoo_fin[['Closing Price', 'Simple Moving Average']].plot(figsize=(16, 8))
plt.title("EUR/INR moving average for one week")
plt.xlabel("Date")
plt.ylabel("EUR/INR stock price")
plt.legend()
plt.show()

data = pd.read_csv('EURINR=X.csv', index_col='Date', parse_dates=True)

# One day CCI
fig1, ax = plt.subplots(2, sharex=True)
data['Closing Price'] = data['Closing Price']
data['typical_price'] = (data['Closing Price'] + data['High'] + data['Low']) / 3
data["SMA"] = data["typical_price"].rolling(window=2).mean()
data["mean_deviation"] = np.abs(data['typical_price'] - data["SMA"]).rolling(window=2).mean()
data['CCI'] = (data['typical_price'] - data['SMA']) / (0.015 * data['mean_deviation'])
ax[0].plot(data["Closing Price"], color='blue', label="Closing price")
plt.legend(loc='upper left')
ax[1].plot(data["CCI"], color='black', label="EUR/INR CCI One Day")
plt.legend()
plt.suptitle("EUR/INR CCI One Day")
plt.xlabel("Date")
plt.show()

# One week CCI
fig1, ax = plt.subplots(2, sharex=True)
data['typical_price'] = (data['Closing Price'] + data['High'] + data['Low']) / 3
data['Closing Price'] = data['Closing Price']
data["SMA"] = data["typical_price"].rolling(window=7).mean()
data["SMA"] = data["typical_price"].rolling(window=7).mean()
data["mean_deviation"] = np.abs(data['typical_price'] - data["SMA"]).rolling(window=7).mean()
data['CCI'] = (data['typical_price'] - data['SMA']) / (0.015 * data['mean_deviation'])
ax[0].plot(data["Closing Price"], color='blue', label="Closing Price")
plt.legend()
ax[1].plot(data["CCI"], color='black', label="EUR/INR CCI One week")
plt.legend()
plt.suptitle("EUR/INR CCI One week")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.show()

# One day BUY, SELL Indicators
plt.figure(figsize=(12, 6))
plt.plot(data["Closing Price"], label="EUR/INR Closing Price", color='black')
plt.plot(data["Closing Price"].rolling(window=2).mean(), label="One Day Moving Averages", color='blue')
buy = np.where((data['Closing Price'] > data["Closing Price"].rolling(window=2).mean()) & (data['Closing Price'].shift(1) < data["Closing Price"].rolling(window=2).mean().shift(1)), 1, np.nan) * 0.95 * data['Low']
sell = np.where((data["Closing Price"].rolling(window=2).mean() > data['Closing Price']) & (data["Closing Price"].rolling(window=2).mean().shift(1) < data['Closing Price'].shift(1)), 1, np.nan) * 0.95 * data['High']
plt.scatter(data.index, buy, color='green', marker='^', label='Buy Signal')
plt.scatter(data.index, sell, color='red', marker='v', label='Sell Signal')
plt.title("EUR/INR Moving Averages One Day")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt.show()

# One week BUY, SELL Indicators
plt.plot(data["Closing Price"], label="EUR/INR Closing Price", color='black')
plt.plot(data["Closing Price"].rolling(window=7).mean(), label="One Week Moving Averages", color='blue')
buy = np.where((data['Closing Price'] > data["Closing Price"].rolling(window=7).mean()) & (data['Closing Price'].shift(1) < data["Closing Price"].rolling(window=7).mean().shift(1)), 1, np.nan) * 0.95 * data['Low']
sell = np.where((data["Closing Price"].rolling(window=7).mean() > data['Closing Price']) & (data["Closing Price"].rolling(window=7).mean().shift(1) < data['Closing Price'].shift(1)), 1, np.nan) * 0.95 * data['High']
plt.scatter(data.index, buy, color='green', marker='^', label='Buy Signal')
plt.scatter(data.index, sell, color='red', marker='v', label='Sell Signal')
plt.title("EUR/INR Moving Averages One Week")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt
