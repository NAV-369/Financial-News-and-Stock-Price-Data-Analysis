import sys
import os

# Add the absolute path of the 'src' folder
sys.path.append(os.path.abspath('./src'))

# Test the imports
from src.data_loader import load_data
from src.indicators import calculate_indicators
from src.visualize import plot_sma, plot_rsi, plot_macd

print("Imports successful!")