Came up with that it should be async since its a bot and may do multiple tasks at once but well figure that out later

commands.Bot is the same as commands.Client im pretty sure

i dont really know what cog means except its like a seperator of what things are

files are snake_case, classes are PascalCase

FOR 
bot.start()
->
load_extension("cogs.slashy_commands_cog")
->
Discord.py imports the file
->
finds async def setup(bot)
->
setup() creates the Cog
->
bot.add_cog()
->
commands/events are registered