import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/selam'):
        await message.channel.send(f'As Ben {client.user} Nasıl yardımcı olabilirim?')
    elif message.content.startswith('/'):
        await message.channel.send(f'As Ben {client.user} Nasıl yardımcı olabilirim?')
        
client.run("TOKEN GİR")
