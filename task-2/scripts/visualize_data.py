import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df):
    """
    Plot stock price data along with technical indicators and financial metrics.
    :param df: DataFrame containing stock price data, technical indicators, and financial metrics
    """
    plt.figure(figsize=(12, 10))

    # Plot Close Price
    plt.subplot(4, 1, 1)
    plt.plot(df['Close'], label='Close Price')
    plt.title('Stock Price (Close)')
    plt.legend()

    # Plot Moving Averages
    plt.subplot(4, 1, 2)
    plt.plot(df['SMA_50'], label='50-day SMA', color='orange')
    plt.plot(df['SMA_200'], label='200-day SMA', color='blue')
    plt.title('Moving Averages')
    plt.legend()

    # Plot RSI
    plt.subplot(4, 1, 3)
    plt.plot(df['RSI'], label='RSI', color='purple')
    plt.axhline(y=70, color='r', linestyle='--')
    plt.axhline(y=30, color='r', linestyle='--')
    plt.title('RSI (Relative Strength Index)')
    plt.legend()

    # Plot P/E ratio (if available)
    if 'PE_ratio' in df.columns:
        plt.subplot(4, 1, 4)
        plt.plot(df['PE_ratio'], label='P/E Ratio', color='green')
        plt.title('P/E Ratio')
        plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Load the processed data that includes indicators and financial metrics
    df = pd.read_csv("data/processed_data_with_indicators.csv")
    
    plot_stock_data(df)