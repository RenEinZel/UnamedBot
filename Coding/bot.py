import discord
import os
import asyncio
import traceback

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('.env')
Code = os.getenv('KEYS')
bot = commands.Bot(os.getenv('PREFIX'), 
                    intents=discord.Intents(
                        members=True, guilds=True, presences=True, typing=True, messages=True, reactions=True
                    ) 
                )


@bot.event
async def on_ready():
    print('Loading......')
    await asyncio.sleep(3)
    for filename in os.listdir("./cogs"):
        try:
            if filename.endswith(".py") and filename != "__init__.py":
                bot.load_extension(f'cogs.{filename[:-3]}')
                print('Succesfully Load {} Cogs!'.format(filename))
        except Exception as e:
            print('Cog {} Not loaded!'.format(filename))
            traceback.print_exc()
            return
    await asyncio.sleep(3)
    print('Assistant Bot Is Ready To Assist!')
    print('#################################')
    

bot.run(Code)


