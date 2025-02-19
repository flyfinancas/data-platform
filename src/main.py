import requests
import json
from config.settings import token, url

headers = {"Authorization": f"ApiKey z{token}"}

class APIExtractor:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")

if __name__ == "__main__":
    extractor = APIExtractor(url, headers)
    print(extractor.get_data())