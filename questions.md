**cogs/log_commands.py** getting a yellow squigly for action_autocomplete with suggestion: 
def action_autocomplete(
    self: Self@LogCommandsCog,
    interaction: Interaction[Client],
    current: str
) -> CoroutineType[Any, Any, list[Choice[str]]]:
saw it in the discord.py docs but i didnt understand it and got really offput by the -> symbol.
FIXED (NOT), just had to define the action_autocomplete before the auto_complete thing, still dont get the syntax and the -> makes me nervous D:

>>>so apparently i didnt need the -> CoroutineType[Any, Any, list[Choice[str]]]:, its just to help readability, dont get the syntax so will not be putting it in
but basically had to put the function above the discord.app_commands.command not just the discord.app_commands.autocomplete which i do not understand why since it doesnt seem to be referenced in the discord.app_commands.command

**.gitignore** do not understand why even if i wrote notes.md and questions.md into the .gitignore file. it doesnt seem to be getting ignored?

**docstrings**
how do i use docstrings properly?
(log_command.py)

