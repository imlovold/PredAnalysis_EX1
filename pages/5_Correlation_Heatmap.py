# pages/5_Correlation_Heatmap.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

FILE_PATH = "heart_disease_dataset.csv"
st.title("Correlation Heatmap (Numeric + Categorical)")

df = pd.read_csv(FILE_PATH)

# Function to compute Cramér's V for categorical variables
def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    return np.sqrt(phi2 / (min(k-1, r-1) + 1e-8))

# Identify columns
cat_cols = df.select_dtypes(include=['object', 'category', 'int64']).columns.tolist()
num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
cat_cols = [c for c in cat_cols if c not in num_cols]

# Compute correlations
cols_for_corr = cat_cols + num_cols
corr_dict = {}

st.write(f"Computing correlation matrix for {len(cols_for_corr)} columns...")

for col1 in cols_for_corr:
    corr_dict[col1] = {}
    for col2 in cols_for_corr:
        if col1 == col2:
            corr_dict[col1][col2] = 1.0
        elif col1 in cat_cols and col2 in cat_cols:
            corr_dict[col1][col2] = cramers_v(df[col1], df[col2])
        elif col1 in num_cols and col2 in num_cols:
            corr_dict[col1][col2] = df[col1].corr(df[col2])
        else:
            if col1 in num_cols:
                numeric = df[col1]
                categorical = pd.get_dummies(df[col2], drop_first=False)
            else:
                numeric = df[col2]
                categorical = pd.get_dummies(df[col1], drop_first=False)
            corr_dict[col1][col2] = categorical.apply(lambda x: numeric.corr(x)).abs().max()

# Convert to DataFrame
corr_df = pd.DataFrame(corr_dict)

# Heatmap
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Flag strong correlations
threshold = st.slider("Highlight correlations above", min_value=0.0, max_value=1.0, value=0.3, step=0.05)

strong_corrs = []
for col1 in corr_df.columns:
    for col2 in corr_df.columns:
        if col1 != col2 and corr_df.loc[col1, col2] >= threshold:
            strong_corrs.append((col1, col2, corr_df.loc[col1, col2]))

if strong_corrs:
    strong_df = pd.DataFrame(strong_corrs, columns=["Variable 1", "Variable 2", "Correlation"])
    strong_df = strong_df.sort_values(by="Correlation", ascending=False)
    st.dataframe(strong_df)
else:
    st.info("No correlations exceed the threshold.")
