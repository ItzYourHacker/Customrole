from __future__ import annotations
import discord
from discord.ext import commands
import os 
os.system("pip install jishaku && pip install discord && pip install aiosqlite")
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"
import aiosqlite
import asyncio
import logging

token =""

logging.basicConfig(level=logging.INFO,format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",datefmt="%H:%M:%S",)
logger = logging.getLogger("__name__")

class Oxytech(commands.AutoShardedBot):
  def __init__(self) -> None:
    super().__init__(command_prefix =commands.when_mentioned_or("-"),case_insensitive=True, intents=discord.Intents.all(),strip_after_prefix=True)

  async def setup_hook(self) -> None:   
    initial_extensions = ['jishaku']

    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])
############################################################
        
    for extension in initial_extensions:
        await self.load_extension(extension)
        logger.info(f"Loaded Extension [{extension}]")
    await self.tree.sync()
#########################################################  
  async def on_connect(self):
    await self.change_presence(status=discord.Status.dnd,
                               activity=discord.Activity(                             type=discord.ActivityType.streaming,
                                 name='-help'))


      
  async def config_db(self):
    setattr(custom,"config", await aiosqlite.connect("db/config.db"))
    async with custom.config.cursor() as cursor:
      await cursor.execute("""CREATE TABLE IF NOT EXISTS config (
          guild BIGINT,
          staff BIGINT DEFAULT 0,
          vip BIGINT DEFAULT 0,
          girl BIGINT DEFAULT 0,
          guest BIGINT DEFAULT 0,
          friend BIGINT DEFAULT 0,
          reqrole BIGINT DEFAULT 0)""")
      logger.info("Loaded config db")
       


custom = Oxytech()
custom.owner_ids = [289100850285117460]

@custom.event
async def on_ready():     
    logger.info("Loaded & Online!")
    logger.info(f"Logged in as: {custom.user}")
    logger.info(f"Connected to: {len(custom.guilds)} guilds")
    logger.info(f"Connected to: {len(custom.users)} users")
        


async def main():
    await custom.config_db()
    await custom.start(token)


asyncio.run(main())
