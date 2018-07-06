"""The main bot module."""
import inspect
import logging
import discord
from discord.ext import commands
import dist
from dnd import dnd
from roller import roller

print(f"Current discord.py version: {discord.__version__}")
log = logging.getLogger(__name__)


class DNDBot(commands.Bot):
    def __init__(self, loop):
        super().__init__(command_prefix=["!", "/"], loop=loop,
                         token=dist.token)

        self.client_id = dist.client_id
        self.postgresql = dist.postgresql  # future implementation

        dnd_members = inspect.getmembers(dnd)
        for name, member in dnd_members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

        roller_members = inspect.getmembers(roller)
        for name, member in roller_members:
            if isinstance(member, commands.Command):
                if member.parent is None:
                    self.add_command(member)

    async def on_ready(self):
        print('------')
        print('Bot activated and logged in.')
        print('------')
        print(f'Bot User: {self.user}\n')
        print(f'Bot User ID: {self.user.id}')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)


@property
def config(self):
    return __import__('dist')
