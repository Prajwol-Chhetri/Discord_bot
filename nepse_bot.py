import os
import discord
# from keep_alive import keep_alive
from check_time import check_time

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


client.run('')


""" remove comment when deploying real time """
# keep_alive()
# client.run(token)


