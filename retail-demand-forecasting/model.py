from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import numpy as np

def train_and_evaluate(df):
    """Splits time-series data chronologically, trains XGBoost, and evaluates."""
    # Chronological split (80% train, 20% test)
    train_size = int(len(df) * 0.8)
    train, test = df.iloc[:train_size], df.iloc[train_size:]

    features = ['dayofweek', 'month', 'quarter', 'lag_1', 'lag_7', 'rolling_mean_7']
    X_train, y_train = train[features], train['sales']
    X_test, y_test = test[features], test['sales']

    # Initialize and train XGBoost
    model = XGBRegressor(n_estimators=150, learning_rate=0.05, max_depth=5, random_state=42)
    model.fit(X_train, y_train)

    # Generate Forecast
    predictions = model.predict(X_test)
    
    # Calculate Business Metrics
    mape = mean_absolute_percentage_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    # Package results for visualization
    test_results = test.copy()
    test_results['predictions'] = predictions

    return model, mape, rmse, test_results