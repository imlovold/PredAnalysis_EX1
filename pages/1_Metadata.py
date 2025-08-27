import streamlit as st
import pandas as pd
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("Metadata & Information")

# Column descriptions with mappings
COLUMN_INFO = {
    "age": {"Type": "numeric", "Description": "Age of the individual in years."},
    "sex": {"Type": "categorical", "Description": "Biological sex", "Categories": {0: "Female", 1: "Male"}},
    "cp": {"Type": "categorical", "Description": "Chest pain type", "Categories": {
        1: "Typical angina", 2: "Atypical angina", 3: "Non-anginal pain", 4: "Asymptomatic"}},
    "trestbps": {"Type": "numeric", "Description": "Resting blood pressure (mm Hg)."},
    "chol": {"Type": "numeric", "Description": "Serum cholesterol (mg/dL)."},
    "fbs": {"Type": "categorical", "Description": "Fasting blood sugar >120 mg/dL", "Categories": {0: "No", 1: "Yes"}},
    "restecg": {"Type": "categorical", "Description": "Resting electrocardiogram results", "Categories": {
        0: "Normal", 1: "ST-T abnormality", 2: "Left ventricular hypertrophy"}},
    "thalach": {"Type": "numeric", "Description": "Max heart rate achieved."},
    "exang": {"Type": "categorical", "Description": "Exercise-induced angina", "Categories": {0: "No", 1: "Yes"}},
    "oldpeak": {"Type": "numeric", "Description": "ST depression induced by exercise."},
    "slope": {"Type": "categorical", "Description": "Slope of the peak exercise ST segment", "Categories": {
        1: "Upsloping", 2: "Flat", 3: "Downsloping"}},
    "ca": {"Type": "categorical", "Description": "Number of major vessels (0–3)", "Categories": {
        0: "0 vessels", 1: "1 vessel", 2: "2 vessels", 3: "3 vessels"}},
    "thal": {"Type": "categorical", "Description": "Thalassemia status", "Categories": {
        3: "Normal", 6: "Fixed defect", 7: "Reversible defect"}},
    "smoking": {"Type": "categorical", "Description": "Smoking status", "Categories": {0: "No", 1: "Yes"}},
    "diabetes": {"Type": "categorical", "Description": "Diabetes status", "Categories": {0: "No", 1: "Yes"}},
    "bmi": {"Type": "numeric", "Description": "Body Mass Index (kg/m²)."},
    "heart_disease": {"Type": "binary target", "Description": "Presence of heart disease", "Categories": {
        0: "No heart disease", 1: "Heart disease"}}
}

if not os.path.exists(FILE_PATH):
    st.error(f"File '{FILE_PATH}' not found.")
else:
    file_stat = os.stat(FILE_PATH)

    # File metadata
    st.subheader("File Metadata")
    st.markdown(f"- **File type:** `{os.path.splitext(FILE_PATH)[1]}`")
    st.markdown(f"- **File size:** {file_stat.st_size / 1024:.2f} KB")
    st.markdown(f"- **Last modified:** {pd.to_datetime(file_stat.st_mtime, unit='s')} ")

    # Load data
    df = pd.read_csv(FILE_PATH)

    # Data dimensions
    st.subheader("Data Dimensions")
    st.markdown(f"- **Number of rows:** {df.shape[0]}")
    st.markdown(f"- **Number of columns:** {df.shape[1]}")

    # Preview 
    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    # Column descriptions
    st.subheader("Column Descriptions")
    dict_df = pd.DataFrame([
        {"Column": col,
         "Type": info["Type"],
         "Description": info["Description"],
         "Categories": info.get("Categories", None)}
        for col, info in COLUMN_INFO.items()
    ])
    st.dataframe(dict_df)

    # Cast categorical/binary variables + apply label mappings
    for col, info in COLUMN_INFO.items():
        if info["Type"].startswith("categorical") or info["Type"].startswith("binary"):
            if "Categories" in info:
                df[col] = df[col].map(info["Categories"]).astype("category")
            else:
                df[col] = df[col].astype("category")

    # Preview
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Encoding categorical labels
    categorical_cols = [col for col, info in COLUMN_INFO.items()
                        if info["Type"].startswith("categorical") or info["Type"].startswith("binary")]

    st.subheader("Encoding Categorical Variables")

    # Apply one-hot encoding
    encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    st.write("After one-hot encoding (first 5 rows, new binary columns created):")
    st.dataframe(encoded.head())

    st.markdown("""
    *Note:* One-hot encoding expands categorical variables into multiple binary columns.  
    For example, `cp` (1–4) becomes `cp_2`, `cp_3`, `cp_4`.  
    This avoids the model treating categories as numeric values with an order.
    """)