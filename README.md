# VPN-Email_public
## Verifica a tabela excel e envia um email para o endereço indicado ##
###### v.1.3 ######

Este código faz parte de algumas ferramentas que estão sendo criadas, para automação de tarefas diárias do setor
Atualmente, apenas abre a planilha indicada no template **Planilha_template**, verifica se há datas menores ou iguais ao dia (se há datas vencidas), e caso houver, envia um email com a lista do nome e data vencido.
Podendo ser um aviso ao colaborador responsável, ou para a abertura de chamados em plataformas que aceitem esse tipo de solicitação.
Necessário a criação de uma tarefa automática no "Agendador de tarefas" de acordo com a frequência desejada.

### Arquivo conf.txt ###
No arquivo conf, substitua o caminho de exemplo, para o caminho completo, com o nome e extensão do arquivo com as datas da vpn e salve o arquivo.

### Seção SMTP_Config ###
Desitnada a configurções para o envio do email

**Subject:** Assunto do email
**From:** Endereço de email que está enviando
**password** Senha do email que está enviando
**SMTP_server** Servidor de envio (essa infomação estrá disponível no site do seu provedor de email)
**Port** Porta de envio do servidor de email (essa infomação estrá disponível no site do seu provedor de email)
**protocol:** Tipo de protocolo de envio (essa infomação estrá disponível no site do seu provedor de email)

### Seção Destinatario ###
Define o endereço para qula será envido

**to:** Endereço de destino dp email

### Seção Excel_local ###
Define o nome e endereço da planilha que será verificada

**local:**Caminho completo, com o nome e extensão do arquivo


### Ao finalizar a configuração dos dados, salve o arquivo conf.txt ###