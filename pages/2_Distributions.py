import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")

data = load_data()

# Manually define categorical and numeric variables based on data dictionary
categorical_cols = [
    "sex", "cp", "fbs", "restecg", "exang",
    "slope", "ca", "thal", "smoking", "diabetes", "heart_disease"
]
numeric_cols = [
    "age", "trestbps", "chol", "thalach", "oldpeak", "bmi"
]

# Frequency tables for categorical variables
st.header("Categorical Variables")
for col in categorical_cols:
    st.subheader(f"{col}")
    st.write(data[col].value_counts())

# Histograms for numeric variables
st.header("Distributions of Numerical Variables")
for col in numeric_cols:
    fig, ax = plt.subplots()
    sns.histplot(data[col], kde=True, ax=ax, color="skyblue")
    ax.set_title(f"Distribution of {col}")
    st.pyplot(fig)

