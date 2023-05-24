import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
from constantes import *

def gerar_codigo_aut():
    return randint(10 ** (QTDE_DIGITOS_CODIGO_AUT - 1),
                   10 ** (QTDE_DIGITOS_CODIGO_AUT) - 1)

def mandar_email(destinatario, corpo_email):
    # Configurações do servidor SMTP e informações de autenticação
    smtp_host = 'gmail.com'
    smtp_port = 587
    smtp_username = 'henrique.cunha@ifpb.edu.br'
    smtp_password = '#Hdnc350#'

    # Criar objeto MIMEMultipart para construir o email
    email = MIMEMultipart()

    # Configurar os campos do email (Remetente, Destinatário, Assunto)
    email['From'] = 'henrique.cunha@ifpb.edu.br'
    email['To'] = destinatario
    email['Subject'] = 'Códido de autenticação para entrar no discord do curso de Engenharia de Computação'

    # Adicionar o conteúdo do email
    email.attach(MIMEText(str(corpo_email), 'plain'))

    # Configurar conexão SMTP e enviar o email
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()  # Iniciar conexão segura
        server.login(smtp_username, smtp_password)  # Fazer login no servidor SMTP
        server.send_message(email)  # Enviar o email

    print(f'Email enviado com sucesso para {destinatario}')


def verificar_email(email):
    # Padrão de expressão regular para verificar o formato do email
    padrao_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Verifica se o email corresponde ao padrão
    if re.match(padrao_email, email):
        return True
    else:
        return False