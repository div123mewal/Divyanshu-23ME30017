import pandas as pd
import numpy as np

def load_or_generate_data(filepath=None):
    """Loads CSV data or generates realistic seasonal mock data for recruiters to test."""
    if filepath:
        try:
            return pd.read_csv(filepath, parse_dates=['date'])
        except FileNotFoundError:
            pass # Fallback to generator
            
    # Generate 2 years of daily sales data with trend, seasonality, and noise
    dates = pd.date_range(start='2024-01-01', periods=730)
    np.random.seed(42)
    trend = np.linspace(50, 120, 730)
    seasonality = 25 * np.sin(2 * np.pi * dates.dayofyear / 365.25)
    noise = np.random.normal(0, 8, 730)
    
    sales = trend + seasonality + noise
    # Prevent negative sales
    sales = np.maximum(sales, 5) 
    
    return pd.DataFrame({'date': dates, 'sales': sales})

def engineer_features(df):
    """Transforms raw dates into machine learning features."""
    df = df.sort_values('date').copy()
    
    # Time-based features
    df['dayofweek'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['quarter'] = df['date'].dt.quarter
    
    # Lag features (What were the sales 1 day ago? 7 days ago?)
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    
    # Rolling window statistics
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()
    
    # Drop rows with NaN values created by lag/rolling features
    return df.dropna()