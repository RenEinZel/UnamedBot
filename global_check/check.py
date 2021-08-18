import discord
import os

from discord.ext import commands


class NSFWOnly(commands.CheckFailure):
    pass
class OwnerOnly(commands.CheckFailure):
    pass
class MainGuildOnly(commands.CheckFailure):
    pass
class KickPermOnly(commands.CheckFailure):
    pass
class BanPermOnly(commands.CheckFailure):
    pass
class DelMessagesPermOnly(commands.CheckFailure):
    pass

def owner():
    async def predicate(ctx):
        if ctx.message.author.id == 340142066128388096:
            return True
        else:
            raise OwnerOnly()
    return commands.check(predicate)


def banperm():
    async def predicate(ctx):
        if 'ban_members' in get_perms(ctx.author):
            return True
        else:
            raise BanPermOnly()
    return commands.check(predicate)


def kickperm():
    async def predicate(ctx):
        if 'kick_members' in get_perms(ctx.author):
            return True
        else:
            raise KickPermOnly()
    return commands.check(predicate)


def clearperm():
    async def predicate(ctx):
        if 'manage_messages' in get_perms(ctx.author):
            return True
        else:
            raise DelMessagesPermOnly()
    return commands.check(predicate)


def get_perms(user):
    return (' '.join(perm for perm, value in user.guild_permissions if value).split())