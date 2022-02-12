# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = -1
        self.array = {}
        self.snaps = {}

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snaps[self.snap_id] = self.array.copy()
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        if snap_id-1 not in self.snaps or self.snaps[snap_id-1] == {}\
            or index not in self.snaps[snap_id-1]:
            return 0
        return self.snaps[snap_id-1][index]

obj2=SnapshotArray(2)
obj2.set(0,12)
print(obj2.snap())
print(obj2.snap())
print(obj2.get(1,0))
print(obj2.get(1,0))
print(obj2.snap())
print(obj2.snap())
# obj1 = SnapshotArray(3)
# obj1.set(0,5)
# print(obj1.snap())
# obj1.set(0,5)
# print(obj1.get(0,0))

# obj = SnapshotArray(4)
# print(obj.snap())
# print(obj.snap())
# print(obj.get(3,1))
# obj.set(2,4)
# print(obj.snap())
# obj.set(1,4)

