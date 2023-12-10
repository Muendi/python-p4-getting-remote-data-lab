import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    
    def load_json(self):
        response = requests.get(self.url)
        json_data = response.json()
        return json_data
    
    def get_response_json(self):
        response = requests.get(self.url)
        return response.json()

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)
data = requester.load_json()
print(json.dumps(data, indent=2))
