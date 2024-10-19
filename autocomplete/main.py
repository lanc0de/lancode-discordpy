import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

frutas = ["maçã", "banana", "laranja", "morango", "uva", "pera", "abacaxi", "melão", "mamão", "kiwi", "tangerina", "limão", "romã", "caqui", "figo", "abacate", "goiaba", "cereja", "ameixa", "pêssego","carambola", "jaca", "maracujá", "framboesa", "amora", "jabuticaba", "pitanga", "graviola", "cupuaçu","caju", "manga", "siriguela", "umbu", "acerola", "marmelo", "groselha", "ará", "lichia", "tomate","coco", "papaya", "cajá", "tamarindo", "jabuticaba", "pitanga", "graviola", "cupuaçu", "caju", "manga", "siriguela"]

@bot.tree.command()
async def escolher_fruta(interact:discord.Interaction, fruta:str):
    await interact.response.send_message(f'Você Escolheu {fruta}')

@escolher_fruta.autocomplete('fruta')
async def fruta_autocomplete(interact:discord.Interaction, pesquisa:str):
    opcoes = []
    for fruta in frutas:
        if pesquisa in fruta:
            fruta_opcao = app_commands.Choice(name=fruta, value=fruta)
            opcoes.append(fruta_opcao)
    return opcoes[:25]

@bot.event
async def on_ready():
    await bot.tree.sync()

bot.run("TOKEN")
