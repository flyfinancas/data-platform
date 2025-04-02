from config.settings import token, urlClientes
from factory.extractor import APIExtractor
from factory.transform import Transformer

headers = {"Authorization": f"ApiKey {token}"}

# Get clients data
clientes = APIExtractor(urlClientes,headers)
df_clientes = clientes.get_data()


if __name__ == "__main__":
    # main()
    print(df_clientes)
    pass
