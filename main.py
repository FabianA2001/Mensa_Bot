import Token
from Meals import Meals
import discord
from discord.ext import commands
from discord.ext import tasks as discordTasks
from datetime import datetime as dt
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
hour = 8
minute = 0
block_day = ["saturday", "sunday"]


@discordTasks.loop(minutes=1)
async def messageDaily():
  if dt.now().strftime("%A").lower() in block_day:
    return
  if dt.now().hour == hour - 2 and dt.now().minute == minute:
    await dm_task()


def generate_string(meals):
  result = ""
  for meal in meals:
    result += f"{meal.name} --- {meal.price}€\n"
  return result


def add_fields_to_embed(embed, id):
  meals = Meals(id)
  embed.add_field(
    name="__Hauptgericht__",
    value=generate_string(meals.main_meal),
    inline=False,
  )
  embed.add_field(
    name="__Beilage__",
    value=generate_string(meals.supplement_meal),
    inline=False,
  )
  embed.add_field(
    name="__Nachtisch__",
    value=generate_string(meals.dessert_meal),
    inline=False,
  )
  return embed


async def dm_task():
  await bot.wait_until_ready()
  for id in Token.IDS:
    user = await bot.fetch_user(id)
    if user == None:
      print("Das ist die falsche channel id")
    else:
      embed = discord.Embed(
        title="Mensa 1 - Braunschweig",
        description=f"{dt.now().strftime('%d.%m.%Y')}",
        color=0xFF5733,
      )
      embed = add_fields_to_embed(embed=embed, id=101)
      await user.send(embed=embed)

      embed = discord.Embed(
        title="Mensa 2 - Braunschweig",
        description=f"{dt.now().strftime('%d.%m.%Y')}",
        color=0x32A852,
      )
      embed = add_fields_to_embed(embed=embed, id=105)
      await user.send(embed=embed)


@bot.event
async def on_ready():
  messageDaily.start()


keep_alive()
# bot.run(Token.DISCORD_TOKEN)

# https://plainenglish.io/blog/send-an-embed-with-a-discord-bot-in-python
