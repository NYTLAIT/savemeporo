import discord
from discord.ext import commands

# SETUP AND LINK TO MAIN FILE(bot.py)
class LogCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # SIMPLE CHECK IF WORKING
    @discord.app_commands.command(name='test_log', description='testing if log commands work')
    async def test001(self, interaction:discord.Interaction):
        await interaction.response.send_message(f'log_cog_bot_test a success!')

    # ENTER NEW LEDGER LOG, /COMMAND FORMAT ->
    # /log <action: autocomplete> <amount: int> <note: str>
    @discord.app_commands.command(name="log", description="Enter a new a ledger log")
    @discord.app_commands.describe(
        action="in (gained money)|out (lost money)",
        amount="enter amount gained/lost",
        note="(in) optional note | (out) suggested for item spent on"
    )

    @discord.app_commands.autocomplete(action=action_autocomplete)
    async def log(self, interaction:discord.Interaction, action: str, amount: float, note: str):
        await interaction.response.send_message(
            f'test log_command: action-{action}, amount-{amount}, note-{note}')
        
    # ^ for the autocomplete 
    # (must be explicity attached for autocomplete above to work: is why amount and note are not autocompletes)
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name='action_option', value='action_option')
            for action_option in action_options if current.lower() in action_option.lower()
        ]
    
    # PRINT IF COG IS BEING SEEN
    print('log_commands.py: log_cog is being seen')
    
async def setup(bot):
    await bot.add_cog(LogCommandsCog(bot))
    print('log_commands.py: log commands have loaded and synced to bot.py')