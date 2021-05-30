import os
import discord
# from keep_alive import keep_alive
from check_time import check_time
from market_details import summary, top_gainers, top_losers

client = discord.Client()


# token = os.environ['discord_token']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if "status" in message.content:
        if check_time():
            await message.channel.send('Market is currently open')
        else:
            await message.channel.send('Market is currently closed')

    if "summary" in message.content:
        summary()
        await message.channel.send(f'Top gainers are:\n{top_gainers}')
        await message.channel.send(f'Top losers are:\n{top_losers}')


client.run('')

""" remove comment when deploying real time """
# keep_alive()
# client.run(token)
