from config.settings import token, urlClientes, EMAIL_CONFIG
from factory.extractor import APIExtractor
from factory.transform import Transformer
from factory.emailer import Emailer

headers = {"Authorization": f"ApiKey {token}"}

# Get clients data
clientes = APIExtractor(urlClientes,headers)
df_clientes = clientes.get_data()


if __name__ == "__main__":
    from tests.data import dados
    import pandas as pd
    df = pd.DataFrame(dados)

    # Separando entradas e saídas
    entradas = df[df['Valor'] > 0]['Valor'].sum()
    saidas = df[df['Valor'] < 0]['Valor'].sum()
    diferenca = entradas + saidas

    tabela_html = df.to_html(index=False, justify="center", border=1, classes='tabela-financeira')



    # Create email sender
    emailer = Emailer(
        EMAIL_CONFIG["smtp_server"],
        EMAIL_CONFIG["smtp_port"],
        EMAIL_CONFIG["sender_email"],
        EMAIL_CONFIG["password"]
    )

    # Example of sending an email
    recipient = "rodolfogdemelo@gmail.com, jessica@flyfinancas.com.br, karilin@flyfinancas.com.br"
    subject = "FLY-FINANCAS: Relatorio Diario"
    body = f"""
    <h2>Relatório Financeiro Diário</h2>
    <p>Segue abaixo os lançamentos financeiros do dia:</p>
    {tabela_html}
    <br>
    <h3>Resumo do Dia</h3>
    <ul>
        <li><strong>Total de Entradas:</strong> R$ {entradas:.2f}</li>
        <li><strong>Total de Saídas:</strong> R$ {abs(saidas):.2f}</li>
        <li><strong>Diferença:</strong> <span style="color: {'green' if diferenca >= 0 else 'red'};">R$ {diferenca:.2f}</span></li>
    </ul>
    """
    
    emailer.send_email(recipient, subject, body)
    pass
