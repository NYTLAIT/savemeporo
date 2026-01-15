import discord
from discord.ext import commands

# SETUP AND LINK TO MAIN FILE(bot.py)
class SlashyCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # SIMPLE CHECK IF WORKING
    @discord.app_commands.command(name='test_slashy', description='testing if slash commands work')
    async def test001(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'slashy_cog_bot_test a success!')

    print('slashy_commands.py: slashy_cog is being seen')
    
async def setup(bot):
    await bot.add_cog(SlashyCommandsCog(bot))
    print('slashy_commands.py: slashy commands have loaded and synced to bot.py')
