import discord
from discord.ext import commands
import time
from dotenv import load_dotenv
import os
load_dotenv()

discord_token = os.environ.get('DISOCRD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('login Bot: {}'.format(bot.user))

@bot.command() # def를 써줘야한다. 여기서는 ping을 쓸 시 pong이 돌아감.
async def ping(ctx):
    await ctx.send(f'pong! {round(round(bot.latency, 4)*1000)}ms')
    # 봇의 핑을 pong! 이라는 메세지와 함께 전송한다. latency는 일정 시간마다 측정됨에 따라 정확하지 않을 수 있다.
    await ctx.send('이후 0부터 3까지 5초 단위로 출력이 됩니다.')
    for i in range(4):
        time.sleep(5)
        await ctx.send('{}'.format(i))
         

@bot.command(name="1234")
async def _12345(ctx):
    await ctx.send("5678")
#파이썬 문법에 따라 함수를 만들 때에는 첫글자에는 숫자를 넣을 수 없는데, 숫자를 사용하고싶다면 함수 이름 자리는 다른 아무것으로 대체하고 괄호 안에 name=""을 사용하여 명령어를 제작할 수 있다.

@bot.command(name='hello')
async def author_test(ctx):
    # print(ctx) # 정보 안나온다.
    # await ctx.send('@everyone') # 모두 호출. 비슷하게 '@here' 이나 '@qwer'등도 태그가 달려있는 사람들을 호출.
    # 개별 호출할 때는 맴버들의 아이디가 필요.. <@{member_id}>를 보내야 함.. 쓴 사람을 호출할 때 id = ctx.message.author.id 
    author = ctx.message.author
    author_id = ctx.message.author.id
    author_name = ctx.message.author.name
    message_contents = ctx.message.content

    str_result = '''
author = {author}
author ID = {author_id}
author name = {author_name}
message contents = {message_contents}
<@{author_id}>
    '''.format(author=author,
               author_id=author_id,
               author_name=author_name,
               message_contents=message_contents)

    await ctx.send(str_result)

@bot.command(name='mention_repeat')
async def set_timer(ctx):
    try:
        # 모든 시간은 초단위.
        # 차례대로 : ['mention_repeat', 몇초 후, 반복 횟수, 메시지, ]
        lst = ctx.message.content.split()[1:]
        await ctx.send(lst)
    except:
        await ctx.send('잘못된 사용법입니다.')

@bot.command(name='check')
async def check(ctx):
    time.sleep(3)
    check_lst = '''
    <@{}>,
    <@{}>,
    <@{}>,
    '''.format('서형준',1,ctx.message.author.id)
    
    await ctx.send(
        check_lst
    )


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