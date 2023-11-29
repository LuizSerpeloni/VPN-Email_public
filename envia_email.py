import email.message
import smtplib
#import configparser

import configs
import verifica_vencidos
import configs

def enviar():
    ###### Começo da classe enviar
    #####
    '''# Processos do Parser:
    # Cria o objeto ConfigParser
    config = configparser.ConfigParser()

    # Leia o arquivo de configuração
    config.read('conf.txt', encoding='utf-8')'''

    configs.config_email()
    To_conf, Subject_conf, From_conf, password_conf, SMTP_server_conf, Port_conf = configs.config_email()
    ##### Fim do Parser




    # Lê o texto de envio
    with open('Texto_template.txt', 'r') as arquivo:
        texto = arquivo.read()

    # Abre a varável que vai para o texto
    vencidos, tabela_html = verifica_vencidos.verifica()

    #   Variáveis do arquivo de configuração
    '''SMTP_server_conf = config['SMTP_Config']['SMTP_server']
    Port_conf = config['SMTP_Config']['Port']'''

    corpo_email = f"""
        <p> </p>
        <p>{texto}</p>
        <p></p>
        <p></p>
        <p>{tabela_html}</p>
        <p></p>
        """

    # Dados como Para, Com cópia, Assunto e senha do email
    msg = email.message.Message()
    msg['From'] = From_conf
    msg['To'] = To_conf
    msg['Subject'] = Subject_conf
    password = password_conf
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)


    # Dados do servidor SMTP/Inicie a conexão com o servidor SMTP
    s = smtplib.SMTP(SMTP_server_conf, int(Port_conf))
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    # Encerre a conexão com o servidor SMTP
    #server.quit()

    # Fim da classe enviar
    #####