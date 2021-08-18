import discord
import random

from discord.ext import commands
from global_check.check import *

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='dice')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _dice(self, ctx, Bet):
        try:
            reply_to = ctx.message.author
            dice = random.randint(1, 6)
            if dice == 1:
                roll = '1 ⚀'
            if dice == 2:
                roll = '2 ⚁'
            if dice == 3:
                roll = '3 ⚂'
            if dice == 4:
                roll = '4 ⚃'
            if dice == 5:
                roll = '5 ⚄'
            if dice == 6:
                roll = '6 ⚅'
            if int(Bet) == dice:
                result = 'Won :)'
            if int(Bet) != dice:
                result = 'Lost :('
            dice_roll_embed = discord.Embed(
                colour=discord.Colour.blue()
            )
            dice_roll_embed.set_author(name='DiceRollResult')
            dice_roll_embed.add_field(name=f'You {result}', value='Roll:`{}`'.format(roll), inline=False)
            dice_roll_embed.set_footer(text='Replying To {}'.format(reply_to))
            await ctx.send(embed=dice_roll_embed)
        except Exception:
            return

    @commands.command(name='slots')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _slots(self, ctx):
        reply_to = ctx.message.author
        abc_list = ['`1`',
                    '`2`',
                    '`3`', ]

        a = random.choice(abc_list)
        b = random.choice(abc_list)
        c = random.choice(abc_list)
        x = str(a) + ' ' + str(b) + ' ' + str(c)

        slots_embed_lose = discord.Embed(
            colour=discord.Colour.red()
        )
        slots_embed_lose.set_author(name='Roll Result')
        slots_embed_lose.add_field(name='You Lost...', value='{}'.format(x), inline=False)
        slots_embed_lose.set_footer(text='Replying To {}'.format(reply_to))

        slots_embed_win = discord.Embed(
            colour=discord.Colour.green()
        )
        slots_embed_win.set_author(name='Roll Result')
        slots_embed_win.add_field(name='You Won!', value='{}'.format(x), inline=False)
        slots_embed_win.set_footer(text='Replying To {}'.format(reply_to))

        if a == b == c:
            winner_role = discord.utils.get(ctx.message.guild.roles, name='Slots_Winner :)')
            winner = ctx.message.author
            userID = ctx.message.author.id
            await ctx.send(embed=slots_embed_win)
            await winner.add_roles(winner_role)
            await ctx.send(
                'Congratulations <@%s>! You Have Successfully Acquired A Role For Your Victory! Have Fun! :3' % (
                    userID))
        else:
            await ctx.send(embed=slots_embed_lose)        




def setup(bot):
    bot.add_cog(Fun(bot))
