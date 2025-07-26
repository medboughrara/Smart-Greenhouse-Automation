import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Smart Greenhouse Dashboard",
    page_icon="🌱",
    layout="wide"
)

def load_data():
    """Load and preprocess the dataset."""
    try:
        df = pd.read_csv('data/IoTProcessed_Data.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def plot_temperature_humidity(df):
    """Create temperature and humidity visualization."""
    st.subheader("Temperature and Humidity Over Time")
    
    fig = plt.figure(figsize=(12, 6))
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    
    sns.lineplot(data=df, x='date', y='tempreature', color='red', ax=ax1, label='Temperature')
    sns.lineplot(data=df, x='date', y='humidity', color='blue', ax=ax2, label='Humidity')
    
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Temperature (°C)', color='red')
    ax2.set_ylabel('Humidity (%)', color='blue')
    
    # Combine legends
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
    
    plt.title('Temperature and Humidity Trends')
    st.pyplot(fig)
    plt.close()

def plot_water_level(df):
    """Create water level visualization."""
    st.subheader("Water Level Status")
    
    fig = px.line(df, x='date', y='water_level',
                  title='Water Level Over Time')
    fig.add_hline(y=50, line_dash="dash", line_color="red",
                  annotation_text="Critical Level")
    st.plotly_chart(fig)

def plot_npk_levels(df):
    """Create NPK levels visualization."""
    st.subheader("NPK Levels")
    
    # Create a long-format DataFrame for NPK levels
    npk_df = df[['date', 'N', 'P', 'K']].melt(
        id_vars=['date'],
        var_name='Nutrient',
        value_name='Level'
    )
    
    fig = px.line(npk_df, x='date', y='Level', color='Nutrient',
                  title='NPK Levels Over Time')
    st.plotly_chart(fig)

def plot_actuator_status(df):
    """Create actuator status visualization."""
    st.subheader("Actuator Activity")
    
    # Calculate actuator activation percentages
    total_records = len(df)
    fan_active = (df['Fan_actuator_ON'].sum() / total_records) * 100
    water_pump_active = (df['Watering_plant_pump_ON'].sum() / total_records) * 100
    
    # Create metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Fan Usage", f"{fan_active:.1f}%")
    with col2:
        st.metric("Water Pump Usage", f"{water_pump_active:.1f}%")
    
    # Create correlation heatmap
    st.subheader("Parameter Correlations")
    corr_matrix = df[['tempreature', 'humidity', 'water_level', 'N', 'P', 'K',
                      'Fan_actuator_ON', 'Watering_plant_pump_ON']].corr()
    
    fig = plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation between Parameters and Actuator Actions')
    st.pyplot(fig)
    plt.close()

def main():
    st.title("🌱 Smart Greenhouse Monitoring Dashboard")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Sidebar filters
    st.sidebar.title("Filters")
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(df['date'].min().date(), df['date'].max().date())
    )
    
    # Filter data based on date range
    mask = (df['date'].dt.date >= date_range[0]) & (df['date'].dt.date <= date_range[1])
    filtered_df = df[mask]
    
    # Display current conditions
    st.header("Current Conditions")
    latest = filtered_df.iloc[-1]
    cols = st.columns(6)
    cols[0].metric("Temperature", f"{latest['tempreature']:.1f}°C")
    cols[1].metric("Humidity", f"{latest['humidity']:.1f}%")
    cols[2].metric("Water Level", f"{latest['water_level']:.1f}%")
    cols[3].metric("Nitrogen", f"{latest['N']:.1f}")
    cols[4].metric("Phosphorus", f"{latest['P']:.1f}")
    cols[5].metric("Potassium", f"{latest['K']:.1f}")
    
    # Create visualizations
    plot_temperature_humidity(filtered_df)
    
    col1, col2 = st.columns(2)
    with col1:
        plot_water_level(filtered_df)
    with col2:
        plot_npk_levels(filtered_df)
    
    plot_actuator_status(filtered_df)

if __name__ == "__main__":
    main()
