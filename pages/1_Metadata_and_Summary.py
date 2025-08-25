import streamlit as st
import pandas as pd
import os

FILE_PATH = "heart_disease_dataset.csv"

st.title("📄 Metadata, Information & Summary")

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

    st.subheader("Column Information")
    info_df = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.astype(str),
        'Missing Values': df.isna().sum(),
        'Unique Values': df.nunique()
    })
    st.dataframe(info_df)

    st.subheader("Numeric Summary")
    st.dataframe(df.describe())

    st.subheader("Data Limitations & Considerations")
    st.markdown("""
    - **Missing Values:** Check for NaNs or placeholder values (e.g., -9).
    - **Granularity:** Data is at the individual level; periodicity not represented.
    - **Update Frequency:** Likely static, may not reflect current trends.
    - **Missing Variables:** E.g., medication history, diet, genetics beyond 'famhist'.
    - **Potential Bias:** Some groups may be underrepresented.
    - **Encoding Limitations:** Numeric codes for categorical variables need decoding.
    """)
