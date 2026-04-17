import streamlit as st
import pandas as pd

st.title("Cutoff Analysis")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    required_cols = ['College', 'Branch', 'Category', 'Year', 'Cutoff']

    if not all(col in df.columns for col in required_cols):
        st.error("Invalid CSV format")
    else:
        pivot_df = df.pivot_table(
            index=['College', 'Branch', 'Category'],
            columns='Year',
            values='Cutoff'
        ).reset_index()

        st.success("File processed successfully")
        st.dataframe(pivot_df)
    
