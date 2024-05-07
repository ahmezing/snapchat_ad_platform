import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.snapchat_api import SnapchatAPI

def test_add_segment():
    """
    Test creating a new custom segment via the Snapchat API.
    """
    # Load environment variables
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    refresh_token = os.getenv('REFRESH_TOKEN')
    access_token = os.getenv('ACCESS_TOKEN')
    ad_account_id = os.getenv('AD_ACCOUNT_ID')

    # Initialize the Snapchat API class
    api = SnapchatAPI(client_id, client_secret, access_token, refresh_token)

    # Define the new segment name and description
    segment_name = "New Test Segment"
    segment_description = "A segment created for testing purposes"

    try:
        # Create a new segment and store its ID
        new_segment_id = api.create_segment(segment_name, segment_description, ad_account_id)
        print(f"New Segment ID: {new_segment_id}")

    except Exception as e:
        print(f"Error creating new segment: {e}")

if __name__ == "__main__":
    test_add_segment()
