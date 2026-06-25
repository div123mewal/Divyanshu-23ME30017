import streamlit as st
import plotly.graph_objects as go
from data_pipeline import load_or_generate_data, engineer_features
from model import train_and_evaluate

st.set_page_config(page_title="Retail Demand Forecasting", layout="wide")

st.title("📈 Retail Demand Forecasting Engine")
st.markdown("An end-to-end time-series forecasting pipeline using **XGBoost** to predict inventory demand based on historical sales, seasonality, and lag features.")

# Pipeline Execution
with st.spinner("Extracting data and engineering time-series features..."):
    raw_data = load_or_generate_data()
    processed_data = engineer_features(raw_data)
    
with st.spinner("Training XGBoost Regressor..."):
    model, mape, rmse, test_df = train_and_evaluate(processed_data)

# Sidebar KPI Dashboard
st.sidebar.header("Model Performance (Test Set)")
st.sidebar.metric("Mean Absolute Percentage Error (MAPE)", f"{mape:.2%}")
st.sidebar.metric("Root Mean Squared Error (RMSE)", f"{rmse:.2f} units")
st.sidebar.markdown("---")
st.sidebar.markdown("**Features Used:**\n- Day of Week\n- Month / Quarter\n- 1-Day Lag\n- 7-Day Lag\n- 7-Day Rolling Average")

# Visualization
st.subheader("Actual Sales vs. Model Forecast")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=test_df['date'], y=test_df['sales'], 
    name='Actual Sales', line=dict(color='#1f77b4', width=2)
))
fig.add_trace(go.Scatter(
    x=test_df['date'], y=test_df['predictions'], 
    name='XGBoost Forecast', line=dict(color='#ff7f0e', width=2, dash='dot')
))

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales Volume",
    hovermode="x unified",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

st.plotly_chart(fig, use_container_width=True)

# Data Table
with st.expander("View Raw Forecast Data"):
    st.dataframe(test_df[['date', 'sales', 'predictions']].sort_values('date', ascending=False))