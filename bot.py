# created by: Tsz Kit Wong
# bot.py

import discord
import os
import random
from webScrapFunctions import *
from dotenv import load_dotenv


TOKEN = "TOKEN"
GUILD = "GUILD"
client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} enabled.")  # display message in console when connected

@client.event
async def on_message(message):
    # prevents bot from replying to itself and causing endless loop
    if message.author == client.user:
        return

    call = "$bot Price Check "
    if call in message.content:
        before_call, call, ticker = message.content.partition(call)
        await message.channel.send(initiate(ticker))


client.run(TOKEN)
