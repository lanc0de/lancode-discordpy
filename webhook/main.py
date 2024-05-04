from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook('')

embed = DiscordEmbed(title='Titulo', description='Descrição')

with open('imagens/imagem.jpg', 'rb') as imagem:
    webhook.add_file(imagem.read(), 'imagem.jpg')
    embed.set_image(url='attachment://imagem.jpg')
    
webhook.add_embed(embed)

webhook.execute()