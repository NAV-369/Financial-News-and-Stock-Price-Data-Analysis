README for Task-2: Stock Price Analysis and Visualization

Objective

Task-2 focuses on analyzing stock price data by applying technical indicators and visualizing the results. The data analysis is conducted using pynance and saved in a Jupyter notebook within the notebook folder.

Steps to Complete Task-2
	1.	Set Up the Environment
	•	Ensure you have the required libraries (pynance, pandas, matplotlib, TA-Lib) installed in your virtual environment.
	•	Activate your environment using:

source /path-to-your-env/bin/activate

	2.	Retrieve Stock Data
	•	Use pynance to retrieve historical stock price data for a specific ticker.
Example:

import pynance as pn

# Retrieve stock data for a specific ticker (e.g., "AAPL")
ticker = "AAPL"
stock_data = pn.data.equities.retrieve(ticker)

# Display the first few rows of the data
print(stock_data.head())

	3.	Calculate Technical Indicators
Apply commonly used indicators to analyze the stock data.
	•	Simple Moving Average (SMA):
Calculate a rolling average of closing prices.

stock_data['SMA_20'] = stock_data['Close'].rolling(window=20).mean()
print(stock_data[['Close', 'SMA_20']].head())


	•	Relative Strength Index (RSI):
Measure the speed and change of price movements.

import talib
stock_data['RSI'] = talib.RSI(stock_data['Close'], timeperiod=14)
print(stock_data[['Close', 'RSI']].head())


	•	Moving Average Convergence Divergence (MACD):
Evaluate momentum using MACD and its signal line.

stock_data['MACD'], stock_data['Signal'], _ = talib.MACD(
    stock_data['Close'], 
    fastperiod=12, 
    slowperiod=26, 
    signalperiod=9
)
print(stock_data[['Close', 'MACD', 'Signal']].head())

	4.	Visualize Stock Data
	•	Plot stock prices and technical indicators to understand trends.
Example:

import matplotlib.pyplot as plt

# Plot stock prices
plt.figure(figsize=(10, 6))
plt.plot(stock_data['Close'], label='Close Price', color='blue')
plt.plot(stock_data['SMA_20'], label='20-Day SMA', color='orange')
plt.title('Stock Prices with 20-Day SMA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

	5.	Save and Document Results
	•	Save the analysis in a .ipynb file located in the notebook folder.
	•	Include comments and descriptions for each step in the notebook to ensure readability and clarity.

Deliverables
	•	A completed Jupyter notebook (.ipynb) in the notebook folder.
	•	Visualizations showcasing stock price trends and applied technical indicators.