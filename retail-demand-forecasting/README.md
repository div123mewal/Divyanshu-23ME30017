# 📈 Retail Demand Forecasting Engine

An end-to-end machine learning pipeline designed to forecast retail sales volume and optimize inventory management. This project structures time-series data, extracts rolling statistical features, and utilizes gradient boosting to generate accurate future demand predictions.

## 🧠 System Architecture
* **`data_pipeline.py`**: Handles ETL operations, generating chronological lag features (`t-1`, `t-7`) and rolling window averages to capture underlying seasonal trends.
* **`model.py`**: Implements an `XGBoost` regressor optimized for time-series splits, evaluated via Mean Absolute Percentage Error (MAPE) and RMSE.
* **`main.py`**: A Streamlit dashboard utilizing Plotly for interactive forecast visualization and performance tracking.

## 🚀 Execution Instructions
Install the required dependencies:
```bash
pip install -r requirements.txt