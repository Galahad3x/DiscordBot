# bot.py
import os
from dotenv import load_dotenv
import random

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('PIBOT_TOKEN')

# 2
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
	print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="99", help="Respon amb :100:")
async def nine_nine(ctx):
	await ctx.send(":100:")

@bot.command(name="coin", help="Juga a cara o creu")
async def cara_o_creu(ctx):
	sol = random.choice([True, False])
	if sol:
		missatge = "Ha sortit cara! :thumbsup:"
	else:
		missatge = "Ha sortit creu! :flushed:"
	await ctx.send(missatge)


bot.run(TOKEN)
