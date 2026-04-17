from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI(title="Cutoff Analysis API")

@app.get("/")
def home():
    return {"message": "Cutoff Analysis API is running"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()

    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    required_cols = ['College', 'Branch', 'Category', 'Year', 'Cutoff']

    if not all(col in df.columns for col in required_cols):
        return {"error": "Invalid CSV format"}

    # Pivot (year-wise cutoff)
    pivot_df = df.pivot_table(
        index=['College', 'Branch', 'Category'],
        columns='Year',
        values='Cutoff'
    ).reset_index()

    # Create category-wise data
    result = {}

    categories = pivot_df['Category'].unique()

    for cat in categories:
        result[cat] = pivot_df[pivot_df['Category'] == cat].to_dict(orient="records")

    return {
        "message": "File processed successfully",
        "data": result
    }
