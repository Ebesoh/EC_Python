#api_call.py
import requests

def fetch_data():
    r = requests.get("https://api.example.com/data")
    return r.json()
