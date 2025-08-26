import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_PATH = "heart_disease_dataset.csv"

# Column descriptions dictionary
COLUMN_DESCRIPTIONS = {
    "sex": "Biological sex (0 = female, 1 = male).",
    "cp": "Chest pain type (0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic).",
    "fbs": "Fasting blood sugar >120 mg/dL (0 = false, 1 = true).",
    "restecg": "Resting electrocardiogram results (encoded).",
    "exang": "Exercise-induced angina (0 = no, 1 = yes).",
    "slope": "Slope of the peak exercise ST segment (encoded).",
    "ca": "Number of major vessels (0–3) colored by fluoroscopy.",
    "thal": "Thalassemia status (3 = normal, 6 = fixed defect, 7 = reversible defect).",
    "smoking": "Current smoking status (0 = no, 1 = yes).",
    "diabetes": "Diabetes status (0 = no, 1 = yes).",
    "heart_disease": "Target variable: Presence of heart disease (0 = no, 1 = yes)."
}

st.title("Categorical Variable Explorer")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)

    # Only categorical variables (int/object) with reasonable unique values
    categorical_cols = [c for c in df.columns if df[c].dtype in ["int64", "object"] and df[c].nunique() <= 15]

    if not categorical_cols:
        st.warning("No categorical variables found in this dataset.")
    else:
        selected_col = st.selectbox("Choose a categorical variable:", categorical_cols)

        # Show description if available
        st.markdown(f"**Description:** {COLUMN_DESCRIPTIONS.get(selected_col, 'No description available.')}")

        unique_vals = df[selected_col].nunique()

        if unique_vals <= 2:
            # Binary categorical → Pie chart
            st.subheader(f"Pie Chart of {selected_col}")
            fig, ax = plt.subplots(figsize=(4,4))
            df[selected_col].value_counts().plot.pie(
                autopct='%1.1f%%', startangle=90, ax=ax, wedgeprops={'edgecolor':'white'}
            )
            ax.set_ylabel("")
            st.pyplot(fig)
        else:
            # Multi-category → Bar chart
            st.subheader(f"Bar Chart of {selected_col}")
            fig, ax = plt.subplots(figsize=(5,4))
            df[selected_col].value_counts().plot(kind="bar", ax=ax, color="skyblue")
            ax.set_ylabel("Count")
            st.pyplot(fig)
else:
    st.error(f"File '{FILE_PATH}' not found.")
