import discord
import time
import asyncio


from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='ping')
    @commands.cooldown(1.0, 5.0,)
    async def _ping(self, ctx):
        msg = ctx.message
        reply_to_ping = msg.author
        start = time.perf_counter()
        checkping = await msg.channel.send('Checking Ping...')
        end = time.perf_counter()
        duration = (end - start) * 1000
        pingcheck_embed = discord.Embed(
            colour = discord.Colour.green()
        )
        await asyncio.sleep(1)
        pingcheck_embed.set_author(name=f'PingCheck')
        pingcheck_embed.add_field(name='Ping', value='{:.2f}ms'.format(duration), inline=False)
        pingcheck_embed.set_footer(text='Replying To {}'.format(reply_to_ping))
        await msg.channel.send(embed=pingcheck_embed)
        await checkping.delete()
        pass


    @commands.command(name='hello')
    async def _hello(self, ctx):
        await ctx.send("Hello, I am a robot... Yeah.... Dont Ask Me Why")


    @commands.command(name='checkperms')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _checkperms(self, ctx, *, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, color=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))
        embed.add_field(name='Permissions:', value=perms)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Basic(bot))
