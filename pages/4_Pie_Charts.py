import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("🥧 Pie Charts for Categorical Columns")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    cat_cols = df.select_dtypes(include=['int64', 'object']).columns.tolist()
    cat_cols = [c for c in cat_cols if df[c].nunique() <= 10]

    if cat_cols:
        selected_col = st.selectbox("Choose a column to display as a pie chart:", cat_cols)
        fig, ax = plt.subplots(figsize=(4,4))
        df[selected_col].value_counts().plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            ax=ax,
            wedgeprops={'edgecolor':'white'}
        )
        ax.set_ylabel("")
        ax.set_title(f"Distribution of {selected_col}")
        st.pyplot(fig)
    else:
        st.info("No suitable categorical columns found for pie charts.")
else:
    st.error(f"File '{FILE_PATH}' not found.")
