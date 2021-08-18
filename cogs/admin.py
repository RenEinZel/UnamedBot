import discord
from discord.ext import commands
from global_check.check import *

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @owner()
    @commands.command()
    async def unload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send("Could Not Load Cog", delete_after=5)
            return
        await ctx.send("Cog Unloaded", delete_after=5)

    @owner()
    @commands.command()
    async def load(self, ctx, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could Not Load Cog", delete_after=5)
            return
        await ctx.send("Cog loaded", delete_after=5)

    @owner()
    @commands.command()
    async def reload(self, ctx, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send("Could Not Reload Cog", delete_after=5)
            return
        await ctx.send("Cog Reloaded", delete_after=5)


    
    
def setup(bot):
    bot.add_cog(Admin(bot))
