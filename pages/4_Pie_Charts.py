import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    return pd.read_csv("heart_disease_dataset.csv")

data = load_data()

st.title("Pie Charts for Categorical Columns")

# Manually define categorical columns (based on data dictionary)
categorical_cols = [
    "sex", "cp", "fbs", "restecg", "exang",
    "slope", "ca", "thal", "smoking", "diabetes", "heart_disease"
]

if categorical_cols:
    selected_col = st.selectbox("Choose a column to display as a pie chart:", categorical_cols)
    fig, ax = plt.subplots(figsize=(4,4))
    data[selected_col].value_counts().plot.pie(
        autopct='%1.1f%%',
        startangle=90,
        ax=ax,
        wedgeprops={'edgecolor': 'white'}
    )
    ax.set_ylabel("")
    ax.set_title(f"Distribution of {selected_col}")
    st.pyplot(fig)
else:
    st.info("No suitable categorical columns found for pie charts.")
