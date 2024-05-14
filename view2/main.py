import discord, os
from discord.ext import commands
from discord import SelectOption

permissoes = discord.Intents.all()
bot = commands.Bot('.', intents=permissoes)

async def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}")

@bot.event
async def on_ready():
    await carregar_cogs()
    print(f"Pronto!\n")

bot.run("")