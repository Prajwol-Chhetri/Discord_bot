# IMPORTING THE REQUIRED MODULES FOR THIS BOT
import discord
from keep_alive import keep_alive
from market_details import market_status, get_live_script, gainers, losers
import nepali_datetime

# Giving privilege to the bot to see members entering the server.
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# creating a now object of nepali_datetime class to give the current time.
now = nepali_datetime.datetime.now()

# user manual containing detail of commands and their description
manual = '__**USER MANUAL**__ \ncommand: **!hello** \ndescription: Greet User \n\ncommand: **!status** \ndescription: Return Current Status of Nepse \n\ncommand: **!gainers** \ndescription: Returns the top 10 gainers of the market currently. \n\ncommand: **!losers** \ndescription: Returns the top 10 losers of the market currently. \n\ncommand: **!script** *SYMBOL* \ndescription: Returns the details of the company. Symbol is the abbreviation of the company.'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# this function sends private message to the user joining the server with the manual and welcomes the user in the channel.
@client.event
async def on_member_join(member):
    channel = client.get_channel('Your Channel ID here')
    public_embed = discord.Embed(title=f"Welcome {member.name}",
                                 description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
    public_embed.set_thumbnail(url=member.avatar_url)  # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=public_embed)

    private_embed = discord.Embed(
        title=f"Thanks for joining {member.guild.name}\nYou can see the commands to get started below:",
        description=f"\n{manual}")  # F-Strings!
    await member.send(embed=private_embed)


@client.event
async def on_message(message):
    # This condition prevents the bot to responding to itself.
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!hello'):
        await message.channel.send(f'Hello! {message.author.name}')

    if "!help" in msg:
        await message.channel.send(manual)

    if "!status" in msg:
        try:
            current_date = nepali_datetime.date.today()
            current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")
            nepse = market_status()
            if nepse["point-change"] < 0:
                await message.channel.send(
                    f'As of {current_date} {current_time} \n{nepse["status"]} with a loss of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
            elif nepse["point-change"] > 0:
                await message.channel.send(
                    f'As of {current_date} {current_time} \n{nepse["status"]} with a gain of {nepse["point-change"]} points.\nNEPSE Index = {nepse["index"]} \nPercent Change = {nepse["percent-change"]}')
            else:
                await message.channel.send(
                    f'As of {current_date} {current_time} \n{nepse["status"]} \nNEPSE Index = {nepse["index"]} \nPoint Change = {nepse["point-change"]} \nPercent Change = {nepse["percent-change"]}')
        except (ConnectionError, TimeoutError) as error:
            await message.channel.send('We could not establish connection with server please try again')

    if "!gainers" in msg:
        try:
            current_date = nepali_datetime.date.today()
            current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")
            top_gainers = gainers()
            await message.channel.send(f'As of {current_date} {current_time} \nThe top gainers are: \n{top_gainers}')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')

    if "!losers" in msg:
        try:
            current_date = nepali_datetime.date.today()
            current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")
            top_losers = losers()
            await message.channel.send(f'As of {current_date} {current_time} \nThe top losers are: \n{top_losers}')
        except ConnectionError:
            await message.channel.send('We could not establish connection with server please try again')

    if msg.startswith("!script"):
        try:
            current_date = nepali_datetime.date.today()
            current_time = (nepali_datetime.datetime.time(now)).strftime("%I:%M%p")
            symbol = msg.split("!script ", 1)[1]
            await message.channel.send('Please wait fetching the details of the script')
            company = get_live_script(symbol.upper())
            if company is None:
                await message.channel.send(
                    'We could not find the script. Please make sure you type in the symbol correctly')
            else:
                await message.channel.send(
                    f'{company["company"]} \nAs of {current_date} {current_time} \nLTP = {company["LTP"]} \nOpening Price = {company["open"]} \nPrevious Close = {company["previous-close"]} \nToday\'s Highest Price = {company["high"]} \nToday\'s Lowest Price = {company["low"]} \nChange = {company["change"]}%')
        except (ConnectionError, TimeoutError) as error:
            await message.channel.send('We could not establish connection with server please try again')


keep_alive()
client.run('Your_Bot_Token_Here')
