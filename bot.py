import discord
from discord.ext import commands

import logging

import os
from dotenv import load_dotenv
load_dotenv()



discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
bot.run(discord_token, log_handler=handler, log_level=logging.DEBUG)
