"""The main bot bot module."""
import discord
import asyncio
from dist import token
from dnd import DND

bot = discord.bot()
print(f"Current discord.py version: {discord.__version__}")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
    await bot.say(f'{member} joined at {member.joined_at}')


@bot.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await bot.send_message(
            message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await bot.edit_message(tmp, f'You have {counter} messages.')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await bot.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!update'):
        await bot.send_message(message.channel, 'Update test.')
    elif message.content.startswith('!wiki'):
        await bot.send_message(
            message.channel, 'Wiki search results: ')
    await bot.process_commands(message)

bot.run(token)
