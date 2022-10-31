# 알람 정보를 넣어두는 dict.
# 구조 : 
# (추후 수정하는 방향.. but 이게 방대해질 경우 다른 해결방법을 찾아야 한다.) key : userid, value : {serverid:['alarmid']} .. 
# list로 처리해도 되긴 하지만 추후 무언가 쓸 일이 있지 않을까 싶어서 dict 형태로 구조를 짜놓음.
# example. 예약시간 변경..,,, XXXX 이건 안됨.
# 어떤 예시가 있을까?
import asyncio

alarm_info = dict()

class saveAlarmInfo:
    def __init__(self):
        self.info = dict()
        
    def info(self):
        return self.info
    
    def leng(self):
        return len(self.info)
    
    def get_id(self,message:str):
        # print('get',message)
        # print(alarm_info)
        for i in range(10):
            if i not in self.info:
                self.info[i] = message
                return i 
        return ''
    
    async def delete_id(self,t:int,i:int):
        if t <= 0:
            return '0초 이하 X!!'
        if i not in self.info:
            # 여기서 raise를 쓰게되면 어떤 일이 일어날까?.. error 반환, 
            return '해당 정보 없음.'
        await asyncio.sleep(t)
        message = self.info[i]
        del self.info[i]
        return f'메세지 삭제 완료, 메세지: {message}'
        
    