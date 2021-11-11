import disnake
from disnake.ext import commands
import config, asyncio
import utils.database

class CustomWikiBot(commands.AutoShardedBot):
    async def on_ready(self):
        print(f"Login {self.user}\nStarting Discord Bot.")
    
    def __init__(self):
        intent = disnake.Intents.default()
        intent.members = True
        intent.presences = True
        super().__init__(commands.when_mentioned_or(*config.PREFIX), intent=intent, shard_count=8)
        self.remove_command("help")
        for extension in config.EXTENSION_LIST:
            self.load_extension(extension)
        asyncio.run(utils.database.create_wiki_table())

bot = CustomWikiBot()
bot.run(config.BOT_TOKEN)