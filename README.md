# Snapchat Ad Project

This application interfaces with Snapchat's advertising platform to manage custom segments and user data. It provides functionality to authenticate with Snapchat, exchange authorization codes for tokens, and push user data to specific segments.

## Getting Started

### Prerequisites

Before you start, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)



### Installation


1. **Clone the Repository**
   Clone the repository using the following command:
   ```bash
   git clone https://github.com/ahmezing/snapchat_ad_platform.git
   cd snapchat_ad_project
2. **Set Up a Virtual Environment**
Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install Required Packages**
Install all required packages that are used in the project:

   ```bash
   pip install flask requests python-dotenv

### Configuration

1. **Environment Variables**
   Set up the necessary environment variables by creating a `.env` file in the root directory of your project. Populate it with the following entries (can also be found in `.env.example`):

   ```plaintext
   CLIENT_ID=your_client_id # paste your own
   CLIENT_SECRET=your_client_secret # paste your own
   REDIRECT_URI=https://127.0.0.1:8000/callback # or paste your own if you have one setup
   REFRESH_TOKEN=your_refresh_token # Obtain this from setting up the app
   ACCESS_TOKEN=your_access_token # Obtain this after authentication
   AD_ACCOUNT_ID=your_ad_account_id # paste your own
   TEST_SEGMENT_ID=your_test_segment_id # Obtain this from the api, or you can use an existing one
2. **OAuth App Setup**
   
If you already have a Snapchat OAuth application:

    Replace the CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI values in your .env file with those from your existing app.
    You can skip starting the Flask server in the next section because your existing app already handles the redirect URL.

If you need to set up a new Snapchat OAuth application:

    Register a new app on the Snapchat developer platform and use the redirect URL provided in .env.example.
    Make sure to copy your CLIENT_ID, CLIENT_SECRET, and REDIRECT_URI to the .env file.

3. **SSL Certificates**
Ensure you have `cert.pem` and `key.pem` in the `flask_app` directory to support HTTPS.


### Running the Application


1. **Start the Flask Server**
Start the server by running the following command:
   ```bash
   python flask_app/app.py
2. **Generate Authentication URL**
To authenticate with Snapchat and obtain your tokens, run the following script to generate an authorization URL:

   ```bash
   python generate_auth_url.py 

then add the tokens to the `.env` file

3. **Follow the URL Generated in Step 3, then authorize the app**
it shall then exchange the code with access token and refresh token, and redirects you to the local Redirect URI specified, where you will be able to access the tokens 

4. **Paste The Shown Tokens to The `.env` File for Them To Be Utilized**

5. **Create a Custom Segment**
Run the following command to create a new custom segment and note down the new segment ID that will appear in the terminal:

   ```bash
   python tests/test_add_segment_api.py
6. **Add the Segment ID to the `.env` file**
Add the newly created segment's ID to the `.env` file under TEST_SEGMENT_ID.

7. **Test Adding The Randomly Generated Users to the Specified Segment**
Run the following command to test the API that is dedicated to add users to a segement:

   ```bash
   python tests/test_push_users_api.py

### Using the API
The module `modules/snapchat_api.py` includes the `SnapchatAPI` class that provides methods to authenticate, create segments, push user data to segments, and read user data from files.
  

## Development Notes
- The application uses Flask to manage web requests and handle OAuth callbacks.
- Data management is handled through the `SnapchatAPI` class.
- Flask Server: Starting the server is only necessary if the redirect URL is required.
- `modules/snapchat_api.py` can be easily extended to have more functionalities with `SnapchatAPI`
- `modules/generate_data.py` can be extended to have different generation patterns based on the required parameters for users
