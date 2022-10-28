# 알람 정보를 넣어두는 dict.
# 구조 : 
# (추후 수정하는 방향.. but 이게 방대해질 경우 다른 해결방법을 찾아야 한다.) key : userid, value : {serverid:['alarmid']} .. 
# list로 처리해도 되긴 하지만 추후 무언가 쓸 일이 있지 않을까 싶어서 dict 형태로 구조를 짜놓음.
# example. 예약시간 변경..,,, XXXX 이건 안됨.
# 어떤 예시가 있을까?
alarm_info = dict()