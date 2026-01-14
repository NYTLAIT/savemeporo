import discord
from discord.ext import commands

import logging

import os
from dotenv import load_dotenv
load_dotenv()

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# SETUP DEBUGGING/CHECKING
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if 'summon bots' in message.content.lower():
        await message.channel.send(f'{message.author.mention} has summoned me!')
    await bot.process_commands(message)

# TO LINK /COMMANDS FILE
@bot.event
async def on_ready():
    await bot.load_extensions('cogs.slashy_commands')
    await bot.tree.sync()

bot.run(discord_token, log_handler=handler, log_level=logging.DEBUG)
  