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


---------------------------------------------JSON STUFF I DONT GET JUST YET
import json
import asyncio

class JSONDataManager:
    def __init__(self, file_path='data.json'):
        self.file_path = file_path
        self.lock = asyncio.Lock()
        # Load data at startup
        try:
            with open(self.file_path, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}

    async def get_user(self, user_id):
        return self.data.get(str(user_id), {})

    async def set_user(self, user_id, value: dict):
        async with self.lock:
            self.data[str(user_id)] = value
            # Save immediately
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=4)

    async def update_user_points(self, user_id, points):
        async with self.lock:
            user_data = self.data.get(str(user_id), {'points': 0})
            user_data['points'] += points
            self.data[str(user_id)] = user_data
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=4)
            return user_data['points']

from discord.ext import commands
from data_manager import JSONDataManager

bot = commands.Bot(command_prefix='/', intents=intents)
data_manager = JSONDataManager()

@bot.command()
async def addpoints(ctx, amount: int):
    new_points = await data_manager.update_user_points(ctx.author.id, amount)
    await ctx.send(f"{ctx.author.mention} now has {new_points} points!")
 ---------------------------------------------------

discord.apps_commands.command in cog
bot.command in main

**REALLY COOL WAY OF FILTERING**
really cool way of filtering:
for action_option in action_options if current.lower() in action_option.lower()
loop through items in action_options -> for action_option in action_options
return the option if the current being typed is in(part of) an action_option item -> if current.lower() in action_option.lower()

(name='action_option', value='action_option') -> creates options for dropdown
**END**

**FLOW OF COMMANDS WITH AUTOCOMPLETE**
discord.app_commands.command -> defines /commmand
discord.app_commands.command -> adds descriptions to the options
discord.app_commands.command -> dynamic suggestion generator
some reason discord.py likes metadata and dynamic stuff seperate or some???
im not to sure about it but wow, ig code has personality alright

I still do not understand but here:
    async def action_autocomplete(self, interaction:discord.Interaction, current: str
    ) -> list[discord.app_commands.Choice[str]]:
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]
the -> is something to do with type hint, which says some like the function being defined is going to return a list of app_commands.Choice, i dont know why it is in this syntax and most importantly why im getting an error when I dont include it, at least from my understand of this error message:
discord.ext.commands.errors.ExtensionFailed: Extension 'cogs.log_commands' raised an error: TypeError: unknown parameter given: action

nvm, im a liar, just needed the function to be above the discord.app_commands.command which i still dont get why

    # for the autocomplete below
    # (must be explicity written and put into in the autocomplete for autocomplete below to work: 
    # is why amount and note are not autocompletes)
    async def action_autocomplete(self, interaction:discord.Interaction, current: str):
        action_options = ['in', 'out']
        return [
            discord.app_commands.Choice(name=action_option, value=action_option)
            for action_option in action_options if current.lower() in action_option.lower()
        ]
**END**

**ABOUT THE COMMAND PREFIX BEING NEEDED**
bot = Bot(command_prefix='/', intents=intents)
command_prefix still needed apparently, something about:
^ '__init__() missing 1 required positional argument: 'command_prefix''
**END**

**CLASS SYNTAX**
class Child(Parent):
child inherits everything but can add or override what i want
**END**





