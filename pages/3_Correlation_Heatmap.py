import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("📈 Correlation Heatmap")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(10,8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns for correlation analysis.")
else:
    st.error(f"File '{FILE_PATH}' not found.")
