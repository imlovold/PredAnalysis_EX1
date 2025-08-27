import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

# Column descriptions with mappings
COLUMN_INFO = {
    "sex": {"Description": "Biological sex", "Categories": {0: "Female", 1: "Male"}},
    "cp": {"Description": "Chest pain type", "Categories": {
        1: "Typical angina", 2: "Atypical angina", 3: "Non-anginal pain", 4: "Asymptomatic"}},
    "fbs": {"Description": "Fasting blood sugar >120 mg/dL", "Categories": {0: "No", 1: "Yes"}},
    "restecg": {"Description": "Resting electrocardiogram results", "Categories": {
        0: "Normal", 1: "ST-T abnormality", 2: "Left ventricular hypertrophy"}},
    "exang": {"Description": "Exercise-induced angina", "Categories": {0: "No", 1: "Yes"}},
    "slope": {"Description": "Slope of the peak exercise ST segment", "Categories": {
        1: "Upsloping", 2: "Flat", 3: "Downsloping"}},
    "ca": {"Description": "Number of major vessels colored by fluoroscopy", "Categories": {
        0: "0 vessels", 1: "1 vessel", 2: "2 vessels", 3: "3 vessels"}},
    "thal": {"Description": "Thalassemia status", "Categories": {
        3: "Normal", 6: "Fixed defect", 7: "Reversible defect"}},
    "smoking": {"Description": "Smoking status", "Categories": {0: "No", 1: "Yes"}},
    "diabetes": {"Description": "Diabetes status", "Categories": {0: "No", 1: "Yes"}},
    "heart_disease": {"Description": "Presence of heart disease", "Categories": {
        0: "No heart disease", 1: "Heart disease"}}
}

st.title("Categorical Variable Explorer")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    # Automatically map integer codes to labels where defined
    for col, info in COLUMN_INFO.items():
        if "Categories" in info:
            df[col] = df[col].map(info["Categories"]).astype("category")

    # Get categorical columns
    categorical_cols = list(COLUMN_INFO.keys())

    if not categorical_cols:
        st.warning("No categorical variables found in this dataset.")
    else:
        selected_col = st.selectbox("Choose a categorical variable:", categorical_cols)

        # Show description if available
        st.markdown(f"**Description:** {COLUMN_INFO[selected_col]['Description']}")

        # Frequency table
        st.subheader(f"Frequency Table for {selected_col}")
        st.write(df[selected_col].value_counts())

        # Bar chart
        st.subheader(f"Distribution of {selected_col}")
        fig, ax = plt.subplots(figsize=(6,4))
        df[selected_col].value_counts().plot(kind="bar", ax=ax, color="steelblue", edgecolor="black")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Count")
        st.pyplot(fig)

else:
    st.error(f"File '{FILE_PATH}' not found.")
