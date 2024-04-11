import streamlit as st
from PIL import Image
import requests
import io

def call_api(uploaded_file):
    api_endpoint = "http://localhost:8000/run_model"
    files = {"file": uploaded_file}
    try:
        response = requests.post(api_endpoint, files=files)
        if response.status_code == 200:
            
    except Exception as e:
        print(f"ERROR OCCURED while sending request {e}")