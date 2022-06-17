# created by: Tsz Kit Wong
# bot.py

import discord
import os
import random
from dotenv import load_dotenv

TOKEN = "OTg3NDI2Njk4ODAwODEyMTEz.GnB-tu.iDFVr456Tv35jyjflHXrk5tNNIqPfu0BrpTzMQ"
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$flipcoin"):

        random_num = random.randint(0,1)
        choice = None

        if random_num == 0: choice = "heads"
        elif random_num == 1: choice = "tails"

        await message.channel.send(choice)

client.run(TOKEN)
