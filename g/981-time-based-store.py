# https://leetcode.com/problems/time-based-key-value-store/
from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        n = len(arr)

        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2

            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid

        if right == 0:
            return ""

        return arr[right-1][1]

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo", "test", 1)
obj.set("foo", "bar", 1)
print(obj.get("foo", 3))
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))
print(obj.get("foo", 5))

# obj = TimeMap()
# obj.set("ctondw","ztpearaw",1)
# obj.set("vrobykydll","hwliiq",2)
# obj.set("gszaw","ztpearaw",3)
# obj.set("ctondw","gszaw",4)
# print(obj.get("gszaw",5))
# print(obj.get("ctondw",6))
# print(obj.get("gszaw",8))
# print(obj.get("vrobykydll",9))
# print(obj.get("ctondw",10))
# obj.set("vrobykydll","kcvcjzzwx",11)
# print(obj.get("vrobykydll",12))
# print(obj.get("ctondw",13))
# print(obj.get("vrobykydll",14))
# print(obj.set("ztpearaw","zondoubtib",15))
# print(obj.set("kcvcjzzwx","hwliiq",16))
# print(obj.set("wtgbfvg","vrobykydll",17))
# print(obj.set("hwliiq","gzsiivks",18))
# print(obj.get("kcvcjzzwx",19))
# print(obj.get("ztpearaw",20))

# obj = TimeMap()
# obj.set("love","high",10)
# obj.set("love","low",20)
# print(obj.get("love",5)) 
# print(obj.get("love",10))
# print(obj.get("love",15))
# print(obj.get("love",20))
# print(obj.get("love",25))

# obj = TimeMap()
# obj.set("foo", "test", 1)
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 3))
# obj.set("foo", "bar2", 4)
# print(obj.get("foo", 4))
# print(obj.get("foo", 5))
