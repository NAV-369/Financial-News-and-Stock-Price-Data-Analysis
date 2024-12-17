import pandas as pd
import os

def load_and_prepare_data(folder_path):
    """
    Load and prepare stock price data from multiple CSV files.
    :param folder_path: Path to the folder containing CSV files.
    :return: A dictionary of DataFrames with file names as keys.
    """
    data_frames = {}
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']

    # Iterate through all CSV files in the folder
    for file in os.listdir(folder_path):
        if file.endswith('.csv'):
            file_path = os.path.join(folder_path, file)
            print(f"Loading data from: {file_path}")
            
            # Load the data into a DataFrame
            df = pd.read_csv(file_path)
            
            # Check if required columns exist
            for col in required_columns:
                if col not in df.columns:
                    raise ValueError(f"Missing required column '{col}' in file {file}")

            # Add the loaded DataFrame to the dictionary
            data_frames[file] = df
            print(f"Data from {file} loaded successfully.")
    
    return data_frames

if __name__ == "__main__":
    # Path to the data folder containing multiple CSV files (updated path)
    data_folder = "./data/"  # Actual relative path to data folder
    stock_data_frames = load_and_prepare_data(data_folder)

    # Print the keys (file names) and the first few rows of each DataFrame
    for file_name, df in stock_data_frames.items():
        print(f"\nData from file: {file_name}")
        print(df.head())  # Display the first few rows of each DataFrame