#bot.py

import os
from scraper import *

import discord
from dotenv import load_dotenv

import asyncio



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#global variable to store results of 538 scrape
results = {}

#generator that works with the 538 timer to query the site every 15 minutes and store the results in the "result" list


@client.event
async def on_message(message):
    author_name = str(message.author)
    input = message.content.lower()

    #prevents bot from responding to itself
    if message.author == client.user:
        return


    if input == 'forecast!':
        results = scrape()

        biden_wins = "Biden: {biden}%\n".format(biden = results.get('Biden', 0))
        trump_wins = "Trump: {trump}%\n".format(trump = results.get('Trump', 0))
        tie_wins = "Tie: {tie}%".format(tie=results.get('no majority', 0))
        embed = discord.Embed(color=0x0000FF)
        embed.set_thumbnail(url = "https://media.giphy.com/media/3o6ozEVrEqZbHHz81G/giphy.gif")
        embed.description = biden_wins + trump_wins + tie_wins

        await message.channel.send(embed=embed)
        await asyncio.sleep(3)
        await message.channel.send("{trump}% chances are not unheard of. Don't forget to vote!.".format(trump=results.get('Trump',0)))
    if input == 'help!':
        await message.channel.send('What up franz. \nType \"forecast!\" to get the current presidential chances from FiveThirtyEight')

    if input == '"forecast!"':
        await message.channel.send("Without the quotation marks!")

    if input == 'thank you bot':
        await message.channel.send(f'You\'re welcome, {author_name[:-5]}')




client.run(TOKEN)

