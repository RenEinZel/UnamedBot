import discord
import time
import sys
import os

from discord.ext import commands
from datetime import datetime

status = discord.Status

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _userinfo(self, ctx, *, user: discord.Member = None):
        global user_avatar, user_device, user_status_output
        reply_to = ctx.message.author
        if (user is None or user == None):
            user = ctx.message.author
        user_status = str(user.status)
        print(user_status)
        if user_status == 'online':
            user_status_output = ':grinning:  Online'
        if user_status == 'idle':
            user_status_output = ':sleeping: Idle'
        if user_status == 'dnd':
            user_status_output = '⛔ DoNotDisturb'
        if user_status == 'offline':
            user_status_output = '✖️Offline/Invisible'
        roles = []
        for r in user.roles:
            roles.append(r.name)
        user_roles = ", ".join(roles)
        user_nick = user.nick
        user_color = user.color
        user_toprole = user.top_role
        user_server = user.guild
        user_joined = user.joined_at
        user_created = user.created_at
        if user.is_avatar_animated() is True:
            user_avatar = user.avatar_url_as(format='gif')
        if user.is_avatar_animated() is False:
            user_avatar = user.avatar_url_as(format='png')
        if user.is_on_mobile() is True:
            user_device = ':iphone:Mobile'
        if user.is_on_mobile() is False:
            user_device = ':desktop:Desktop/Web'
        embed_info = discord.Embed(color=user_color)
        embed_info.set_author(name='{}\'s Info'.format(user.display_name))
        embed_info.set_thumbnail(url=user_avatar)
        embed_info.add_field(name='CreatedAt', value='{}'.format(user_created), inline=False)
        embed_info.add_field(name='Nickname', value='{}'.format(user_nick), inline=False)
        embed_info.add_field(name='Avatar', value='[Link]({})'.format(user_avatar), inline=False)
        embed_info.add_field(name='Status', value='{}'.format(user_status_output), inline=False)
        embed_info.add_field(name='Device', value='{}'.format(user_device), inline=False)
        embed_info.add_field(name='Server', value='{}'.format(user_server), inline=False)
        embed_info.add_field(name='JoinedServerAt', value='{}'.format(user_joined), inline=False)
        embed_info.add_field(name='Top_Role', value='{}'.format(user_toprole), inline=False)
        embed_info.add_field(name='Roles', value='{}'.format(user_roles), inline=False)
        embed_info.add_field(name='Color', value='{}'.format(user_color), inline=False)
        embed_info.set_footer(text='Replying To {}'.format(reply_to))
        await ctx.send(embed=embed_info)

    @commands.command(name='serverinfo')
    @commands.cooldown(1.0, 5.0, commands.BucketType.user)
    async def _serverinfo(self, ctx):
        reply_to = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.guild
        server_name = server.name
        server_region = server.region
        server_id = server.id
        server_roles_amount = len(server.roles)
        server_emotes_amount = len(server.emojis)
        server_members_amount = server.member_count
        server_online = str(sum(1 for member in server.members if member.status!=status.offline))
        server_created_at = server.created_at
        image = server.icon_url_as(format='png')
        server_info_embed = discord.Embed(color=0x7fffff)
        server_info_embed.set_thumbnail(url=image)
        server_info_embed.set_author(name='Server Info')
        server_info_embed.add_field(name='Name', value='{}'.format(server_name), inline=False)
        server_info_embed.add_field(name='Region', value='{}'.format(server_region), inline=False)
        server_info_embed.add_field(name='ID', value='{}'.format(server_id), inline=False)
        server_info_embed.add_field(name='Owner', value='{}'.format(ctx.guild.owner), inline=False)
        server_info_embed.add_field(name='MembersAmount', value='All:`{}`\nOnline:`{}`'.format(server_members_amount, server_online), inline=False)
        server_info_embed.add_field(name='EmojiAmount', value='{}'.format(server_emotes_amount), inline=False)
        server_info_embed.add_field(name='RolesAmount', value='{}'.format(server_roles_amount), inline=False)
        server_info_embed.add_field(name='CreatedAt', value='{}'.format(server_created_at), inline=False)
        server_info_embed.add_field(name='Image', value=f'[Link]({image})', inline=False)
        server_info_embed.set_footer(text='Replying To {}'.format(reply_to))
        await channel.send(embed=server_info_embed)

    


def setup(bot):
    bot.add_cog(Info(bot))

