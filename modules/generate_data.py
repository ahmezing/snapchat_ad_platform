import os
from faker import Faker
import json

def generate_user_data(num_users):
    fake = Faker()
    users = []
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "phone": fake.phone_number()
        }
        users.append(user)
    return users

def save_data_to_file(file_path, data):
    # Ensure the directory exists before writing
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'users_data.txt')
    users = generate_user_data(10)  # Generate data for 10 users
    save_data_to_file(data_dir, users)
