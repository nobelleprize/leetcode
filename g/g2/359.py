# https://leetcode.com/accounts/login/?next=/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.logs = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logs:
            if self.logs[message] + 10 > timestamp:
                return False
            else:
                self.logs[message] = timestamp
                return True
        else:
            self.logs[message] = timestamp 
            return True
            

l = Logger()
print(l.shouldPrintMessage(1, "foo"))
print(l.shouldPrintMessage(2, "bar"))
print(l.shouldPrintMessage(3, "foo"))
print(l.shouldPrintMessage(8, "bar"))
print(l.shouldPrintMessage(10, "foo"))
print(l.shouldPrintMessage(11, "foo"))