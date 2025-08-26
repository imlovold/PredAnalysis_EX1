import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")

data = load_data()

st.title("📄 Metadata, Information & Summary")

# File metadata
FILE_PATH = "heart_disease_dataset.csv"
if os.path.exists(FILE_PATH):
    file_stat = os.stat(FILE_PATH)
    st.subheader("File Metadata")
    st.markdown(f"- **File type:** `{os.path.splitext(FILE_PATH)[1]}`")
    st.markdown(f"- **File size:** {file_stat.st_size / 1024:.2f} KB")
    st.markdown(f"- **Last modified:** {pd.to_datetime(file_stat.st_mtime, unit='s')} ")

# Column information
st.subheader("Column Information")
info_df = pd.DataFrame({
    'Column': data.columns,
    'Data Type': data.dtypes.astype(str),
    'Missing Values': data.isna().sum(),
    'Unique Values': data.nunique()
})
st.dataframe(info_df)

# Numeric summary
st.subheader("Numeric Summary")
st.dataframe(data.describe())

# Column dictionary
column_dict = {
    "age": ["numeric", "Age of the individual in years."],
    "sex": ["categorical", "Biological sex (0 = female, 1 = male)."],
    "cp": ["categorical", "Chest pain type (1 = typical angina, 2 = atypical angina, 3 = non-anginal pain, 4 = asymptomatic)."],
    "trestbps": ["numeric", "Resting blood pressure (mm Hg) measured on admission."],
    "chol": ["numeric", "Serum cholesterol (mg/dl)."],
    "fbs": ["categorical", "Fasting blood sugar >120 mg/dl (0 = false, 1 = true)."],
    "restecg": ["categorical", "Resting electrocardiogram results (0 = normal, 1 = ST-T abnormality, 2 = LV hypertrophy)."],
    "thalach": ["numeric", "Maximum heart rate achieved during exercise."],
    "exang": ["categorical", "Exercise-induced angina (0 = no, 1 = yes)."],
    "oldpeak": ["numeric", "ST depression induced by exercise relative to rest."],
    "slope": ["categorical", "Slope of the peak exercise ST segment (1 = upsloping, 2 = flat, 3 = downsloping)."],
    "ca": ["categorical", "Number of major vessels (0–3) colored by fluoroscopy."],
    "thal": ["categorical", "Thalassemia status (3 = normal, 6 = fixed defect, 7 = reversible defect)."],
    "smoking": ["categorical", "Current smoking status (0 = no, 1 = yes)."],
    "diabetes": ["categorical", "Diabetes status (0 = no, 1 = yes)."],
    "bmi": ["numeric", "Body Mass Index (kg/m²)."],
    "heart_disease": ["binary target", "Presence of heart disease (0 = no, 1 = yes)."]
}

df_dict = pd.DataFrame.from_dict(column_dict, orient="index", columns=["Type", "Description"])
df_dict.index.name = "Column"

st.subheader("Data Dictionary")
st.dataframe(df_dict)

# Data limitations
st.subheader("Data Limitations & Considerations")
st.markdown("""
- **Missing Values:** Check for NaNs or placeholder values (e.g., -9).
- **Granularity:** Data is at the individual level; periodicity not represented.
- **Update Frequency:** Likely static, may not reflect current trends.
- **Missing Variables:** E.g., medication history, diet, genetics beyond 'famhist'.
- **Potential Bias:** Some groups may be underrepresented.
- **Encoding Limitations:** Numeric codes for categorical variables need decoding.
""")
