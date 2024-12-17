import os
import pandas as pd

def load_data(folder_path):
    """Load all CSV files from the 'data' folder and concatenate them into one DataFrame."""
    all_files = os.listdir(folder_path)
    
    # Filter out only CSV files in the 'data' folder
    csv_files = [f for f in all_files if f.endswith('.csv')]  
    
    # List to store data from each CSV file
    df_list = []
    
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        
        try:
            # Read each CSV file and append it to the list
            df = pd.read_csv(file_path)
            
            # Optionally, you can add a column to track the source file
            df['source'] = file
            
            # Append the dataframe to the list
            df_list.append(df)
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    # If no files are found or loaded, return None
    if not df_list:
        print("No CSV files found in the data folder.")
        return None
    
    # Concatenate all DataFrames into one large DataFrame
    all_data = pd.concat(df_list, ignore_index=True)
    
    # Ensure 'Date' is in datetime format (handle invalid date formats)
    all_data['Date'] = pd.to_datetime(all_data['Date'], errors='coerce')
    
    # Set 'Date' as the index
    all_data.set_index('Date', inplace=True)
    
    return all_data