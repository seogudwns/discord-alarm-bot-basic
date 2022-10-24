# 파일 하나에 담기에는 너무 길어서 함수로 분리.
import time
import asyncio

def time_calc(arr):
    times = 0
    
    DHMi = ['d','h','m']
    tmp = []
    for i in range(len(arr)):
        tmp2 = arr[i]
        if tmp2 in DHMi:
            time = int(''.join(tmp))
            if tmp2 == 'd': #일 단위.
                times += time*86400
            elif tmp2 == 'h': #시간 단위.
                times += time*3600
            elif tmp2 == 'm': # 분 단위.
                times += time*60
            tmp = []
        else:
            tmp.append(tmp2)
    if tmp: # 초 단위.
        times += int(''.join(tmp))
    
    return times

async def threader(ctx, unit_time:int, message:str = None):
    await asyncio.sleep(unit_time)
    if message == None:
        return
    await ctx.send(message)