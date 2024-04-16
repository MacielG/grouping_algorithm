# data_handler.py
import pandas as pd

def load_data():
    # Placeholder for data source connection
    # Example: Load data from a CSV file
    try:
        data = pd.read_csv('path_to_data.csv')
        # Validate data
        if 'gender' not in data.columns or 'age' not in data.columns:
            raise ValueError("Missing required columns in data")
        return data
    except FileNotFoundError:
        print("Data file not found.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
