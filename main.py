# Versão 1.4

import envia_email
import verifica_vencidos

# Executa o módulo 'verifica_vencidos' e torna as variáveis 'vencidos' e 'tabela_html' como variáveis locais
verifica_vencidos.verifica()
vencidos, tabela_html = verifica_vencidos.verifica()

# Decide se será enviado o email, ou não
if vencidos.empty:
    exit()
else:
    envia_email.enviar()