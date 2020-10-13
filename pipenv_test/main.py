import requests

response = requests.get("https://httpbin.org/ip")

print(f"Your IP address is {response.json()['origin']}.")
