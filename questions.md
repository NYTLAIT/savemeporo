**cogs/log_commands.py** getting a yellow squigly for action_autocomplete with suggestion: 
def action_autocomplete(
    self: Self@LogCommandsCog,
    interaction: Interaction[Client],
    current: str
) -> CoroutineType[Any, Any, list[Choice[str]]]:
saw it in the discord.py docs but i didnt understand it and got really offput by the -> symbol.