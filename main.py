from cProfile import run
from http import client
import os, discord, time
from urllib import response
from dotenv import load_dotenv
import handleDogAPI as hdapi

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # print('We have logged in as')


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]

    if message.author == client.user:
        return
    
    # if ((message.channel == "dog-bot") or (message.channel == "test-bot")):
    if ((message.channel == "dog-bot")):
        return


    if message.content.startswith('$hello dogbot'):
        time.sleep(2)
        await message.channel.send(f'Hello! {username} 😸')



    if message.content.startswith('$give me dog picture'):
        time.sleep(2)
        await message.channel.send(f'here you go')
        await message.channel.send(hdapi.getdog())




    if message.content.startswith('$commands'):
        time.sleep(2)
        await message.channel.send('my commands are:')
        await message.channel.send("$hello dogbot")
        await message.channel.send("$give me dog picture")


client.run(os.getenv('TOKEN'))

