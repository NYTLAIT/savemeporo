import discord
from discord.ext import commands

# TODO: oraganize them later but for now, template and dump will do

# SETUP AND LINK TO MAIN FILE(bot.py)
class SlashyCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
async def setup(bot):
    await bot.add_cog(SlashyCommandsCog(bot))