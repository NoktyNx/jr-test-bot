"""The main bot module."""
import logging
import discord
import context
import dist

print(f"Current discord.py version: {discord.__version__}")

log = logging.getLogger(__name__)


class DNDBot(discord.Client):  # discord.AutoShardedBot
    def __init__(self):
        super().__init__()

        self.client_id = dist.client_id
        self.token = dist.token
        self.postgresql = dist.postgresql  # future implementation

    async def on_ready(self):
        print('Logged in.')
        print('------')
        print(f'User: {self.user}\n')
        print(f'ID: {self.user.id}')
        print('------')

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=context.Context)

        if ctx.command is None:
            return

        async with ctx.acquire():
            await self.invoke(ctx)


@property
def config(self):
    return __import__('config')
