import discord
from discord.ext import commands

# SETUP AND LINK TO MAIN FILE(bot.py)
class AdjustCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # SIMPLE CHECK IF WORKING
    @discord.app_commands.command(name='test_adjust', description='testing if adjust command work')
    async def test_adjust(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'adjust_cog_bot_test a success!')

    

    print('adjust_commands.py: adjust_cog is being seen')
    
async def setup(bot):
    await bot.add_cog(AdjustCommandsCog(bot))
    print('adjust_commands.py: adjust command have loaded and synced to bot.py')