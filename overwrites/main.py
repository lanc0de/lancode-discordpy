import discord
from discord.ext import commands
from discord import app_commands
from pprint import pprint

intents = discord.Intents.all()
bot = commands.Bot('.', intents=intents)

@bot.event
async def on_ready():
    print(f"Pronto!\n")

@bot.command()
async def mudar_permissoes(ctx:commands.Context):
    canal = ctx.channel
    membro = ctx.author
    
    overwrites = discord.PermissionOverwrite()
    overwrites.add_reactions = True
    overwrites.attach_files = True
    overwrites.mention_everyone = False
    
    await canal.set_permissions(membro, overwrite=overwrites)

@bot.command()
async def obter_permissoes(ctx:commands.Context):
    canal = ctx.channel
    membro = ctx.author

    permissoes_usuario = canal.permissions_for(membro)
    if permissoes_usuario.manage_messages:
        await ctx.reply("Você pode gerir mensagens!")
    print(permissoes_usuario.manage_messages)

bot.run("")