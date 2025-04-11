from fastapi import FastAPI
from main import extract_competitors

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Competitor Analyzer API Running!"}

@app.get("/analyze")
def analyze():
    return extract_competitors()
