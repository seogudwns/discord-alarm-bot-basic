from Services.alarm_info import alarm_info
import random

def create_tmp_id():
    id = str(random.random())[2:]
    if id not in alarm_info:
        return id
    return str(random.random())[2:]
# 임의로 10개 제한을 걸 예정인데 이 확률을 뚫고 중복아이디가 들어가 봇이 오류가 났다면 로또사십쇼.(while로 처리하면 되긴 하지만 뭐..)