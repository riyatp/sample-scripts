import base64
import requests

# Read the contents of the text file into a variable
with open('myfile.txt', 'rb') as file:
    file_contents = file.read()

# Encode the file contents as base64
encoded_contents = base64.b64encode(file_contents).decode('utf-8')

# Set up the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Set up the data for the API request
data = {
    'name': 'My Data Service',
    'revisionComment': 'Initial revision',
    'fileContent': encoded_contents
}

# Send the API request to create a new revision
response = requests.post('https://my.denodo.server/api/solution-manager/v2/data-services', headers=headers, json=data)

# Print the response from the API
print(response.json())
