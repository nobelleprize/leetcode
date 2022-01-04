# https://leetcode.com/problems/logger-rate-limiter/
from collections import defaultdict

class logger:

    def __init__(self):
        self.messages = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.messages:
            if timestamp >= self.messages[message]:
                print(message)
                self.messages[message] = timestamp + 10
                return True
            return False
        else:
            print(message)
            self.messages[message] = timestamp + 10
            return True


# [current, next_allowed]
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

obj = logger()
obj.shouldPrintMessage(1,"foo")
obj.shouldPrintMessage(2, "bar")
obj.shouldPrintMessage(3, "foo")
obj.shouldPrintMessage(8, "bar")
obj.shouldPrintMessage(10, "foo")
obj.shouldPrintMessage(11, "foo")