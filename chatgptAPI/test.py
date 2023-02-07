import requests

api_key = "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"
url = "https://api.openai.com/v1/engines/davinci/completions"

response = requests.get(url, headers={
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}, json={
    "prompt": "What is 2+2?",
    "model": "text-davinci-002",
    "max_tokens": 1024
})

print(response.json())