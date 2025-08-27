import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Column descriptions with mappings (same as Metadata page)
COLUMN_INFO = {
    "sex": {"Type": "categorical", "Description": "Biological sex", "Categories": {0: "Female", 1: "Male"}},
    "cp": {"Type": "categorical", "Description": "Chest pain type", "Categories": {
        1: "Typical angina", 2: "Atypical angina", 3: "Non-anginal pain", 4: "Asymptomatic"}},
    "fbs": {"Type": "categorical", "Description": "Fasting blood sugar >120 mg/dL", "Categories": {0: "No", 1: "Yes"}},
    "restecg": {"Type": "categorical", "Description": "Resting ECG results", "Categories": {
        0: "Normal", 1: "ST-T abnormality", 2: "Left ventricular hypertrophy"}},
    "exang": {"Type": "categorical", "Description": "Exercise-induced angina", "Categories": {0: "No", 1: "Yes"}},
    "slope": {"Type": "categorical", "Description": "Slope of the peak exercise ST segment", "Categories": {
        1: "Upsloping", 2: "Flat", 3: "Downsloping"}},
    "ca": {"Type": "categorical", "Description": "Number of major vessels colored by fluoroscopy", "Categories": {
        0: "0 vessels", 1: "1 vessel", 2: "2 vessels", 3: "3 vessels"}},
    "thal": {"Type": "categorical", "Description": "Thalassemia status", "Categories": {
        3: "Normal", 6: "Fixed defect", 7: "Reversible defect"}},
    "smoking": {"Type": "categorical", "Description": "Smoking status", "Categories": {0: "No", 1: "Yes"}},
    "diabetes": {"Type": "categorical", "Description": "Diabetes status", "Categories": {0: "No", 1: "Yes"}},
    "heart_disease": {"Type": "binary target", "Description": "Presence of heart disease", "Categories": {
        0: "No heart disease", 1: "Heart disease"}}
}

@st.cache_data
def load_data():
    df = pd.read_csv("heart_disease_dataset.csv")

    # Cast categorical columns and apply label mappings
    for col, info in COLUMN_INFO.items():
        if info["Type"].startswith("categorical") or info["Type"].startswith("binary"):
            if "Categories" in info:
                df[col] = df[col].map(info["Categories"]).astype("category")
            else:
                df[col] = df[col].astype("category")
    return df

data = load_data()

st.title("📊 Categorical Distributions")

categorical_cols = list(COLUMN_INFO.keys())

for col in categorical_cols:
    st.subheader(f"{col}: {COLUMN_INFO[col]['Description']}")

    # Frequency table
    st.write("Frequency Table:")
    st.write(data[col].value_counts())

    # Bar chart
    fig, ax = plt.subplots()
    sns.countplot(x=data[col], ax=ax, palette="Set2", order=data[col].value_counts().index)
    ax.set_title(f"Distribution of {col}")
    ax.set_xlabel("")
    ax.set_ylabel("Count")
    st.pyplot(fig)

