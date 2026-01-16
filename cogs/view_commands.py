import discord
from discord.ext import commands

from logics.view_logic import view_option_gateway

# SETUP AND LINK TO MAIN FILE(bot.py)
class ViewCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ENTER NEW LEDGER LOG, /COMMAND FORMAT -> /log <action: autocomplete> <amount: int> <note: str>
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        action_options = ['year', 'month', 'day']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]

    @discord.app_commands.command(name="view", description="View ledger")
    @discord.app_commands.describe(scope="statement range")
    
    @discord.app_commands.autocomplete(scope=action_autocomplete)
    async def view(self, interaction:discord.Interaction, scope: str):
        
        await interaction.response.defer()

        # LOGIC INSERT
        user = str(interaction.user)
        statement = view_option_gateway(user, scope)
        # ^^^END

        # EMBED FILL
        embed = discord.Embed(
            title=f"{scope.capitalize()} Statement - {statement[scope]}",
            description=f"Total Added: ${statement['total_added']} | Total Spent: ${statement['total_spent']} \n"
                        f"Net Change: ${statement['net_change']} \n"
                        f"Balance: ${statement['balance']}",
            color=discord.Color.dark_teal()
        )

        # ^^^END

        await interaction.followup.send(embed=embed, ephemeral=True)
        
    # PRINT IF COG IS BEING SEEN
    print('view_commands.py: view_cog is being seen')

# LINK TO MAIN BOT
async def setup(bot):
    await bot.add_cog(ViewCommandsCog(bot))
    print('view_commands.py: view commands have loaded and synced to bot.py')