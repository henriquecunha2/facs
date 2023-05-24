import discord
from discord.ext import commands
from email_utils import verificar_email, mandar_email, gerar_codigo_aut
from constantes import *
from usuario import Usuario

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
codigos = dict()

@bot.event
async def on_ready():
    for guild in bot.guilds:
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                print(f'Nome do canal: {channel.name}, ID do canal: {channel.id}')

@bot.event
async def on_member_join(member):
    guild = member.guild  # Obtém o servidor em que o membro entrou

    canal_id = ID_CANAL_AUT  # Substitua pelo ID do canal desejado
    canal = bot.get_channel(canal_id)

    if canal is not None:
        mensagem = f"Bem-vindo(a), {member.name}! Por favor, digite abaixo seu e-mail institucional."
        await canal.send(mensagem)

    # if role is not None:
    #     await member.add_roles(role)  # Adiciona o cargo ao membro

@bot.event
async def on_message(message):
    # Verifique se a mensagem foi enviada em um canal específico
    if message.channel.id == ID_CANAL_AUT:  # Substitua pelo ID do canal desejado
        # Verifique se o autor da mensagem não é o próprio bot
        if message.author != bot.user:
            usuario = Usuario(message.author)
            if verificar_email(message.content):
                destinatario = message.content
                usuario.email = destinatario
                usuario.codigo = gerar_codigo_aut()
                codigos[usuario.codigo] = usuario
                mandar_email(destinatario, usuario.codigo)
                await message.channel.send(f'Email enviado para {destinatario}')
            elif len(message.content) == QTDE_DIGITOS_CODIGO_AUT:
                cod = int(message.content)
                if cod in codigos.keys():
                    await message.channel.send(f'Usuário {codigos[cod]} autenticado com sucesso')
                    del codigos[cod]
                    # Mudar cargo do usuário da msg
                    # role = discord.utils.get(guild.roles, name='aluno')

arq_token = open("token_discord.txt", )
bot.run(arq_token.readline())
arq_token.close()