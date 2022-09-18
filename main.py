import discord
import os
from dotenv import load_dotenv

client = discord.Client(intents=discord.Intents.default())

load_dotenv()
TOKEN = os.getenv("TOKEN")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Bonjour"):
        await message.channel.send("Bonjour, bienvenue sur le serveur")

    if message.content == "Help":
        await message.author.send('Je t\'écoute que puis-je faire pour toi?')




@client.event
async def on_connect():
    print("Mr Robot est connecté au serveur")
    channel = client.get_channel("channel id")
    await channel.send("Je suis la pour vous aider")
    client.get_channel("channel id")
    await channel.send('Que puis-je faire pour vous?')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Bienvenue sur le serveur {member} n'hésite pas à me solliciter!")

client.run(TOKEN)
