import talib

def calculate_indicators(df):
    """Calculate technical indicators and add them to the DataFrame."""
    
    # Calculate 50-day and 200-day Simple Moving Averages
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    
    # Calculate RSI (Relative Strength Index)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    
    # Calculate MACD (Moving Average Convergence Divergence)
    macd, macdsignal, macdhist = talib.MACD(df['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    df['MACD'] = macd
    df['MACD_Signal'] = macdsignal
    df['MACD_Hist'] = macdhist
    
    return df