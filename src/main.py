from config.settings import *
from factory.extractor import APIExtractor
from factory.transform import *

headers = {"Authorization": f"ApiKey {token}"}

df = APIExtractor(urlClientes, headers).get_data()
clientes = Trasformer.df_reader(df, schemaCliente)

print(clientes)
