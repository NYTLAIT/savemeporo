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
            title=f"{scope.capitalize()} Statement - {statement['month_name']}",
            description=f"Added: ${statement['total_added']} | Spent: ${statement['total_spent']} \n"
                        f"Net Change: ${statement['net_change']} \n"
                        f"Balance: ${statement['balance']}",
            color=discord.Color.dark_teal()
        )

        # EMBED FEILD LOOPS DEPENDING ON SCOPE TYPE
        # YEAR
        if scope == 'year':
            for month_num, monthly_data in statement['monthly_data'].items():
                embed.add_field(
                name=f"{monthly_data['month']}",
                value=(
                    f"Added: ${monthly_data['added']} | "
                    f"Spent: ${monthly_data['spent']} | "
                    f"Net: ${monthly_data['net_change']} \n"
                ),
                inline=False
            )
                
                month_logs = []
                for log in monthly_data['logs']:
                    month_logs.append(
                        f"id {log['ledger_id(PK)']} | "
                        f"{log['action']} | "
                        f"${log['amount']} | "
                        f"{log.get('note', '—')}"
                    )
                # IN CASIES
                if month_logs:
                    embed.add_field(name=f"Entries: {len(monthly_data['logs'])}", value="\n".join(month_logs[:8]), inline=False)
        
        # MONTH
        elif scope == "month":
            for week_num, weekly_data in statement['weekly_data'].items():
                embed.add_field(
                name=f"Week {week_num} ({weekly_data['week_start_date']} - {weekly_data['week_end_date']})",
                value=(
                    f"Added: ${weekly_data['added']} | "
                    f"Spent: ${weekly_data['spent']} | "
                    f"Net: ${weekly_data['net_change']}"
                ),
                inline=False
                )
            
                week_logs = []
                for log in weekly_data['logs']:
                    week_logs.append(
                        f"id {log['ledger_id(PK)']} | "
                        f"{log['action']} | "
                        f"${log['amount']} | "
                        f"{log.get('note', '—')}"
                    )
                # IN CASIES
                if week_logs:
                    embed.add_field(name=f"Entries: {len(weekly_data['logs'])}", 
                                    value="\n".join(week_logs[:8]), 
                                    inline=False
                                    )
        
        # DAY
        elif scope == "day":
            for time_num, timely_data in statement['timely_data'].items():
                embed.add_field(
                name=f"{timely_data['time']}",
                value=(
                    f"Added: ${timely_data['added']} | "
                    f"Spent: ${timely_data['spent']} | "
                    f"Net: ${timely_data['net_change']}"
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
                    embed.add_field(name=f"Entries: {len(timely_data['logs'])}", 
                                    value="\n".join(day_logs[:8]), 
                                    inline=False
                                    )

        # ^^^END

        await interaction.followup.send(embed=embed, ephemeral=True)
        
    # PRINT IF COG IS BEING SEEN
    print('view_commands.py: view_cog is being seen')

# LINK TO MAIN BOT
async def setup(bot):
    await bot.add_cog(ViewCommandsCog(bot))
    print('view_commands.py: view commands have loaded and synced to bot.py')