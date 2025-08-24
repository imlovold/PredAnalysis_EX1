import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# File path
FILE_PATH = "heart_disease_dataset.csv"

st.set_page_config(page_title="Heart Disease Data Explorer", layout="wide")
st.title("🫀 Heart Disease Data Explorer")

# Check if file exists
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
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Data info
    st.subheader("Column Information")
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isna().sum(),
        'Unique Values': df.nunique()
    })
    st.dataframe(info_df)

    # Numeric summary
    st.subheader("Numeric Summary")
    st.dataframe(df.describe())

    # Categorical summary
    st.subheader("Categorical Distributions")
    categorical_cols = df.select_dtypes(include=['int64', 'object']).columns.tolist()
    for col in categorical_cols:
        if df[col].nunique() < 20:  # avoid too many bars
            st.write(f"**{col}**")
            fig, ax = plt.subplots()
            df[col].value_counts().plot(kind='bar', ax=ax)
            st.pyplot(fig)

    # Target class balance
    st.subheader("Target: Heart Disease Class Balance")
    if 'heart_disease' in df.columns:
        fig, ax = plt.subplots()
        df['heart_disease'].value_counts().plot(kind='bar', color=['skyblue','salmon'], ax=ax)
        ax.set_xlabel('Heart Disease')
        ax.set_ylabel('Count')
        st.pyplot(fig)

    # Correlation heatmap
    st.subheader("Correlation Heatmap (Numeric Columns)")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    if len(numeric_cols) > 1:
        fig, ax = plt.subplots(figsize=(10,8))
        sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
        st.pyplot(fig)
