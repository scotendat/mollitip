import requests

# Making an HTTP GET request to a hypothetical URL
response = requests.get('https://api.example.com/data')

# Printing the response text
print("Snowball #1: ", response.text)
