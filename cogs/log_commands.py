import discord
from discord.ext import commands

from logics.log_logic import enter_log

# SETUP AND LINK TO MAIN FILE(bot.py)
class LogCommandsCog(commands.Cog):
    def __init__(self, bot):
        """
        create snippet/clone/uh of main bot from commands.Cog 
        which gets initialized so that it may be referenced 
        so that the commands in the cog can do what main bot does
        """
        self.bot = bot

    # ENTER NEW LEDGER LOG, /COMMAND FORMAT -> /log <action: autocomplete> <amount: int> <note: str>
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        """
        created function action_autocomplete to provide the choices
        and also filter what the user is typing live
        """
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]

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
        await interaction.response.defer()

        # LOGIC INSERT
        user = str(interaction.user)
        receipt = enter_log(action, amount, note, user)
        # ^^^END

        # EMBED FILL
        if action == 'in':
            title = "ADD"
        elif action == 'out':
            title = "OUT"

        embed = discord.Embed(
            title=title,
            description=f"Added: ${receipt['amount']} \n"
                        f"Note: {receipt['note']} \n"
                        f"Balance: ${receipt['balance']}",
            color=discord.Color.dark_teal()
        )

        for time_num, timely_data in receipt['timely_data'].items():
            embed.add_field(
            name=f"{timely_data['time']}",
            value=(
                f"Added: ${timely_data['added']} | "
                f"Spent: ${timely_data['spent']} | "
                f"Net: ${timely_data['net_change']} \n"

            ),
            inline=False
            )

            day_logs = []
            for log in timely_data['logs']:
                day_logs.append(
                    f"id {log['ledger_id(PK)']} | "
                    f"{log['action']} | "
                    f"${log['amount']} | "
                    f"{log.get('note', '—')}"
                )
            # IN CASIES
            if day_logs:
                embed.add_field(name="", 
                                value="\n".join(day_logs[:8]), 
                                inline=False
                                )
        # ^^^END

        await interaction.followup.send(embed=embed, ephemeral=True)
        
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