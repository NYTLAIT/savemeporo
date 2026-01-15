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

cog(self)->captain->controls
bot(main bot in bot.py)->ship->engine
self.bot->the link
each cog(captain) is its own but can all control the ship

async def test(self, interaction:discord.Interaction): -> test is the method, needs to know which instance it belongs to

unsure of what __init__ does still

        # global sync ->
    await bot.tree.sync()
        # server id way -> 
        # for now, says global sync may take longer
    guild = discord.Object(id=guild_id)
    # not sure what does but said something about needing to specify the server
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)

__init__.py in cogs is simply to treat that folder as a package, nothing really has to go in there

