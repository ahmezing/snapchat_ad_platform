import requests
import sys
import json
import os
import logging
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


load_dotenv()
logging.basicConfig(level=logging.INFO)

class SnapchatAPI:
    def __init__(self, client_id, client_secret, access_token=None, refresh_token=None):
        self.base_url = "https://adsapi.snapchat.com"
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.access_token = access_token

    def authenticate(self):
        url = f"{self.base_url}/v1/oauth2/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            self.access_token = response.json()['access_token']
            logging.info("Successfully authenticated.")
        else:
            raise Exception(f"Failed to authenticate: {response.text}")

    def push_user_data(self, segment_id, user_data):
        if not self.access_token:
            self.authenticate()  # re-authenticate if token is missing

        url = f"{self.base_url}/v1/segments/{segment_id}/users"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=user_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to push user data: {response.text}")

    def read_user_data(self, file_path):
        with open(file_path, 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    refresh_token = os.getenv('REFRESH_TOKEN')
    access_token = os.getenv('ACCESS_TOKEN')
    api = SnapchatAPI(client_id, client_secret, access_token, refresh_token)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    users_data_path = os.path.join(current_dir, '..', 'data', 'users_data.json')
    user_data = api.read_user_data(users_data_path)
    print(api.push_user_data(os.getenv('TEST_SEGMENT_ID'), user_data))
