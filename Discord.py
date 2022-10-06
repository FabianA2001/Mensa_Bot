import Token

import discord
from discord.ext import commands
from discord.ext import tasks as discordTasks
from datetime import datetime as dt

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
hour = 22


@discordTasks.loop(minutes=10)
async def messageDaily():
    if dt.now().hour == hour:

        await dm_task()


async def dm_task():
    await bot.wait_until_ready()
    channel = await bot.fetch_user(Token.ID)
    if channel == None:
        print("Das ist die falsche channel id")
    else:
        await channel.send("Test")


@bot.event
async def on_ready():
    messageDaily.start()


bot.run(Token.TOKEN)
