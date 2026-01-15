import discord
from discord.ext import commands

# SETUP AND LINK TO MAIN FILE(bot.py)
class ViewCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # SIMPLE CHECK IF WORKING
    @discord.app_commands.command(name='test_view', description='testing if slash commands work')
    async def test_view(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'view_cog_bot_test a success!')

    print('view_commands.py: view_cog is being seen')
    
async def setup(bot):
    await bot.add_cog(ViewCommandsCog(bot))
    print('view_commands.py: view commands have loaded and synced to bot.py')