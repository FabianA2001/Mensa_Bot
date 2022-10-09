import Token

import discord
from discord.ext import commands
from discord.ext import tasks as discordTasks
from datetime import datetime as dt

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
hour = 8
minute = 36
block_day = ["saturday", "sunday"]


@discordTasks.loop(minutes=1)
async def messageDaily():
    if dt.now().strftime("%A").lower() in block_day:
        return
    if dt.now().hour == hour and dt.now().minute == minute:
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


bot.run(Token.DISCORD_TOKEN)
