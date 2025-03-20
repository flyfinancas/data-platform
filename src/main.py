from config.settings import token, url
from extract.extractor import APIExtractor

headers = {"Authorization": f"ApiKey {token}"}

extractor = APIExtractor(url, headers)
print(extractor.get_data())