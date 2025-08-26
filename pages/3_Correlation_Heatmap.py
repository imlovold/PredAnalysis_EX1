import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")

data = load_data()

st.title("Correlation Heatmap")

numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()

if len(numeric_cols) > 1:
    # Full correlation heatmap
    st.subheader("Full Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10,8))
    sns.heatmap(data[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    # Correlation with target
    if "heart_disease" in data.columns:
        st.subheader("Correlation with Target (heart_disease)")
        fig, ax = plt.subplots(figsize=(4,6))
        corr_target = data[numeric_cols].corr()[["heart_disease"]].sort_values(by="heart_disease", ascending=False)
        sns.heatmap(corr_target, annot=True, fmt=".2f", cmap="coolwarm", ax=ax, cbar=True, vmin=-1, vmax=1)
        st.pyplot(fig)
else:
    st.warning("Not enough numeric columns for correlation analysis.")