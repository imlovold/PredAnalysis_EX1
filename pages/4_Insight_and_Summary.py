import streamlit as st
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

FILE_PATH = "heart_disease_dataset.csv"

st.title("Insights & Summaries")

if not os.path.exists(FILE_PATH):
    st.error(f"File '{FILE_PATH}' not found.")
else:
    df = pd.read_csv(FILE_PATH)

    # Smart numeric summary
    st.subheader("Numeric Insights")

    numeric_cols = ["age", "trestbps", "chol", "thalach", "oldpeak", "bmi"]
    summary_list = []

    for col in numeric_cols:
        desc = df[col].describe()
        skew = df[col].skew()
        iqr = desc["75%"] - desc["25%"]
        outliers = ((df[col] < (desc["25%"] - 1.5 * iqr)) | (df[col] > (desc["75%"] + 1.5 * iqr))).sum()
        
        summary_list.append({
            "Variable": col,
            "Mean": round(desc["mean"], 2),
            "Std Dev": round(desc["std"], 2),
            "Min": round(desc["min"], 2),
            "25%": round(desc["25%"], 2),
            "Median": round(desc["50%"], 2),
            "75%": round(desc["75%"], 2),
            "Max": round(desc["max"], 2),
            "Skewness": round(skew, 2),
            "Outliers (IQR method)": outliers
        })

    st.dataframe(pd.DataFrame(summary_list))

    findings = []

    if df["chol"].max() > 600:
        findings.append("⚠️ Extremely high cholesterol values detected (>600 mg/dL) – possible errors.")
    if df["trestbps"].max() > 220:
        findings.append("⚠️ Blood pressure values above 220 mmHg detected – review needed.")
    if df["bmi"].mean() > 35:
        findings.append("ℹ️ Average BMI suggests many individuals may be overweight/obese.")
    if df["thalach"].min() < 60:
        findings.append("⚠️ Some very low max heart rate values detected (<60 bpm).")

    if findings != []:
        # Findings
        st.subheader("Automated Findings")

        for f in findings:
            st.write(f)


    def categorical_insights(df, target_col="heart_disease"):
        st.subheader("Categorical Insights")

        # Select categorical columns (small cardinality only)
        cat_cols = df.select_dtypes(include=['object', 'category', 'int64']).columns.tolist()
        cat_cols = [c for c in cat_cols if df[c].nunique() <= 15 and c != target_col]

        if not cat_cols:
            st.info("No categorical variables suitable for insight analysis.")
            return

        # Prepare overview table
        overview = []
        for col in cat_cols:
            counts = df[col].value_counts(dropna=False)
            n_categories = df[col].nunique()
            
            # Smart flag: top category dominates relative to second-largest
            if len(counts) > 1:
                dominance_ratio = counts.iloc[0] / counts.iloc[1]
            else:
                dominance_ratio = 1
            flag = "⚠️ Dominant Category" if dominance_ratio > 3 else ""

            top_prop = counts.iloc[0] / counts.sum()
            overview.append({
                "Variable": col,
                "# Categories": n_categories,
                "Top Category %": f"{top_prop:.1%}",
                "Flag": flag
            })

        overview_df = pd.DataFrame(overview)
        st.dataframe(overview_df)

        # Select variable to visualize
        selected_col = st.selectbox("Choose a variable to display visualizations:", cat_cols)

        # Show visualizations
        counts = df[selected_col].value_counts(dropna=False)
        fig, axes = plt.subplots(1, 2, figsize=(8, 3))

        # Left: counts
        counts.plot(kind='bar', ax=axes[0], color="skyblue", edgecolor="black")
        axes[0].set_ylabel("Count")
        axes[0].set_title("Counts")

        # Right: % by heart_disease
        if target_col in df.columns:
            ctab = pd.crosstab(df[selected_col], df[target_col], normalize="index") * 100
            ctab.plot(kind="bar", stacked=True, ax=axes[1], colormap="coolwarm", edgecolor="black")
            axes[1].set_ylabel("% within category")
            axes[1].set_title(f"{selected_col} vs {target_col}")
        else:
            axes[1].axis("off")

        st.pyplot(fig)
    
    categorical_insights(df, target_col="heart_disease")

