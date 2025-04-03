import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()
    for post in posts[:5]:
        print(f"{post['title']}\n{post['body']}\n")
else:
    print("Failed to fetch data.")

#some APIs support filters via parameters:
params = {'useId': 1}
response = requests.get(url, params=params)
print(response.json())

#APIs that require keys
headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Accept': 'application/json'
}

response = requests.get('https://api.example.com/data', headers=headers)

#handle errors gracefully
try:
    response = requests.get(url, timeout=5)
    reponse.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")