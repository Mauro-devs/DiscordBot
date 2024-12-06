import discord
import random
from discord.ext import commands
import asyncio  # Corrigido o nome do módulo para asyncio


# Definindo as permissões necessárias para o bot
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.voice_states = True

# Criando a instância do bot
bot = commands.Bot(command_prefix="/", intents=intents)



@bot.event
async def on_member_join(user):
    channel = bot.get_channel(1255343152244719699)
    embed = discord.Embed(description= (f"Seja bem vindo {user.mention}! ✅"), color = 0x00ff00)
    embed.set_image(url="https://i.pinimg.com/originals/8b/56/f0/8b56f0d49d6baaf048c911f3b0d7c06c.jpg")
    await channel.send(embed=embed)
    await channel.send("✅ Digite '/comandos' para ter acesso a lista de comandos ✅")


@bot.command()
async def ola(ctx: commands.Context):
    usuario = ctx.author
    canal = ctx.channel
    await ctx.reply(f"Olá, {usuario.display_name}\nVocê está no canal: {canal.name}\nTipo do canal: {canal.type}")

@bot.command()
async def comandos(ctx):
    comandos_ajuda = """
    **Comandos Disponíveis:**
    /ola - Mostra em qual canal o usário está e o tipo dele.\n
    /adivinhar - Inicia um jogo de adivinhação de números de 0 - 10.\n
    /desembaralhar - Inicia um jogo de desembaralhar palavras.\n
    /moeda - Gira uma moeda, dando as opções "Cara"😁 ou "Coroa"👑 ao usuário.\n
    /jogo - Inicia um jogo com perguntas sobre computação.\n
    /limpar - Limpa o canal de texto em que o usuário se encontra.\n
    /comandos - Apresenta uma lista dos comandos disponíveis.
    """
    await ctx.send(comandos_ajuda)

@bot.command()
async def moeda(ctx: commands.Context):
    mensagem = await ctx.send("Cara ou coroa?")
    await mensagem.add_reaction("😁")
    await mensagem.add_reaction("👑")
    resultado = random.choice(["😁", "👑"])

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["😁", "👑"]

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=10, check=check)
        if resultado == reaction.emoji:
            await ctx.send(f"Parabéns {user.display_name}, você acertou!🥳.\nDigite '/moeda' para jogar novamente! 🟡")
        else:
            await ctx.send("Que pena, você errou 😢\nDigite o comando '/moeda' novamente para jogar! 🟡")
    except:
        await ctx.send("Tempo esgotado!\nDigite o comando '/moeda' para jogar novamente! 🟡")

@bot.command()
async def desembaralhar(ctx: commands.Context):
    palavras = ["python", "discord", "bot", "programação", "jogo", "desenvolvimento", "artificial", "linguagem", "computador", "internet", "algoritmo", "inteligência", "ciência", "matemática", "história", "geografia", "literatura", "física", "química", "biologia", "engenharia", "filosofia"]
    palavra = random.choice(palavras)
    palavra_embaralhada = ''.join(random.sample(palavra, len(palavra)))

    await ctx.send(f"Desembaralhe a palavra: {palavra_embaralhada}, você tem 15 segundos")

    def check(m):
        return m.author == ctx.author
    try:
        chance = await bot.wait_for('message', timeout=15, check=check)
        if chance.content.lower() == palavra:
            await ctx.send(f"Parabéns {ctx.author.display_name}🥳, você acertou! \nDigite '/desembaralhar' para jogar novamente.")
        else:
            await ctx.send(f"Que pena😢, você errou.\nA palavra correta era {palavra}.\nDigite '/desembaralhar' para jogar novamente.")
    except asyncio.TimeoutError:
        await ctx.send("Tempo esgotado!⏱️ Digite o comando '/desembaralhar' para jogar novamente.")

@bot.command()
async def adivinhar(ctx: commands.Context):
        
    numero_aleatorio = random.randint(0, 10)
    chances = 3
    await ctx.send("Adivinhe o número entre 0 e 10. Você tem 3 chances.")
        
    def check_palpite(m):
            return m.author == ctx.author

    for chance in range(chances):
            try:
                palpite = await bot.wait_for('message', timeout=15, check=check_palpite)
                palpite_num = int(palpite.content)
                
                if palpite_num == numero_aleatorio:
                    await ctx.send(f"Parabéns {ctx.author.display_name}, seu palpite está correto! 🥳.\nDigite '/adivinhar' para jogar novamente.")
                    return
                elif palpite_num < numero_aleatorio:
                    await ctx.send("O número é maior 👆")
                else:
                    await ctx.send("O número é menor 👇")
            
            except asyncio.TimeoutError:
                await ctx.send(f"O tempo acabou! ⏱️{numero_aleatorio}⏱️.\nDigite '/adivinhar' para jogar novamente.")
                return
            except ValueError:
                await ctx.send("Por favor, insira um número válido. 😁")
        
    await ctx.send(f"Que pena😢, você não conseguiu adivinhar.\nO número era {numero_aleatorio}. Digite '/adivinhar' para jogar novamente.")

@bot.command()
async def jogo(ctx):
    ctx.send("Este é um quiz sobre computação 💻\nSegue perguntas abaixo:")
    perguntas = [
        ("Uma máquina que processa dados de acordo com instruções programadas.", "Computador"), ("Software que gerencia o hardware do computador e fornece serviços para programas.", "Sistema operacional"),
        ("Um meio de comunicação entre o programador e o computador para escrever software.", "Linguagem de programação"), ("Um conjunto de instruções passo a passo para resolver um problema.", "Algoritmo"),
        ("Um erro ou falha em um programa de computador que causa comportamento incorreto.", "Bug"), ("Uma rede global de computadores interconectados que compartilham informações.?", "Internet"),
        ("Um endereço numérico que identifica um dispositivo na rede.", "Ip"), ("Um sistema de segurança que monitora e controla o tráfego de rede com base em regras de segurança.", "Firewall"),
        ("Um conjunto organizado de dados armazenados e acessados eletronicamente.", "Banco de dados"), ("Um conjunto de definições e protocolos para construir e integrar software de aplicações.", "Api"),
        ("Programas e outros sistemas operacionais usados por um computador.", "Software"), ("Componentes físicos de um computador, como CPU, RAM e disco rígido.", "Hardware"),
        ("Serviços de computação fornecidos pela internet, incluindo armazenamento, servidores e bases de dados.", "Computação em nuvem"), ("O processo de codificação de informações para impedir o acesso não autorizado.", "Criptografia"),
        ("Um computador que fornece dados a outros computadores em uma rede.", "Servidor"), ("Simulação de processos de inteligência humana por sistemas de computador.", "Inteligência Artificial")
    ]
    
    pergunta, resposta = random.choice(perguntas)
    await ctx.send(pergunta)

    def check(m):
        return m.author == ctx.author

    try:
        chance = await bot.wait_for('message', timeout=20, check=check)
        if chance.content.lower() == resposta.lower():
            await ctx.send(f"Parabéns {ctx.author.display_name}, você acertou! 🥳 \nDigite '/jogo' para jogar novamente.")
        else:
            await ctx.send(f"Que pena😢, você errou. A resposta correta era {resposta}.\nDigite '/jogo' para jogar novamente.")
    except asyncio.TimeoutError:
        await ctx.send("Tempo esgotado!⏱️ Digite '/jogo' para jogar novamente.")

@bot.command()
async def limpar(ctx: commands.Context):
    try:
        if ctx.guild.me.guild_permissions.manage_messages:
            await ctx.channel.purge()
            await ctx.send("Seu canal está limpo\nPara limpar novamente digite: '/limpar'", delete_after=5)
            
        else:
            await ctx.send('Você não tem permissão para apagar mensagens', delete_after=5)
    except:
        await ctx.send("Ocorreu um erro, digite '/limpar'", delete_after= 5)

@bot.event
async def on_ready():
    print("Estou funcionando")

with open ("token.0.txt", "r", encoding="utf-8") as f:
    bottoken = f.read()

bot.run(bottoken)
