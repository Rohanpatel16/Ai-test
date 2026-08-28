import os
import requests

# CONFIGURATION
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN")
REPO_OWNER = "YOUR_GITHUB_USERNAME"
REPO_NAME = "YOUR_REPO_NAME"

# Optional: Set a webhook URL from https://webhook.site to receive the reply asynchronously
CALLBACK_WEBHOOK = "https://webhook.site/YOUR-UUID-HERE"

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/dispatches"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
}

payload = {
    "event_type": "gemma-query",
    "client_payload": {
        "prompt": "Give 3 short tips for clean code.",
        "model": "gemma4:e2b",
        "callback_url": CALLBACK_WEBHOOK
    }
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 204:
    print(" Action triggered successfully!")
    print("1. View live progress on GitHub Actions tab.")
    print(f"2. Response will be posted to {CALLBACK_WEBHOOK}")
else:
    print(f"❌ Failed: {response.status_code}")
    print(response.text)
