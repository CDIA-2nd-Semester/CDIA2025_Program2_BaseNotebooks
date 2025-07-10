
import pandas as pd

def load_data(route):
    """
    Load data from a CSV file.

    Parameters:
    route (str): The file path to the CSV file.

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    df = pd.read_csv(route)
    return df

