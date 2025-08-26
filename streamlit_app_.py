import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")

data = load_data()

st.title("Heart Disease Dataset Dashboard")
st.write("Use the sidebar to explore metadata, distributions, correlations, and more.")

st.write("### Dataset Quick Info")
st.write(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")
st.dataframe(data.head())