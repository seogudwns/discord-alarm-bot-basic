# 알람의 시간간극이 2달을 넘어갈 경우 컷하기 위해 만든 error
class TimeLongError(Exception):
    def __init__(self,msg=None):
        self.msg=msg
    def __str__(self):
        return self.msg

# 알람 갯수제한을 위한 error. default = 10.
class ListLongError(Exception):
    def __init__(self,msg=None):
        self.msg=msg
    def __str__(self):
        return self.msg

# repeat는 대강 365번 잡자.
class RepeatLongError(Exception):
    def __init__(self,msg=None):
        self.msg=msg
    def __str__(self):
        return self.msg