from flask import Flask, request, jsonify
import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

@app.route('/callback')
def callback():
    # Retrieve the 'code' from the query parameters
    code = request.args.get('code')
    if code:
        try:
            # Exchange the authorization code for access tokens
            access_token, refresh_token = exchange_code_for_token(code)
            return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
        except Exception as e:
            logging.error(f"Token exchange failed: {e}")
            return str(e), 500
    return 'Authorization code not found', 400

def exchange_code_for_token(code):
    # Define the URL for the token exchange endpoint
    url = "https://accounts.snapchat.com/login/oauth2/access_token"
    # Prepare the data payload for the POST request
    data = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': os.getenv('REDIRECT_URI')
    }
    # Make the POST request to exchange the code for tokens
    response = requests.post(url, data=data)
    if response.status_code == 200:
        tokens = response.json()
        return tokens['access_token'], tokens['refresh_token']
    else:
        raise Exception(f"Failed to retrieve tokens: {response.text}")

if __name__ == '__main__':
    # Run the app with SSL context for HTTPS and debug enabled
    app.run(debug=True, port=8000, ssl_context=('cert.pem', 'key.pem'))
