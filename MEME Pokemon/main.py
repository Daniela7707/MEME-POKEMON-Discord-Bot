import discord
from discord.ext import commands
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


def get_pokemon_image_url():
    pokemon_id = random.randint(1, 1025)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'

    res = requests.get(url)
    data = res.json()

    return data['sprites']['front_default']


@bot.command()
async def pokemon(ctx):
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)

bot.run(TOKEN) 