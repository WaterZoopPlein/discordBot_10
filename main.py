import os

import requests
from discord.ext import commands

import numberText.numberText as Num
from inspiroError import *

bot = commands.Bot(command_prefix='=')


@bot.event
async def on_ready():
    print("Bring it on.")


@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)} ms')


@bot.command()
async def inspire(ctx):
    try:
        r = requests.get("https://inspirobot.me/api?generate=true")
    except Exception as e:
        raise InspiroError(str(e))
    if r.status_code != 200:
        raise InspiroError("API request failed. Invalid response code ({})".format(r.status_code))
    await ctx.send(r.text)


@bot.command()
async def verbose(ctx, *number):
    try:
        num_text = Num.num_to_text(int(number[0]))
        await ctx.send(f"{num_text}")
    except Exception as e:
        await ctx.send(f"{str(e)}")


token = os.getenv('DISCORD_BOT_TOKEN')
bot.run(token)
