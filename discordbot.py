import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

import time
from threading import Thread

import discord
import discord.ext
from discord.ext import commands
from Services.time_func import (time_calc, threader)

discord_token = os.environ.get('DISOCRD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='>',intents=intents)

@bot.event
async def on_ready():
    print('login Bot: {}'.format(bot.user))

@bot.command() # def를 써줘야한다. 여기서는 ping을 쓸 시 pong이 돌아감.
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')
#     # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.
#     await ctx.send('이후 0부터 3까지 5초 단위로 출력이 됩니다.')
#     for i in range(4):
#         time.sleep(5)
#         await ctx.send('{}'.format(i))

@bot.command(name='사용자정보')
async def author_test(ctx):
    # print(ctx) # 정보 안나온다.
    # await ctx.send('@everyone') # 모두 호출. 비슷하게 '@here' 이나 '@qwer'등도 태그가 달려있는 사람들을 호출.
    # 개별 호출할 때는 맴버들의 아이디가 필요.. <@{member_id}>를 보내야 함.. 쓴 사람을 호출할 때 id = ctx.message.author.id 
    author = ctx.message.author
    author_id = ctx.message.author.id
    str_result = '''
author = {author}
author ID = {author_id}
    '''.format(author=author,
               author_id=author_id)

    await ctx.send(str_result)

@bot.command(name='알람')
async def timer(ctx):
    try:
        lst = ctx.message.content.split()[1:]
        message = '알람이 종료되었습니다.'
        res_time = time_calc(lst[0])
        if len(lst) == 2:
            message = lst[1]
        elif len(lst)>2:
            message = ' '.join(lst[1:])
        
        await threader(res_time)
        await ctx.send(message)
    except:
        await ctx.send('잘못된 사용법입니다.')

@bot.command(name='반복알람')
async def repeat_timer(ctx):
    try:
        lst = ctx.message.content.split()[1:]
        
        after_time = time_calc(lst[0])
        repeat_time = time_calc(lst[1])
        # print(after_time,repeat_time)
        if max(repeat_time,after_time) >= 5184000:
            await ctx.send('대기시간 혹은 반복시간이 너무 깁니다.')
            time.sleep(0.5)
            the_error_string
            
        repeat = int(lst[2])
        message = ' '.join(lst[3:])
        
        await ctx.send('반복 알람 설정이 예약되었습니다.')
        
        await threader(after_time)

        await ctx.send('반복 알람 시작! 메시지 : {}'.format(message))
        
        for i in range(repeat):
            await threader(repeat_time)
            await ctx.send(message)
            
        await ctx.send('반복알람이 종료되었습니다.')
        
    except:
        await ctx.send('잘못된 사용법입니다.')

@bot.command(name='test')
async def test_command(ctx):
    discord.ext.tasks.Loop



# @bot.command(name='check')
# async def check(ctx):
#     time.sleep(3)
#     check_lst = '''
#     <@{}>,
#     <@{}>,
#     <@{}>,
#     '''.format('HJ',1,ctx.message.author.id)
    
#     await ctx.send(check_lst)

bot.run(discord_token)


# ! First problem.
# WARNING  discord.ext.commands.bot Privileged message content intent is missing, commands may not work as expected. 
# & 
# '''
# raise PrivilegedIntentsRequired(exc.shard_id) from None
# discord.errors.PrivilegedIntentsRequired: Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. 
# It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.
# '''
# --> solved.

# ! Second Problem.
# 시간은 어떻게 제어하면 좋을까?
# time.sleep()에 어떤 maximum 한도가 있다.. 어쩌지? + 경고메시지도 뜨네??..
# Thread라는 것이 있는데 이를 이용해보면 될까?
# 참고용1 : https://github.com/seogudwns/discord.py/blob/master/discord/ext/tasks/__init__.py 
# 참고용2 : https://fishpoint.tistory.com/5237
# Done... use asyncio(python의 비동기에 대한 사용.)