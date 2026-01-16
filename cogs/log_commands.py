import discord
from discord.ext import commands

from logics.log_logic import enter_log

# SETUP AND LINK TO MAIN FILE(bot.py)
"""
create snippet/clone/uh of main bot from commands.Cog 
which gets initialized so that it may be referenced 
so that the commands in the cog can do what main bot does
"""
class LogCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # SIMPLE CHECK IF WORKING
    @discord.app_commands.command(name='test_log', description='testing if log commands work')
    async def test_log(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'log_cog_bot_test a success!')

    # ENTER NEW LEDGER LOG, /COMMAND FORMAT -> /log <action: autocomplete> <amount: int> <note: str>
    """
    created function action_autocomplete to provide the choices
    and also filter what the user is typing live
    """
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]

    """
    .command declares the /command and creates it/lists it but doesnt do anything
    and .describe describes the component and also give description to user typing
    """
    @discord.app_commands.command(name="log", description="Enter a new a ledger log")
    @discord.app_commands.describe(
        action="in (gained money)|out (lost money)",
        amount="enter amount gained/lost",
        note="(in) optional note | (out) suggested write what item spent on"
    )
    
    @discord.app_commands.autocomplete(action=action_autocomplete)
    async def log(self, interaction:discord.Interaction, action: str, amount: float, note: str):
        """
        creates the dynamic stuffs, that brings that UI for the autocomplete, float, and str
        """
        user = str(interaction.user)
        enter_log(action, amount, note, user, data_file='data.json')

        await interaction.response.send_message(
            f'test log_command-> action:{action}, amount:{amount}, note:{note}')
        
    # PRINT IF COG IS BEING SEEN
    print('log_commands.py: log_cog is being seen')

# LINK TO MAIN BOT
async def setup(bot):
    """
    links to the main bot, setup_hook in bot.py looks for setup,
    looks inside and then brings main bot reference like imprinting
    so that the commands can call the main bot

    TODO: unsure of how the process really runs from start to finish
    since it **seems** top to bottom but no time to check debugging 
    feature to follow path right now
    """
    await bot.add_cog(LogCommandsCog(bot))
    print('log_commands.py: log commands have loaded and synced to bot.py')