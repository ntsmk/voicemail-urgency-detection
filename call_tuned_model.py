import requests
from google.auth import default
from google.auth.transport.requests import Request
import os
from dotenv import load_dotenv

load_dotenv()
PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = os.getenv("LOCATION")
ENDPOINT_ID = os.getenv("ENDPOINT_ID")
URL = f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/endpoints/{ENDPOINT_ID}:generateContent"

# Get access token using default credentials (Application Default Credentials)
credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
credentials.refresh(Request())
token = credentials.token

# Build the headers
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Gemini content format
body = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": "The internet is down. Call me back"}
            ]
        }
    ],
}

# Make the POST request
response = requests.post(URL, headers=headers, json=body)

# Show result
print("Status:", response.status_code)
print("Response:\n", response.json())
