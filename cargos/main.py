import discord
from discord.ext import commands
from discord import app_commands

permissoes = discord.Intents.all()
bot = commands.Bot('.', intents=permissoes)

@bot.event
async def on_ready():
    print(f"Pronto!\n")

@bot.command()
async def cargo_verde(ctx:commands.Context):
    membro = ctx.author
    cargo_verde = discord.utils.get(ctx.guild.roles, name='verde')

    await membro.add_roles(cargo_verde)

@bot.command()
async def listar_cargos(ctx:commands.Context):
    cargos_usuario = ctx.author.roles
    for cargo in cargos_usuario:
        if cargo.is_default():
            cargos_usuario.remove(cargo)
    print(cargos_usuario)

@bot.command()
async def criar_cargo(ctx:commands.Context, *, nome):
    permissoes = discord.Permissions(administrator = True)
    cargo_criado = await ctx.guild.create_role(name=nome, color=0x457EAC, permissions=permissoes) 

    await ctx.author.add_roles(cargo_criado)
    await ctx.reply(f"Cargo {cargo_criado.name} criado e adicionado a {ctx.author.mention}.")

bot.run("")