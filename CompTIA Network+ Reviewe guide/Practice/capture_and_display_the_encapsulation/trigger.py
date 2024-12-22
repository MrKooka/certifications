import requests

response = requests.get("http://example.com")
print(response.status_code)
print(response.text[:200])  # Print first 200 chars
