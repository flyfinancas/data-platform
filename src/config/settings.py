from datetime import datetime

data = datetime.now()
dia = data.day
mesAtual = data.month
mesPassado = data.month -1
ano = data.year
data

token = "Z0EjZPzTOb9-qbVJTaLC_8MBDwlIfyVkPb1Jkg4gO0c5uT1yGYKdbhymdooxURAnynsbTrCaUm2kwDer_ognz4-fzjXjZpgL91gl4_Hpqqeo_erG4K7M9uXrh2Pn7T4LAp3szAxHWrCxbXqRAWFz3g.."
urlClientes = "https://apinewintegracao.bomcontrole.com.br/integracao/Cliente/Pesquisar"
urlFinanceiroPesquisar = f"https://apinewintegracao.bomcontrole.com.br/integracao/Financeiro/Pesquisar?dataInicio={ano}-{mesPassado:02d}-01 00:00:00&dataTermino={ano}-{mesAtual:02d}-{dia:02d} 00:00:00&tipoData=DataConciliacao"

# API Configuration
BASE_URL = "https://apinewintegracao.bomcontrole.com.br/integracao"
ENDPOINTS = {
    "clients": f"{BASE_URL}/Cliente/Pesquisar",
    "financial": f"{BASE_URL}/Financeiro/Pesquisar"
}

def get_financial_url():
    data = datetime.now()
    dia = data.day
    mesAtual = data.month
    mesPassado = data.month - 1
    ano = data.year
    
    return f"{ENDPOINTS['financial']}?dataInicio={ano}-{mesPassado:02d}-01 00:00:00&dataTermino={ano}-{mesAtual:02d}-{dia:02d} 00:00:00&tipoData=DataConciliacao"

# Email Configuration
EMAIL_CONFIG = {
    "smtp_server": "smtp.hostinger.com",  # Change this according to your email provider
    "smtp_port": 465,
    "sender_email": "dataplatform@flyfinancas.com.br",  # Replace with your email
    "password": "Caradotisim@123"  # Replace with your email password or app-specific password
}

if __name__ == "__main__":
    print(f"{mesAtual:02d}")