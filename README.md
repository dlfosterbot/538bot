# 538bot
Update 03/20/21: 

Requests and stores 538 presidential forecast odds and returns them to a discord server using a bot. Scraper.py refers to [https://projects.fivethirtyeight.com/2020-election-forecast/us_simulations.json]. There are 100 simulations. Scraper creates a dictionary with two keys: Biden and Trump. Value is the number of wins (out of 100). That value corresponds to the percentage likelihood that the candidate will win the 2020 election. 
 
Use .env to store bot token and server information.

Follow [Discord's documentation](https://discordpy.readthedocs.io/en/latest/discord.html) and use "!forecast."