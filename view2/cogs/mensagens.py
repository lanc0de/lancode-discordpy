import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord import SelectOption

class ViewCumprimento(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Ola', custom_id='botao_ola')
    async def botao_ola(self, interact:discord.Interaction, botao:discord.ui.Button):
        await interact.response.send_message(f"Olá, {interact.user.name}!")
    
    opcoes = [
        SelectOption(label='Marmita'),
        SelectOption(label='Lasanha'),
        SelectOption(label='Melancia')
    ]
    
    @discord.ui.select(placeholder='Qual a sua comida favorita?', options=opcoes, custom_id='select_comida')
    async def selecao_resposta(self, interact:discord.Interaction, select:discord.ui.Select):
        opcao_escolhida = select.values[0]
        await interact.response.send_message(f"Você escolheu {opcao_escolhida}!")


class Mensagens(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    @commands.command()
    async def view_persistente(self, ctx:commands.Context):
        view_cumprimento = ViewCumprimento()
        await ctx.reply(view=view_cumprimento)


async def setup(bot):
    bot.add_view(ViewCumprimento())
    await bot.add_cog(Mensagens(bot))