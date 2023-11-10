# Versão 1.3

import pandas as pd
from datetime import datetime
import email.message
import smtplib
import configparser

#####
# Processos do Parser:
# Cria o objeto ConfigParser
config = configparser.ConfigParser()

# Lê o arquivo de configuração e o coloca na variável config
config.read('conf.txt', encoding='utf-8')

# Pega o caminho da planilha:
path = config['Excel_local']['local']
#####

# Abre o excel necessário
plan_data = pd.read_excel(path)

# Coleta a variável para verificar a data
now = datetime.now()

#####
# Define a classe enviar_email
def enviar_email():

#   Variáveis do arquivo de configuração
    Subject_conf = config['SMTP_Config']['Subject']
    From_conf = config['SMTP_Config']['From']
    password_conf = config['SMTP_Config']['password']
    SMTP_server_conf = config['SMTP_Config']['SMTP_server']
    Port_conf = config['SMTP_Config']['Port']
    protocol_conf = config['SMTP_Config']['protocol']
    to_conf = config['Destinatario']['to']

    corpo_email = f"""
    <p>Bom dia!</p>
    <p> </p>
    <p>Aviso: Os seguintes certificados estão vencidos, ou vencem hoje:</p>
    <p></p>
    <p>{tabela_html}</p>
    <p></p>
    <p>Para mais informações, consulte o arquivo "Planilha Datas VPN.xlsx"</p>
    <p></p>
    <p></p>
    <p>Obrigado!</p>
    """

    # Dados como Para, Com cópia, Assunto e senha do email
    msg = email.message.Message()
    msg['Subject'] = Subject_conf
    msg['From'] = From_conf
    msg['To'] = to_conf
    password = password_conf
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    # Dados do servidor SMTP
    s = smtplib.SMTP(SMTP_server_conf, int(Port_conf))
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
# Fim da classe enviar_email
#####

# Configura a estrutura do dataframe
columns = ['Colaborador', 'Data Expiração']
# Verifica se há datas vencidas e coloca em no dataframe vencidos:
vencidos = plan_data[columns].where(plan_data['Data Expiração'] <= now)
# Remove as linhas vazias
vencidos = vencidos.dropna()

# Se o dataframe "vencidos" estiver fazio, finaliza o programa
# Se contiver dados, inicia a rotina de envio de email
if vencidos.empty:
    exit()
else:
    tabela_html = vencidos.to_html(classes='table table-striped', index=False)
    enviar_email()