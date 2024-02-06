import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Get the Notion integration token from environment variables
token = os.getenv('NOTION_TOKEN')

# Notion API endpoint for creating a new record
endpoint = 'https://api.notion.com/v1/pages'

# Database ID where you want to create a new record
database_id = '63eefad1dd0f49f280cfe46bee8858e2'
# Database ID for which you want to retrieve the schema

# Notion API endpoint for retrieving database schema
endpoint = f'https://api.notion.com/v1/databases/{database_id}'

# Headers including the integration token
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13'
}

# Make a GET request to retrieve the database schema
response = requests.get(endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Extract schema information from the response
    schema = response.json()['properties']

    # Display all fields in the schema
    print("Fields in the database schema:")
    for field_name, field_info in schema.items():
        print(f"{field_name}: {field_info['type']}")
else:
    print("Error:", response.text)
