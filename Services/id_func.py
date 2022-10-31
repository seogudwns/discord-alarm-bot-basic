import asyncio
from Services.alarm_info import alarm_info

def get_id(message:str):
    print('get',message)
    # print(alarm_info)
    for i in range(10):
        if i not in alarm_info:
            alarm_info[i] = message
            return i 
    return None

async def delete_id(t:int,i:int):
    await asyncio.sleep(t) 
    del alarm_info[i]