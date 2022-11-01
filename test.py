# import asyncio
# import time
# import psutil
# from threading import Thread

# https://jybaek.tistory.com/895 메모리 사용량.
# def memory_usage(message: str = 'debug'):
#     # current process RAM usage
#     p = psutil.Process()
#     rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
#     print(f"[{message}] memory usage: {rss: 10.5f} MB")

# memory_usage('#1')
# print(f"start at {time.strftime('%X')}")
# result = 0
# async def check1(i):
#     global result
#     # await asyncio.sleep(1)
#     result += i
#     # print(result)

# async def check2(k):
#     for i in range(k):
#         await asyncio.create_task(check1(i))

# asyncio.run(check2(100000))

# print(result)
# print(f"finished at {time.strftime('%X')}")
# memory_usage('#2')

# result = 0
# for i in range(100000):
#     result = result + i

# print(result)
# print(f"finished at {time.strftime('%X')}")
# memory_usage('#3')

# async def check3(i):
#     global result
#     # await asyncio.sleep(1)
#     result += i
#     # print(result)

# async def check4(k):
#     for i in range(k):
#         await Thread.run(check3(i))

# Thread.run(check4(1000))

# print(result)
# print(f"finished at {time.strftime('%X')}")
# memory_usage('#3')

# import asyncio
# from datetime import datetime
# from random import randint

# async def run_job() -> None:
#     delay = randint(5, 15)
#     print(f'{datetime.now()} sleep for {delay} seconds')
#     await asyncio.sleep(delay)  # 5~15초 동안 잠자기
#     print(f'{datetime.now()} finished ({delay} sec)')

# async def main() -> None:
    
#     for i in range(int(input())):
#         asyncio.create_task(run_job())
#         await asyncio.sleep(10)

# asyncio.run(main())
# import random
# print(str(random.random())[2:])

# import asyncio
# from Services.alarm_info import alarm_info
# from Services.id_func import (get_id, delete_id)

# print(alarm_info)

# alarm_info['123'] = 123
# print(alarm_info)

# # ! 

# import asyncio
# from Services.alarm_info import SaveAlarmInfo

# alarm_info = SaveAlarmInfo()

# print(alarm_info.info)

# x = alarm_info.get_id('qwer')
# for i in range(5):
#     alarm_info.get_id(str(i))
    
# print(alarm_info.info)
# asyncio.run(alarm_info.delete_id(1,2))

# print(alarm_info.info)

