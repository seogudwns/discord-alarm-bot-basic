from dotenv import load_dotenv
import os
load_dotenv()

# !!!! 제어부분... 추후 다시 생각해봐야 함. 여기 넣었을 때 작동하지 않음. usestate같은 것이 있나??..

list_limit = 10 # 알람 갯수제한.
repeat_limit = 100 # 알람 반복 갯수제한.

import asyncio
import datetime
import discord
from discord.ext import commands

from Services.time_func import (time_calc, threader)
from Services.alarm_info import SaveAlarmInfo
from Services.Exception import (TimeLongError, ListLongError, RepeatLongError)

alarm = SaveAlarmInfo()

# ! 코드.

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
        if alarm.leng() >= list_limit:
            raise ListLongError
        
        lst = ctx.message.content.split()[1:]

        message = ''
        res_time = time_calc(lst[0])
        # print(res_time)
        if len(lst) == 2:
            message = lst[1]
        elif len(lst)>2:
            message = ' '.join(lst[1:])
        print(message)
        if res_time >= 5184000:
            raise TimeLongError
        print('알람 리스트가 선언이 안되는 것 같은데??.. ')
        print('알람 리스트가 선언이 안되는 것 같은데??..(2) ',alarm.info())
        id = alarm.get_id('{} : {}'.format(datetime.now(), ctx.message.content)) 
        # ! 여기가 문제. 함수 자체가 실행되지 않는데..
        print(id)
        if not id:
            print('id 인식 안됨..')
            raise
        asyncio.create_task(threader(ctx, res_time, id, message))
        asyncio.create_task(alarm.delete_id(res_time+1,id))
        
    except ListLongError:
        await ctx.send('알람 예약 갯수 한도를 초과했습니다.')
    except TimeLongError:
        await ctx.send('2달 이내의 시간으로 설명해주세요.')
    except:
        await ctx.send('잘못된 사용법입니다.')

@bot.command(name='반복알람')
async def repeat_timer(ctx):
    try:
        if alarm.ieng() >= list_limit:
            raise ListLongError
        
        lst = ctx.message.content.split()[1:]
        
        after_time = time_calc(lst[0])
        repeat_time = time_calc(lst[1])
        if max(repeat_time,after_time) >= 5184000:
            raise TimeLongError
        
        repeat = int(lst[2])
        if repeat>repeat_limit:
            raise RepeatLongError
        
        if len(lst) == 4:
            message = lst[3]
        else:
            message = ' '.join(lst[3:]) # ! split에서부터 수정 필요.. 어떻게 하면 좋을까?
        
        id = alarm.get_id('{} : {}'.format(datetime.now(), ctx.message.content))
        await ctx.send('반복 알람 설정이 예약되었습니다.')
        
        asyncio.create_task(await threader(ctx, after_time, id, '반복 알람 시작! 메시지 : {}'.format(message)))
        
        for i in range(1,repeat+1):
            asyncio.create_task(threader(ctx, after_time + i*repeat_time, id, '{}. {}'.format(i,message)))
        
        asyncio.create_task(threader(ctx, after_time + i*repeat_time, id, '반복알람이 종료되었습니다.'))
        asyncio.create_task(alarm.delete_id(after_time + i*repeat_time + 1,id))
        
    except ListLongError:
        await ctx.send('알람 예약 갯수 한도를 초과했습니다.')
    except TimeLongError:
        await ctx.send('대기시간 혹은 반복시간이 너무 깁니다. 2달 이내의 시간으로 설정해주세요.')
    except RepeatLongError:
        await ctx.send('너무 많은 반복입니다. {}개 미만으로 알람 갯수를 줄여주세요.'.format(repeat_limit))
    except Exception:
        await ctx.send('잘못된 사용법입니다.')


# ! 이건 아마도 쉬울텐데... 중간에 정지시키려면 어떻게 하면 좋을까?? thread의 event를 생각해서 코드 업데이트를 해보자.
# ! 우선 알람 리스트 불러오기부터 완성시켜볼 것..!..
@bot.command(name='알람리스트')
async def alarm_lst(ctx):
    try:
        if ctx.message.content[1:] != '알람리스트':
            raise
        
        cnt = 0
        for i in range(list_limit):
            if alarm.info()[i]:
                message = 'id : {}, alarm : {}'.format(i,alarm.info[i])
                cnt += 1
                await ctx.send(message)
                
        if cnt == 0:
            await ctx.send('대기중인 알람이 존재하지 않습니다.')
    except:
        await ctx.send('메시지를 잘못 입력하셨습니다. 정확한 메세지 : >알람리스트')
        
@bot.command(name='알람삭제')
async def delete_alarm(ctx):
    try:
        message = ctx.message.content.split()
        if len(message) != 2:
            raise
        
        id = int(message[1])
        alarm_message = alarm.info[id]
        if not alarm_message:
            raise
        
        asyncio.create_task(alarm.delete_id(id))
        await ctx.send('알람 삭제 완료!, 알람 내용 :',alarm_message)
    except:
        await ctx.send('해당 아이디의 알람이 존재하지 않습니다.')

bot.run(discord_token)

# @bot.command(name='check')
# async def check(ctx):
#     time.sleep(3)
#     check_lst = '''
#     <@{}>,
#     <@{}>,
#     <@{}>,
#     '''.format('HJ',1,ctx.message.author.id)
    
#     await ctx.send(check_lst)



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

# ! Third Problem.
# 여러 명령 제어.. ex 취소 등.. asyncio 사용에 익숙해질 필요가 있다. + 이미 디코 서버에서는 asyncio를 써서 코드를 제어하고 있는듯..

# ! Fourth Problem.
# get_id 함수 자체가 먹통이다.. 왜 작동을 하지 않는 거일까..?.. 당황스러운데..,,,
# 아예 서버를 잡아야 해서 그런건가??..