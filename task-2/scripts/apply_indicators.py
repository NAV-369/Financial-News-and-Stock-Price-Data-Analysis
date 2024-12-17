import os
import pandas as pd
import talib
from prepare_data import load_and_prepare_data  # Import the function

def calculate_indicators(df):
    """
    Calculate technical indicators using TA-Lib
    """
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['SMA_200'] = talib.SMA(df['Close'], timeperiod=200)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(
        df['Close'], fastperiod=12, slowperiod=26, signalperiod=9
    )
    return df

def apply_indicators_to_all_files(stock_data_frames):
    """
    Apply indicators to all stock data files
    """
    processed_data = pd.DataFrame()  # Initialize an empty DataFrame for concatenated data

    for file, df in stock_data_frames.items():
        print(f"Applying indicators to {file}")
        df = calculate_indicators(df)
        processed_data = pd.concat([processed_data, df], ignore_index=True)  # Combine all data

    return processed_data

if __name__ == "__main__":
    # Path to the data folder
    data_folder = "./data/"
    
    # Load and prepare data
    stock_data_frames = load_and_prepare_data(data_folder)

    # Apply indicators and save processed data
    processed_data = apply_indicators_to_all_files(stock_data_frames)

    # Save processed data to a CSV file
    output_file = os.path.join(data_folder, "processed_data_with_indicators.csv")
    processed_data.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")