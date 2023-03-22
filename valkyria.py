"""Valkyria bot client"""
import logging
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def cafe(ctx):
    await ctx.send("True random: " + random.choice(["EH", "Waynes", "3G"]))

bot.run(os.environ.get("VALKYRIA_BOT_KEY"))
