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
result = []

#generator that works with the 538 timer to query the site every 15 minutes and store the results in the "result" list
async def background_scrape():
        result = scrape()
        for i in result:
            yield i

async def five_thirty_eight_timer():
    await client.wait_until_ready()
    while not client.is_closed():
        async for i in background_scrape():
            result.append(i)
        await asyncio.sleep(900)


@client.event
async def on_message(message):
    author_name = str(message.author)
    input = message.content.lower()

    #prevents bot from responding to itself
    if message.author == client.user:
        return


    if input == 'forecast!':
        await message.channel.send("Biden: " + result[-1] + "%" + "\nTrump: " + result[-2] + "%")

    if input == 'help!':
        await message.channel.send('What up franz. \nType \"forecast!\" to get the current presidential chances from FiveThirtyEight')

    if input == '"forecast!"':
        await message.channel.send("Without the quotation marks!")

    if input == 'hello bot':
        await message.channel.send(f'Hi, {author_name[:-5]}')



client.loop.create_task(five_thirty_eight_timer())
client.run(TOKEN)

