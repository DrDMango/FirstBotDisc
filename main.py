
#{author.mention} is to ping the person who talked
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Your Bot Is Ready"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()

import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
intents=intents = discord.Intents.all()


@client.event
async def on_ready():
    print(f'{client.user.name} is online Discord!')
    print(client.guilds)
    for guild in client.guilds:
        if guild.name == GUILD:
            break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
          )
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')
@client.event
async def on_member_join(member):
    print("Yay! {member.name} has joined!")
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the DrDMango Discord Server!!'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    help = [
        'If you want to make BloopBlap say hi to you, do .hello . If you\'re bored and you want BloopBlap to tell you what to do, do .wtd . If you want BloopBlap to flip a coin for you, do .flipcoin . If you wnat BloopBlap to roll a Magic 8 Ball, do .8ball . Thank you for using BloopBlap.',

    ]

    if message.content == '.help':
        response = random.choice(help)
        await message.channel.send(response)

    whattodo = [
        'Make a youtube channel!',
        'Subscribe to DrDMango!',
        'Play a sport!',
        'Play a video game!',
        'Read a book!',
        'Drink a drink!',
        'Eat some food!',
        'Explore your area!',
        'Do your homework!',
        'Talk with your friends!',
        'Talk to your family!',
        'Watch some TV!',
        'Enjoy the sunshine -- or moonlight!',
        'Write a little jig!',
        'Dance to your favorite song!',
        'Play some music!',
        'Sing along to your favorite song!',
        'Make a Discord bot!',
        'Go to your local park!',
        'Error: Syntax Error on Line 34: f\'Hi {member.na__m__}, welcome to the DrDMango Discord Server!!',
        'Eat a snack!',
        'Eat a halo!',
        'Scroll a social media platform!',
        ':sob:',
        'Play or learn an instrument!',
        'Draw something cool!',
        'Eat some *Fanta* or *Pepsi*!'
    ]

    if message.content == '.wtd':
        response = random.choice(whattodo)
        await message.channel.send(response)
    else:
      response = "idk man"
    hello = [
        'Hello!',
        'How are you?',
        'Hi!',
        'What\'s up?',
        'Hello! How are you?',
        'Heyheyhey! What\'s going on?',
        'Hullo!',
        'Hello! What\'s up?',
        'Hmm... you\' being suspiciously nice to me today...',
        'Hey, hello!',
        'Hola!',
        '...hi...',
        'Hello!!!!',
        'What\'s going on dude! Hello!',
        'print ("hello")',
        'Namaskar',
        'Hola Amigo! Soy Dora!',
        '***__~~||HELLO!!!!!||~~__***',
        '```HELLO!!!!!```',
    ]

    if message.content == '.hello':
        response = random.choice(hello)
        await message.channel.send(response)
    else:
      response = "idk man"
    flipcoin = [
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        'Heads!',
        'Tails!',
        '...it landed on the side...',
        '... I don\'t know. I really don\'t know'
    ]

    if message.content == '.flipcoin':
        response = random.choice(flipcoin)
        await message.channel.send(response)
    else:
      response = "idk man"
    magic8Ball = [
        'Yes!',
        'No...',
        'It is so.',
        'Most definitely.',
        ':100:',
        'Don\'t count on it...',
        'Nope, sorry :(',
        'Not gonna happen :/',
        'It is certain',
        'It is uncertain',
        'It is decidedly so.',
        'Concentrate and ask again.',

    ]

    if message.content == '.8ball':
        response = random.choice(magic8Ball)
        await message.channel.send(response)
    else:
      response = "idk man"
    emoji = [
      ':flushed:',
      ':sob:',
      ':smiley:',
      ':cry:',
      ':zany_face:',
      ':skull:',
      ':clown:',
      ':fleur_de_lis:',
      ':rage:',
      ':unamused:',
      ':smirk:',
      ':triumph:',
      ':rolling_eyes:',



    ]

    if message.content == '.emoji':
        response = random.choice(emoji)
        await message.channel.send(response)

        
    
    

client.run(TOKEN)
