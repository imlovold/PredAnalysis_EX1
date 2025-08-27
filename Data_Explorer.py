import streamlit as st

st.set_page_config(page_title="Heart Disease Data Explorer", layout="wide")

st.title(" Heart Disease Data Explorer")

st.markdown("""
    - Predict the likelihood of heart disease for preventive healthcare
    - Response variable: Diagnosis of heart disease (Yes/No)
    - Observation variables: Both categorical and numerical
    - The dataset is built from medical records and personal information about more than 3000 patients.
    - A predictive model could support doctors in early diagnosis, by flagging high-risk patients for further medical testing.
    - Can update the dataset in the future by adding new patients.
    - Let the model predict first and then give feedback on real outcome.
    """)
