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


if __name__ == "__main__":
    print(f"{mesAtual:02d}")