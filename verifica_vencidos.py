import pandas as pd
from datetime import datetime
import configs

def verifica():
    #####
    # Pega o caminho da planilha:
    configs.excel_path()
    path = configs.excel_path()
    #####

    # Abre o excel necessário
    plan_data = pd.read_excel(path)

    # Coleta as variáveis para verificar a data
    now = datetime.now()

    ####

    # Verifica se há datas vencidas, se houver, coloca na tabela e formata em html, e retorna as variáveis 'vencidos' e 'tabela_html'
    columns = ['Colaborador', 'Data Expiração']
    vencidos = plan_data[columns].where(plan_data['Data Expiração'] <= now)
    vencidos = vencidos.dropna()
    tabela_html = vencidos.to_html(classes='table table-striped', index=False)
    return[vencidos, tabela_html]
