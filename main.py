import discord
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot giriş yaptı: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!selam":
        await message.channel.send("Merhaba! 👋")

client.run(os.getenv("TOKEN"))

