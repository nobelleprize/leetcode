class twoStacks:

    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = data
        else:
            exit(1)

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = data
        else:
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            top = self.arr[self.top1]
            self.top1 -= 1
            return top
        else:
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            top = self.arr[self.top2]
            self.top2 += 1
            return top
        else:
            exit(1)

    def printStack(self):
        return self.arr
            

stacks = twoStacks(10)
stacks.push1(1)
stacks.push1(2)
stacks.push1(3)
stacks.push2(5)
stacks.push2(6)
stacks.push2(7)
 
print(stacks.printStack())
