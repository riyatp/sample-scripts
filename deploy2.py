import base64
import requests
import json

# Set the URL of the Solution Manager API
api_url = "http://<denodo_server>/solution-manager/v2"

# Set the username and password for authentication
username = "your_username"
password = "your_password"

# Set the path to the revision file to upload
revision_file_path = "/path/to/revision_file.xml"

# Open the revision file and read its contents
with open(revision_file_path, "rb") as f:
    revision_file_contents = f.read()

# Encode the revision file contents as base64
encoded_revision_file = base64.b64encode(revision_file_contents).decode("utf-8")

# Set the name and comment for the revision
revision_name = "My Revision"
revision_comment = "This is my revision."

# Create the request data as a dictionary
request_data = {
    "name": revision_name,
    "revisionComment": revision_comment,
    "fileContent": encoded_revision_file
}

# Convert the request data to JSON
request_data_json = json.dumps(request_data)

# Set up the API request headers
headers = {
    "Content-Type": "application/json"
}

# Set up the authentication credentials
auth = requests.auth.HTTPBasicAuth(username, password)

# Send the API request to create the revision
response = requests.post(api_url + "/revisions", headers=headers, auth=auth, data=request_data_json)

# Get the revision ID from the response
revision_id = response.json()["id"]

# Set up the API request to deploy the revision
deploy_request_data = {
    "revisionId": revision_id
}

# Convert the deploy request data to JSON
deploy_request_data_json = json.dumps(deploy_request_data)

# Send the API request to deploy the revision
response = requests.post(api_url + "/deployments", headers=headers, auth=auth, data=deploy_request_data_json)

# Print the response from the API
print(response.json())


import socket
import configparser

# Get the hostname of the machine
hostname = socket.gethostname()

# Read the config file based on the hostname
config = configparser.ConfigParser()
config.read(f"{hostname}.ini")

# Access config values by section and option name
option_value = config.get("section_name", "option_name")

