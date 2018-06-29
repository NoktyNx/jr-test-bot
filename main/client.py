"""The main bot client module."""
import discord
import asyncio
from dist import token
import wiki  # Implement this based on !wiki "search_string"

bot = discord.Client()
print(f"Current discord.py version: {discord.__version__}")

@bot.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
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
        tmp = await client.send_message(
        message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, f'You have {counter} messages.')
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!update'):
        await client.send_message(message.channel, 'Update test.')
    await bot.process_commands(message)

bot.run(token)
