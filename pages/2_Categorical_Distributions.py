import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("📊 Categorical Distributions")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    categorical_cols = df.select_dtypes(include=['int64', 'object']).columns.tolist()
    for col in categorical_cols:
        if df[col].nunique() < 20:
            st.write(f"**{col}**")
            fig, ax = plt.subplots(figsize=(4,3))
            df[col].value_counts().plot(kind='bar', ax=ax)
            st.pyplot(fig)
else:
    st.error(f"File '{FILE_PATH}' not found.")
