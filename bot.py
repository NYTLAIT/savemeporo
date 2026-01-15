import discord
import asyncio
from discord.ext import commands

import logging

import os
from dotenv import load_dotenv
load_dotenv()

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
discord_token = os.getenv('DISCORD_TOKEN')
guild_id = int(os.getenv('GUILD_ID')) 

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# TERMINAL READY SIGN | LINK /COMMAND FILES (cogs FOLDER)  
class Bot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('cogs.slashy_commands')
        await self.load_extension('cogs.entry_commands')
        await self.load_extension('cogs.view_commands')

        guild = discord.Object(id=guild_id)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        print(f'{self.user.name} IS ONLINE')

# bot = Bot(command_prefix='/', intents=intents)
bot = Bot(intents=intents)

# SIMPLE CHECK JUST TO SEE IF BOT IS IN CHAT
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if 'summon bots' in message.content.lower():
        await message.channel.send(f'{message.author.mention} has summoned me!')
    # await bot.process_commands(message)

bot.run(discord_token, log_handler=handler, log_level=logging.DEBUG)
  