import matplotlib.pyplot as plt

def plot_sma(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label='Close Price')
    plt.plot(df.index, df['SMA_50'], label='50-Day SMA')
    plt.plot(df.index, df['SMA_200'], label='200-Day SMA')
    plt.legend()
    plt.title('Simple Moving Averages (SMA)')
    plt.show()

def plot_rsi(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['RSI'], label='RSI')
    plt.axhline(y=30, color='r', linestyle='--', label='Oversold (30)')
    plt.axhline(y=70, color='g', linestyle='--', label='Overbought (70)')
    plt.legend()
    plt.title('Relative Strength Index (RSI)')
    plt.show()

def plot_macd(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['MACD'], label='MACD')
    plt.plot(df.index, df['MACD_Signal'], label='MACD Signal Line')
    plt.bar(df.index, df['MACD_Hist'], label='MACD Histogram', color='gray', alpha=0.3)
    plt.legend()
    plt.title('Moving Average Convergence Divergence (MACD)')
    plt.show()