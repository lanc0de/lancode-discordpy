import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import datetime, pytz

class Bot_modificado(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='.', intents=discord.Intents.all())
    async def setup_hook(self):
        self.add_view(View_persistente())
bot = Bot_modificado()

async def carregar_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}")

@bot.event
async def on_ready():
    await carregar_cogs()
    await bot.tree.sync()
    print("Estou pronto!")

@bot.command()
async def sincronizar(ctx:commands.Context):
    if ctx.author.id == 1037315487358529586:
        server = discord.Object(id=1177347390844436554)
        sincs = await bot.tree.sync(guild=server)
        await ctx.reply(f"{len(sincs)} comandos sincronizados")
        ctx.message.author.timeout()
    else:
        await ctx.reply('Apenas o meu dono pode usar esse comando!')

class View_persistente(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label='me aperte', custom_id='botao')
    async def botao(self, interact:discord.Interaction, button):
        await interact.response.send_message('O botao foi pressionado')

@bot.command()
async def gugu(ctx:commands.Context):
    await ctx.reply(view=View_persistente())

@bot.tree.command(description='Responde o usuário com olá')
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f'Olá, {interact.user.name}')
    await interact.followup.send(f'Bom te ver de novo!')

@bot.tree.command()
@app_commands.choices(cor=[
    app_commands.Choice(name='Vermelho', value='BA2D0B'),
    app_commands.Choice(name='Azul', value='22577A'),
    app_commands.Choice(name='Amarelo', value='FFC145')
])
async def cor(interact:discord.Interaction, cor:app_commands.Choice[str]):
    await interact.response.send_message(f"O código hexadecimal da cor {cor.name} é {cor.value}")

@bot.command()
async def enviar_embed(ctx:commands.Context):
    meu_embed = discord.Embed(title='Olá, Mundo!', description='Descrição :D')
    
    imagem_arquivo = discord.File('imagens/imagem.jpg', 'imagem.jpg')
    meu_embed.set_image(url="attachment://imagem.jpg")

    thumb_arquivo = discord.File('imagens/thumb.jpg', 'thumb.png')
    meu_embed.set_thumbnail(url='attachment://thumb.png')

    meu_embed.set_footer(text='Este é o footer')

    meu_embed.color = discord.Color.dark_blue()

    canal_foto = discord.File('imagens/foto_canal.png', 'foto_canal.png')
    meu_embed.set_author(name='Lan Code', icon_url='attachment://foto_canal.png')

    meu_embed.add_field(name='Moedas', value=10, inline=False)
    meu_embed.add_field(name='Filme Favorito', value='DBS: Broly', inline=False)
    meu_embed.add_field(name='Rank', value='Prata', inline=False)


    await ctx.reply(files=[imagem_arquivo, thumb_arquivo, canal_foto], embed=meu_embed)

@bot.command()
async def botao(ctx:commands.Context):
    async def resposta_botao(interact:discord.Interaction):
        await interact.response.send_message('Botão Pressionado!', ephemeral=True)
        await interact.followup.send('Segunda resposta :D')
    view = discord.ui.View()
    botao = discord.ui.Button(label='Botão Infinito', style=discord.ButtonStyle.green)
    botao.callback = resposta_botao
    view.add_item(botao)
    await ctx.send(view=view)

@bot.tree.command()
async def escolher_membro(interact:discord.Interaction, member:discord.Member):
    print(type(member))

@bot.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f"Novo canal criado: {canal.name}")

@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1196465713465008208)
    meu_embed = discord.Embed(title=f'Bem vindo, {membro.name}!')
    meu_embed.description = "Aproveite a estadia!"
    meu_embed.set_thumbnail(url=membro.avatar)
    await canal.send(embed=meu_embed)

@bot.event
async def on_member_remove(membro:discord.Member):
    canal = bot.get_channel(1196465713465008208)
    await canal.send(f"{membro.display_name} Saiu no servidor...\nAté Breve!")
bot.run("")