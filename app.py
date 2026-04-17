import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cutoff Analysis", layout="wide")

st.title("📊 Cutoff Analysis System")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.write("### 📄 Uploaded Data Preview")
        st.dataframe(df.head())

        required_cols = ['College', 'Branch', 'Category', 'Year', 'Cutoff']

        # Validate columns
        if not all(col in df.columns for col in required_cols):
            st.error("❌ Invalid CSV format. Required columns are missing.")
        else:
            # Pivot table
            pivot_df = df.pivot_table(
                index=['College', 'Branch', 'Category'],
                columns='Year',
                values='Cutoff'
            ).reset_index()

            st.success("✅ File processed successfully!")

            st.write("### 📊 Processed Cutoff Data")
            st.dataframe(pivot_df)

            # Category filter
            st.write("### 🔍 Filter by Category")
            categories = pivot_df['Category'].unique()
            selected_category = st.selectbox("Select Category", categories)

            filtered_df = pivot_df[pivot_df['Category'] == selected_category]
            st.dataframe(filtered_df)

            # Download option
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Filtered Data",
                data=csv,
                file_name="filtered_cutoff.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"Error processing file: {e}")
    


        
               
                
                
                    
                       
                
                
