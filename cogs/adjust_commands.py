import discord
from discord.ext import commands

from logics.adjust_logic import enter_adjust

# SETUP AND LINK TO MAIN FILE(bot.py)
class AdjustCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ENTER ADJUST LOG, /COMMAND FORMAT -> /log <action: autocomplete> <amount: float> <adjust_id: int>
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]

    @discord.app_commands.command(name="adjust", description="Enter correct amount to make adjustments to upset another log")
    @discord.app_commands.describe(
        action="the correct action, type 'in' (adding) | 'out' (spending)",
        amount="the correct amount",
        adjust_id="id of the incorrect log"
        )
    
    @discord.app_commands.autocomplete(action=action_autocomplete)
    async def adjust(self, interaction:discord.Interaction, action: str, amount: float, adjust_id: int):

        await interaction.response.defer()

        # LOGIC INSERT
        user = str(interaction.user)
        receipt = enter_adjust(adjust_id, action, amount, user)
        # ^^^END

        # EMBED FILL
        embed = discord.Embed(
            title="ADJUST",
            description=f"ID of Adjusted Log: {receipt['adjust_id']} \n"
                        f"Original Amount: {receipt['original_amount']} \n"
                        f"Correct Amount: ${receipt['correct_amount']} \n"
                        f"Balance: ${receipt['balance']}",
            color=discord.Color.dark_teal()
        )

        # ^^^END

        await interaction.followup.send(embed=embed, ephemeral=True)
    # ^^^END
        
    # PRINT IF COG IS BEING SEEN
    print('adjust_commands.py: adjust_cog is being seen')

# LINK TO MAIN BOT
async def setup(bot):
    await bot.add_cog(AdjustCommandsCog(bot))
    print('adjust_commands.py: adjust commands have loaded and synced to bot.py')