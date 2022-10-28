import asyncio
from Services.alarm_info import alarm_info

def get_id(message):
    print('get',message)
    print(alarm_info)
    for i in range(10):
        if i not in alarm_info:
            alarm_info[i] = message
            return i 

async def delete_id(t,i):
    await asyncio.sleep(t) 
    del alarm_info[i]