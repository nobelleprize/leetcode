# https://leetcode.com/problems/rle-iterator/
from collections import OrderedDict

class RLEIterator:

    def __init__(self, encoding):
        self.A = encoding
        self.index = 0
        
    def next(self, n: int) -> int:
        while self.index < len(self.A):
            if n <= self.A[self.index]:
                self.A[self.index] -= n
                return self.A[self.index + 1]
            n -= self.A[self.index]
            self.index += 2
        return -1

# Your RLEIterator object will be instantiated and called as such:

obj = RLEIterator([3,8,0,9,3,5])
print(obj.next(5))
print(obj.next(1))
print(obj.next(1))
print(obj.next(2))

# obj = RLEIterator([923381016,843,898173122,924,540599925,391,705283400,275,811628709,850,895038968,590,949764874,580,450563107,660,996257840,917,793325084,82])
# print(obj.next(612783106))
# print(obj.next(486444202))
# print(obj.next(630147341))
# print(obj.next(845077576))
# print(obj.next(243035623))
# print(obj.next(731489221))
# print(obj.next(117134294))
# print(obj.next(220460537))
# print(obj.next(794582972))
# print(obj.next(332536150))
# print(obj.next(815913097))
# print(obj.next(100607521))
# print(obj.next(146358489))
# print(obj.next(697670641))
# print(obj.next(45234068))
# print(obj.next(573866037))
# print(obj.next(519323635))
# print(obj.next(27431940))
# print(obj.next(16279485))
# print(obj.next(203970))