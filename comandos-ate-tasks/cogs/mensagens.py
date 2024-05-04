import discord
from discord import app_commands
from discord.ext import commands, tasks

class Mensagens(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
        
    @app_commands.command()
    async def registrar(self, interact:discord.Interaction):
        await interact.response.send_modal(Registro_Modal())
        interact.message.con

class Registro_Modal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title='Registrar')

    nome = discord.ui.TextInput(label='Nome', placeholder='Exemplo: Dutrinha', max_length=30)
    idade = discord.ui.TextInput(label='Idade', placeholder='18', max_length=2)
    sobre = discord.ui.TextInput(label='Conte-nos sobre você', required=False, style=discord.TextStyle.long)
    async def on_submit(self, interact:discord.Interaction):
        await interact.response.send_message(f"Olá, {self.nome}\nIdade: {self.idade}\nDescrição: {self.sobre}")

async def setup(bot):
    await bot.add_cog(Mensagens(bot))