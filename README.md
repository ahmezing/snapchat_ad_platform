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

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`



3. **Install Required Packages**
Install all required packages that are used in the project:

pip install flask requests python-dotenv



### Configuration


### Configuration

1. **Environment Variables**
   Set up the necessary environment variables by creating a `.env` file in the root directory of your project. Populate it with the following entries:

   ```plaintext
   CLIENT_ID=your_client_id # Available in .env.example
   CLIENT_SECRET=your_client_secret # Available in .env.example
   REDIRECT_URI=https://127.0.0.1:8000/callback
   REFRESH_TOKEN=your_refresh_token # Obtain this from setting up the app
   ACCESS_TOKEN=your_access_token # Obtain this after authentication
   TEST_SEGMENT_ID=your_test_segment_id # Available in .env.example




2. **SSL Certificates**
Ensure you have `cert.pem` and `key.pem` in the `flask_app` directory to support HTTPS.


### Running the Application


1. **Start the Flask Server**
Start the server by running the following command:

python flask_app/app.py


2. **Generate Authentication URL**
To authenticate with Snapchat and obtain your tokens, run the following script to generate an authorization URL:

python generate_auth_url.py

than add the tokens to the .env file


### Using the API
The module `modules/snapchat_api.py` includes the `SnapchatAPI` class that provides methods to authenticate, push user data to segments, and read user data from files.


### Running Tests
Execute the following command to run tests and ensure the API functions as expected:

python tests/test_snapchat_api.py


## Development Notes
- The application uses Flask to manage web requests and handle OAuth callbacks.
- Data management is handled through the `SnapchatAPI` class.