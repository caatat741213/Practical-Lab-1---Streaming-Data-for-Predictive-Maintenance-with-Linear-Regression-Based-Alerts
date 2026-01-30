
## Separate read : You can easily switch between reading local CSV files or cloud databases.

import pandas as pd
from sqlalchemy import create_engine
import os
import yaml
import os

def load_config(config_path):

    # Automatically load the YAML configuration file

    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        print(f"✅Config loaded: {config_path}")
        return config
    else:
        print(f"❌Config file not found: {config_path}")
        return None
    
def load_from_csv(file_path):

    # Load raw data from a CSV file
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"✅ CSV Loaded: {file_path}")
        return df
    else:
        print(f"❌File not found: {file_path}")
        return None

def load_from_db(db_url, table_name):

    # Load data from Neon Database (Adapted from your previous workshop)
    try:
        engine = create_engine(db_url)
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, engine)
        print(f"✅DB Data Loaded from {table_name}")
        return df
    except Exception as e:
        print(f"❌DB Connection Failed: {e}")
        return None

class StreamingSimulator:

    # Class to simulate robot data streaming

    def __init__(self, df):
        self.df = df
        self.current_index = 0

    def get_next_point(self):
        if self.current_index < len(self.df):
            point = self.df.iloc[[self.current_index]]
            self.current_index += 1
            return point
        return None
    
