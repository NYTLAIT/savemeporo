1. no data should be deleted as id assignment system will break
2. may run into issues with loading in the data.json file (only if two people write at a command at the exact same time as the data is only read once at the start and never updates until the end of the slash command process)
3. docstrings in cogs not properly added, more just notes for me
4. "discord.ext.commands.errors.ExtensionFailed: Extension 'cogs.log_commands' raised an error: NameError: name 'data' is not defined" even when defined. quick fix of explicityly declaring the data_file which data takes in as a parameter