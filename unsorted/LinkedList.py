class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Given previous node not in LinkedList")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while (temp.next):
            temp = temp.next

        temp.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def deleteNodePos(self, position):
        if self.head == None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break 

        if temp is None:
            return
        if temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

    # def getLength(self):
    #     count = 0
    #     current = self.head
    #     while current:
    #         count += 1
    #         current = current.next
    #     return count

    # def getLengthRec(self, node):
    #     if not node:
    #         return 0
    #     else:
    #         return 1 + self.getLengthRec(node.next)
    
    def findElement(self, element):
        current = self.head

        while current != None:
            if current.data == element:
                return True
            current = current.next

        return False

    def findElementRec(self, element, node):
        if not node:
            return False

        if node.data == element:
            return True

        return self.findElementRec(element, node.next)

    def getNth(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next

        assert(False)
        return 0

    def getLength(self):
        current = self.head
        length = 0

        while current != None:
            length += 1
            current = current.next

        return length

    def nthNodeFromEnd(self, n):
        length = self.getLength()
        index = length - n
        current = self.head

        for i in range(index):
            current = current.next
        return current.data

    def nthNodeFromEndv2(self, n):
    # 2 pointer approach
        main_ptr = self.head
        sec_ptr = self.head

        for i in range(n):
            sec_ptr = sec_ptr.next

        while sec_ptr != None:
            main_ptr = main_ptr.next
            sec_ptr = sec_ptr.next
        return main_ptr.data

    def getMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data
    
    def occurrence(self, n):
        current = self.head
        count = 0
        while current:
            if current.data == n:
                count += 1
            current = current.next

        return count

    def detectCycle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while (slow_ptr.next and fast_ptr.next.next and slow_ptr != fast_ptr):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr == fast_ptr

    def isPalindrome(self):
        current = self.head
        stack = []
        
        while current:
            stack.append(current.data)
            current = current.next
        
        check = self.head

        while check:
            if stack.pop() != check.data:
                return False
            check = check.next

        return True

    def reverse(self):
        prev = None
        current = self.head
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def removeDuplicateSorted(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            current = current.next

    def removeDuplicateUnsorted(self):
        hash = set()
        current = self.head
        hash.add(self.head.data)

        while current.next:
            if current.next.data not in hash:
                hash.add(current.next.data)
                current = current.next
            else:
                current.next = current.next.next

    def swapElements(self, x, y):
        if x == y:
            return
        
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next
        
        if currX == None or currY == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY
        
        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp
       

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(6)
llist.append(8)
llist.append(4)
llist.append(5)
llist.printList()
print('*****')
llist.swapElements(2, 4)
llist.printList()