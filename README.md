# Discord_bot

This bot can give the real-time data of NEPSE.
<br/>You can use this bot in your server to get details of certain scripts, top gainers or losers or status of NEPSE.


## USER MANUAL
* command: **!hello**<br/>description: Greet User

* command: **!status**<br/>description: Return Current Status of Nepse 

* command: **!gainers**<br/>description: Returns the top 10 gainers of the market currently. 

* command: **!losers**<br/>description: Returns the top 10 losers of the market currently. 

* command: **!script** *SYMBOL*<br/>description: Returns the details of the company. Symbol is the abbreviation of the company.



## KEEP BOT RUNNING CONTINUOUSLY
If the bot is running on your PC and you close your PC the bot will stop running.
<br/>In order to run the bot continuously you can use repl.it to run your code. 
<br/>Using the keep_alive module you can create a server that runs the code even after the PC is closed.
<br/>But the webserver will only run the code till one hour without any use.
<br/>So, to keep the webserver and bot running you can use [Uptime-Robot](https://uptimerobot.com/) to ping the server for every five minutes.
<br/>With continuous pings, the bot will never close and keep running continuously.

