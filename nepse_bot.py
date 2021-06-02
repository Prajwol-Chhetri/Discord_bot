# import os
import discord
# from keep_alive import keep_alive
from market_details import market_status, get_live_script
# from ss_scraper import get_script_detail
import nepali_datetime

client = discord.Client()


# token = os.environ['discord_token']
now = nepali_datetime.datetime.now()
current_date = nepali_datetime.date.today()
current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")

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

    if "summary" in msg:
        nepse = market_status()[0]
        if nepse["point-change"] < 0:
            await message.channel.send(f'{nepse["status"]} with a loss of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
        elif nepse["point-change"] > 0:
            await message.channel.send(f'{nepse["status"]} with a gain of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
        else:
            await message.channel.send(f'{nepse["status"]} \nNEPSE Index = {nepse["index"]} \nPoint Change = {nepse["point-change"]} \nPercent Change = {nepse["percent-change"]}')

    if "gainers" in msg:
        top_gainers = market_status()[2]
        await message.channel.send(f'The top gainers are: \n{top_gainers}')

    if "losers" in msg:
        top_losers = market_status()[1]
        await message.channel.send(f'The top losers are: \n{top_losers}')

    if msg.startswith("$script"):
        symbol = msg.split("$script ", 1)[1]
        nepse = market_status()[0]
        if nepse["status"] == "Market Open":
            company = get_live_script(symbol.upper())
            await message.channel.send(f'{company["company"]} \nAs of {current_date} {current_time} \nLTP = {company["LTP"]} \nOpening Price = {company["open"]} \nPrevious Close = {company["previous-close"]} \nToday\'s Highest Price = {company["high"]} \nToday\'s Lowest Price = {company["low"]} \nChange = {company["change"]}%')
        else:
            # company = get_script_detail(symbol.upper())
            # await message.channel.send(f'{company["company"]} \nAs of {current_date} {current_time} \nOpening Price = {company["open"]} \nPrevious Close = {company["previous close"]} \nToday\'s Highest Price = {company["high"]} \nToday\'s Lowest Price = {company["low"]} \nChange = {company["change"]}%')
            await message.channel.send('Market Closed')

client.run('')

""" remove comment when deploying real time """
# keep_alive()
# client.run(token)
