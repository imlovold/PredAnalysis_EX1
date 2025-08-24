import streamlit as st
import os
import pandas as pd
import json

# Path to your folder
FOLDER_PATH = "heart_disease"

st.set_page_config(page_title="Heart Disease Data Explorer", layout="wide")
st.title("📂 Heart Disease Data Explorer")

# Check if folder exists
if not os.path.exists(FOLDER_PATH):
    st.error(f"❌ Folder '{FOLDER_PATH}' not found. Please check the path.")
else:
    files = os.listdir(FOLDER_PATH)

    if not files:
        st.warning("⚠️ No files found in the folder.")
    else:
        for file in files:
            file_path = os.path.join(FOLDER_PATH, file)
            st.subheader(f"📄 {file}")
            st.write(f"Size: {os.path.getsize(file_path)/1024:.2f} KB")

            # Try to preview file content depending on type
            try:
                if file.endswith(".csv"):
                    df = pd.read_csv(file_path)
                    st.dataframe(df.head())
                    st.info(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

                elif file.endswith((".xls", ".xlsx")):
                    df = pd.read_excel(file_path)
                    st.dataframe(df.head())
                    st.info(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

                elif file.endswith(".json"):
                    with open(file_path, "r") as f:
                        data = json.load(f)
                    st.json(data if isinstance(data, dict) else data[:5])

                elif file.endswith(".txt"):
                    with open(file_path, "r") as f:
                        content = f.read(500)
                    st.text(content + ("..." if len(content) == 500 else ""))

                else:
                    st.write("Unsupported file format for preview.")
            except Exception as e:
                st.error(f"Error reading {file}: {e}")
