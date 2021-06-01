# import os
import discord
# from keep_alive import keep_alive
from market_details import market_status, get_script_detail

client = discord.Client()


# token = os.environ['discord_token']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('hello'):
        await message.channel.send('Hello!')

    if "status" in msg:
        if market_status():
            await message.channel.send('Market is currently open')
        else:
            await message.channel.send('Market is currently closed')

    if msg.startswith("$script"):
        symbol = msg.split("$script ", 1)[1]
        if market_status():
            company = get_script_detail(symbol.upper())
            await message.channel.send(f'{company}')
        else:
            await message.channel.send(f'Sorry cannot get details of {symbol.upper()} as market is currently closed')



client.run('')

""" remove comment when deploying real time """
# keep_alive()
# client.run(token)
