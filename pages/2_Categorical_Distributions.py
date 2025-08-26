import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")


data = load_data()


st.header("Categorical Distributions")


categorical_cols = ['cp', 'thal', 'restecg', 'slope']
for col in categorical_cols:
    st.write(f"**{col}**")
    st.write(data[col].value_counts())
