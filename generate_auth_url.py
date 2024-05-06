import os
from dotenv import load_dotenv

load_dotenv()

def generate_auth_url():
    """Generate and return the OAuth2 authorization URL for Snapchat."""
    base_url = "https://accounts.snapchat.com/login/oauth2/authorize"
    client_id = os.getenv('CLIENT_ID')
    redirect_uri = os.getenv('REDIRECT_URI')
    scope = "snapchat-marketing-api"
    response_type = "code"

    # Construct the full URL with query parameters
    url = f"{base_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}"
    return url

if __name__ == "__main__":
    print("Navigate to this URL in your web browser to authorize:")
    print(generate_auth_url())
