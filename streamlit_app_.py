import streamlit as st

st.set_page_config(page_title="Heart Disease Data Explorer", layout="wide")

st.title("🫀 Heart Disease Data Explorer")
st.markdown("""
Welcome to the interactive explorer for the **Heart Disease Dataset**.  
Use the sidebar to navigate between pages:
- **Metadata & Summary**: View dataset metadata, preview, and summary statistics.
- **Categorical Distributions**: Explore categorical features as bar charts.
- **Correlation Heatmap**: Inspect correlations between numeric columns.
- **Pie Charts**: Visualize categorical distributions as pie charts.
""")
