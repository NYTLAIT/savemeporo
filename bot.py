import discord
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

# TERMINAL READY | LINK /COMMAND FILES (cogs FOLDER)
"""
Created "custom"/"extension"/"modified" discord bot(commands.Bot) 
that modifies default startup behavior to load /commands

1. setup_hook provided in the discord.py library to load cogs and 
"sync em"/or some better word to main bot
2. sync the cog commands into the specified guild/server
3. since the bot is more about the slash commands, checking if class 
code went through
"""
class Bot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension('cogs.zzz_slashy_commands')
        await self.load_extension('cogs.log_commands')
        await self.load_extension('cogs.adjust_commands')
        await self.load_extension('cogs.view_commands')

        guild = discord.Object(id=guild_id)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)

        print(f'{self.user.name} IS ONLINE')

# BOT INSTANCE, seems important to note
"""
Create instance of modified bot that creates the connection to Discord (the platform)
"""
bot = Bot(command_prefix='/', intents=intents)

# SIMPLE CHECK JUST TO SEE IF BOT IS IN CHAT
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if 'summon bots' in message.content.lower():
        await message.channel.send(f'{message.author.mention} has summoned me!')
    await bot.process_commands(message)

# RUN BOT
bot.run(discord_token, log_handler=handler, log_level=logging.DEBUG)
  