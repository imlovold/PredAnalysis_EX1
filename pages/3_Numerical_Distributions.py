import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

COLUMN_DESCRIPTIONS = {
    "age": "Age of the individual in years.",
    "trestbps": "Resting blood pressure (mm Hg) on admission.",
    "chol": "Serum cholesterol (mg/dL).",
    "thalach": "Maximum heart rate achieved during exercise.",
    "oldpeak": "ST depression induced by exercise relative to rest.",
    "bmi": "Body Mass Index (kg/m²)."
}

st.title("Numeric Variable Explorer")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    # Only numeric variables
    numeric_cols = [c for c in df.columns if df[c].dtype in ["int64", "float64"] and df[c].nunique() > 15]

    if not numeric_cols:
        st.warning("No numeric variables found in this dataset.")
    else:
        selected_col = st.selectbox("Choose a numeric variable:", numeric_cols)

        # Show description if available
        st.markdown(f"**Description:** {COLUMN_DESCRIPTIONS.get(selected_col, 'No description available.')}")

        # Histogram
        st.subheader(f"Distribution of {selected_col}")
        fig, ax = plt.subplots(figsize=(6,4))
        ax.hist(df[selected_col].dropna(), bins=20, color="steelblue", edgecolor="black")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

        # Boxplot
        st.subheader(f"Boxplot of {selected_col}")
        fig, ax = plt.subplots(figsize=(6,2))
        ax.boxplot(df[selected_col].dropna(), vert=False)
        ax.set_xlabel(selected_col)
        st.pyplot(fig)
else:
    st.error(f"File '{FILE_PATH}' not found.")
