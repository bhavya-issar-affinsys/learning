import requests
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return "Hello World"
@app.get("/fish/{species}")
def read_fish (species: str):
    r = requests.get(f"https://www.fishwatch.gov/api/species/{species}")
    return r.json()