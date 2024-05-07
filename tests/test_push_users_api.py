import sys
import os
import logging
from dotenv import load_dotenv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.snapchat_api import SnapchatAPI

load_dotenv()
logging.basicConfig(level=logging.INFO)

def test_api():
    # Setting up the directory path and loading environment variables
    current_dir = os.path.dirname(os.path.realpath(__file__))
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    refresh_token = os.getenv('REFRESH_TOKEN')
    access_token = os.getenv('ACCESS_TOKEN')

    # Initialize the SnapchatAPI with environment configurations
    api = SnapchatAPI(client_id, client_secret, refresh_token=refresh_token, access_token=access_token)
    
    # Load user data from the JSON file
    users_data_path = os.path.join(current_dir, '..', 'data', 'users_data.json')
    user_data = api.read_user_data(users_data_path)
    
    # Get segment ID and attempt to push user data
    segment_id = os.getenv('TEST_SEGMENT_ID')
    logging.info(f"Segment ID being used: {segment_id}")
    response = api.push_user_data(segment_id, user_data)
    logging.info(f"Response from server: {response}")

if __name__ == "__main__":
    test_api()
