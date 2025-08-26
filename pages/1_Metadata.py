import streamlit as st
import pandas as pd
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("📄 Metadata & Information")

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
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Column info
    st.subheader("Column Information")
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isna().sum(),
        'Unique Values': df.nunique()
    })
    st.dataframe(info_df)

    # Column descriptions
    COLUMN_INFO = {
        "age": {"Type": "numeric", "Description": "Age of the individual in years."},
        "sex": {"Type": "categorical", "Description": "Biological sex (0 = female, 1 = male)."},
        "cp": {"Type": "categorical", "Description": "Chest pain type."},
        "trestbps": {"Type": "numeric", "Description": "Resting blood pressure (mm Hg)."},
        "chol": {"Type": "numeric", "Description": "Serum cholesterol (mg/dL)."},
        "fbs": {"Type": "categorical", "Description": "Fasting blood sugar >120 mg/dL (0 = no, 1 = yes)."},
        "restecg": {"Type": "categorical", "Description": "Resting electrocardiogram results."},
        "thalach": {"Type": "numeric", "Description": "Max heart rate achieved."},
        "exang": {"Type": "categorical", "Description": "Exercise-induced angina (0 = no, 1 = yes)."},
        "oldpeak": {"Type": "numeric", "Description": "ST depression induced by exercise."},
        "slope": {"Type": "categorical", "Description": "Slope of the peak exercise ST segment."},
        "ca": {"Type": "categorical", "Description": "Number of major vessels (0–3)."},
        "thal": {"Type": "categorical", "Description": "Thalassemia status."},
        "smoking": {"Type": "categorical", "Description": "Smoking status (0 = no, 1 = yes)."},
        "diabetes": {"Type": "categorical", "Description": "Diabetes status (0 = no, 1 = yes)."},
        "bmi": {"Type": "numeric", "Description": "Body Mass Index (kg/m²)."},
        "heart_disease": {"Type": "binary target", "Description": "Presence of heart disease (0 = no, 1 = yes)."}
    }

    st.subheader("Column Descriptions")
    dict_df = pd.DataFrame(COLUMN_INFO).T.reset_index().rename(columns={"index": "Column"})
    st.dataframe(dict_df)
