import requests
import json
import pprint

url = "https://apinewintegracao.bomcontrole.com.br/integracao/Cliente/Pesquisar"

headers = {"Authorization": "ApiKey Z0EjZPzTOb9-qbVJTaLC_8MBDwlIfyVkPb1Jkg4gO0c5uT1yGYKdbhymdooxURAnynsbTrCaUm2kwDer_ognz4-fzjXjZpgL91gl4_Hpqqeo_erG4K7M9uXrh2Pn7T4LAp3szAxHWrCxbXqRAWFz3g.."}

response = requests.get(url, headers=headers)

pprint.pprint(response.json())
