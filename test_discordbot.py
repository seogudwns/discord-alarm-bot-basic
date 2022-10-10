# import discord
# from discord.ext import commands

# discord_bot_token = 'MTAyODg4NjE1NTU4NTkzMzMzMg.GoXNm9.1yB98uFDsCm5MybXAlT53w7YIlKT69UWUZoXlM'
# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix=">", intents=intents)

# @bot.event
# async def on_ready():
#     print('Bot: {}'.format(bot.user))

# @bot.command()
# async def ping(ctx):
#     await ctx.send("pong")

# bot.run(discord_bot_token)

from datetime import datetime
import time

datetime_string = "2021년 12월 31일 13시 35분 42.657813초"
datetime_format = "%Y년 %m월 %d일 %H시 %M분 %S.%f초"

datetime_result = datetime.strptime(datetime_string, datetime_format)
print(type(datetime_result)) # <class 'datetime.datetime'>
print(datetime_result) # 2021-12-31 13:35:42.657813

time_result = time.strptime(datetime_string, datetime_format)
print(type(time_result))  # <class 'time.struct_time'>
print(time_result)  # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=31, tm_hour=13, tm_min=35, tm_sec=42, tm_wday=4, tm_yday=365, tm_isdst=-1)


datetime_string = "2021-12-31 13:35:42.657813"
datetime_format = "%Y-%m-%d %H:%M:%S.%f"

datetime_result = datetime.strptime(datetime_string, datetime_format)
print(type(datetime_result)) # <class 'datetime.datetime'>
print(datetime_result) # 2021-12-31 13:35:42.657813

time_result = time.strptime(datetime_string, datetime_format)
print(type(time_result))  # <class 'time.struct_time'>
print(time_result)  # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=31, tm_hour=13, tm_min=35, tm_sec=42, tm_wday=4, tm_yday=365, tm_isdst=-1)


datetime_string = "12/31 2021"
datetime_format = "%m/%d %Y"

datetime_result = datetime.strptime(datetime_string, datetime_format)
print(type(datetime_result)) # <class 'datetime.datetime'>
print(datetime_result) # 2021-12-31 00:00:00

time_result = time.strptime(datetime_string, datetime_format)
print(type(time_result))  # <class 'time.struct_time'>
print(time_result)  # time.struct_time(tm_year=2021, tm_mon=12, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=365, tm_isdst=-1)