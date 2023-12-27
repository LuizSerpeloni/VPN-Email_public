import configparser

#####
# Processos do Parser:
# Cria o objeto ConfigParser
config = configparser.ConfigParser()

# Lê o arquivo de configuração
config.read('conf.txt', encoding='utf-8')

### Setor do email:
def config_email():
    # Configurações de destinatário e SMTP
    To_conf = config['Destinatario']['To']
    Subject_conf = config['SMTP_Config']['Subject']
    From_conf = config['SMTP_Config']['From']
    password_conf = config['SMTP_Config']['password']
    SMTP_server_conf = config['SMTP_Config']['SMTP_server']
    Port_conf = config['SMTP_Config']['Port']
    return [To_conf, Subject_conf, From_conf, password_conf, SMTP_server_conf, Port_conf]


### Setor do Excel
def excel_path():
    # Pega o caminho da planilha:
    path = config['Excel_local']['local']
    return path

def delta_dias():
    delta = config['Dias_aviso']['dias']
    return delta

##### Fim do Parser