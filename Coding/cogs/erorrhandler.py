import discord 
import global_check.check

from discord.ext import commands
from datetime import timedelta



class CommandErrorHandler(commands.Cog):
    # setup
    def __init__(self, bot):
        self.bot = bot
        bot.on_command_error = self._on_command_error

    # handler
    async def _on_command_error(self, ctx, error, bypass=False):
        print(error)
        if (hasattr(ctx.command, "on_error") or (ctx.command and hasattr(
                ctx.cog, f"_{ctx.command.cog_name}__error")) and not bypass):
            return

        if isinstance(error, commands.CommandNotFound):
            notfound = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
            notfound.set_author(name='Error:NotFound')
            notfound.add_field(name='Sorry, I Don\'t See The Command You Entered :(',
                               value='Be Sure To Check Commands I Have!', inline=False)
            return await ctx.send(embed=notfound, delete_after=10)

        elif isinstance(error, commands.MissingRequiredArgument):
            arg = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
            arg.set_author(name='Error:MissingArgument')
            arg.add_field(name='Sorry, You Forgot An Argument :(', value=f'Missing: `{error.param}`', inline=False)
            return await ctx.send(embed=arg, delete_after=10)

        elif isinstance(error, commands.CommandOnCooldown):
            if ctx.author.id == (ctx.owner_id):
                await ctx.reinvoke()
                return
            if (ctx.author.id != ctx.owner_id):
                time_wait = timedelta(seconds=float(f'{error.retry_after:.2f}'))
                cooldown_embed = discord.Embed(color=0xff0000, timestamp=ctx.message.created_at)
                cooldown_embed.set_author(name='Error:Cooldown')
                cooldown_embed.add_field(name='Sorry, You Are On Cooldown:',
                                         value=':clock2: Remaining Time: `{}`'.format(time_wait), inline=False)
                return await ctx.send(embed=cooldown_embed, delete_after=10)

        elif isinstance(error, commands.CheckFailure):
            if isinstance(error, global_check.check.OwnerOnly):
                pass
            elif isinstance(error, global_check.check.NSFWOnly):
                pass
            elif isinstance(error, global_check.check.MainGuildOnly):
                pass
            elif isinstance(error, global_check.check.BanPermOnly):
                pass
            elif isinstance(error, global_check.check.KickPermOnly):
                pass
            elif isinstance(error, global_check.check.DelMessagesPermOnly):
                pass


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))

