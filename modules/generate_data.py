import json
import hashlib
from faker import Faker
import os

fake = Faker()

def hash_email(email):
    return hashlib.sha256(email.encode('utf-8')).hexdigest()

def generate_user_data(data_dir, num_users):
    # Initialize the users list with the schema structure
    users = {
        "users": [{
            "schema": ["EMAIL_SHA256"],
            "data": []
        }]
    }
    # Fill the data list with hashed emails
    for _ in range(num_users):
        email = fake.email()
        hashed_email = hash_email(email)
        users["users"][0]["data"].append([hashed_email])

    # Write to file
    data_path = os.path.join(data_dir, 'users_data.json')
    with open(data_path, 'w') as f:
        json.dump(users, f, indent=4)

if __name__ == "__main__":
    data_dir = '../data'  # Ensure this path correctly points to the 'data' directory
    generate_user_data(data_dir, 10)
