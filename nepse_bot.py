# import os
import discord
from discord.ext import commands
# from keep_alive import keep_alive
from market_details import market_status, get_live_script, gainers, losers
from ss_scraper import get_script_detail
import nepali_datetime

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


# token = os.environ['discord_token']
now = nepali_datetime.datetime.now()
current_date = nepali_datetime.date.today()
current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message_join(member):
    channel = client.get_channel('')
    embed = discord.Embed(title=f"Welcome {member.name}",
                          description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
    embed.set_thumbnail(url=member.avatar_url)  # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('hello'):
        await message.channel.send(f'Hello! {message.author.name}')

    if "status" in msg:
        try:
            nepse = market_status()
            if nepse["point-change"] < 0:
                await message.channel.send(
                    f'{nepse["status"]} with a loss of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
            elif nepse["point-change"] > 0:
                await message.channel.send(
                    f'{nepse["status"]} with a gain of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
            else:
                await message.channel.send(
                    f'{nepse["status"]} \nNEPSE Index = {nepse["index"]} \nPoint Change = {nepse["point-change"]} \nPercent Change = {nepse["percent-change"]}')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')

    if "gainers" in msg:
        try:
            top_gainers = gainers()
            await message.channel.send(f'The top gainers are: \n{top_gainers}')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')

    if "losers" in msg:
        try:
            top_losers = losers()
            await message.channel.send(f'The top losers are: \n{top_losers}')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')

    if msg.startswith("$script"):
        try:
            symbol = msg.split("$script ", 1)[1]
            nepse = market_status()
            if nepse["status"] == "Market Open":
                company = get_live_script(symbol.upper())
                await message.channel.send(
                    f'{company["company"]} \nAs of {current_date} {current_time} \nLTP = {company["LTP"]} \nOpening Price = {company["open"]} \nPrevious Close = {company["previous-close"]} \nToday\'s Highest Price = {company["high"]} \nToday\'s Lowest Price = {company["low"]} \nChange = {company["change"]}%')
            else:
                company = get_script_detail(symbol.upper())
                await message.channel.send(
                    f'{company["company"]} \nAs of {current_date} {current_time} \nOpening Price = {company["open"]} \nPrevious Close = {company["previous close"]} \nToday\'s Highest Price = {company["high"]} \nToday\'s Lowest Price = {company["low"]} \nChange = {company["change"]}%')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')
        except TypeError:
            await message.channel.send(
                'We could not find the script. Please make sure you type in the symbol correctly')


client.run('')

""" remove comment when deploying real time """
# keep_alive()
# client.run(token)
