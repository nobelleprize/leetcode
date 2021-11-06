class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


    def print(self):
        current = self.head
        
        while current:
            print(current.data)
            current = current.next

    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def append(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head

        while (temp.next):
            temp = temp.next

        temp.next = new_node


    def removeDupsUnsorted(self):
        hash = set()
        current = self.head
        hash.add(current.data)
        while current.next:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next


    def removeDupsUnsortedv2(self):
        i = self.head
        j = self.head
        while i.next:
            if j.next == None:
                i = i.next
                j = i
            elif i.data == j.next.data:
                j.next = j.next.next
            else:
                j = j.next


    def length(self):
        current = self.head
        size = 0
        while current != None:
            size += 1
            current = current.next
        return size


    def getKthLast(self, k):
        i = self.length() - k
        current = self.head

        for j in range(i):
            current = current.next

        return current.data


    def partition(self, p):
        i_head = None
        i_last = None
        j_head = None
        j_last = None
        current = self.head
        
        while current != None:
            if current.data >= p:
                if j_head == None:
                    j_head = current
                    j_last = current
                else:
                    j_last.next = current
                    j_last = j_last.next
            
            elif current.data < p:
                if i_head == None:
                    i_head = current
                    i_last = current
                else:
                    i_last.next = current
                    i_last = i_last.next

            current = current.next
        
        if j_last != None:
            j_last.next = None

        if i_head == None:
            return j_head
        
        if j_head == None:
           i_last.next = None
           return i_head

        i_last.next = j_head
        return i_head


    def partitionv2(self, p):
        current = self.head
        tail = self.head

        while current != None:
            next = current.next

            if current.data < p:
                current.next = self.head
                self.head = current

            else:
                tail.next = current
                tail = current
            
            current = next
        tail.next = None

        return current


def add_lists(x, y):
    result = Node(0)
    result_tail = result
    overflow = 0
    while x or y or overflow:
        x_val = x.data if x else 0
        y_val = y.data if y else 0
        
        total = x_val + y_val + overflow
        overflow = total // 10
        
        result_tail.next = Node(total % 10)
        result_tail = result_tail.next

        x = x.next if x else None
        y = y.next if y else None
    
    return result.next


def add_list_forward(a, b):
    stack_a = []
    stack_b = []
    while a:
        stack_a.append(a.data)
        a = a.next
    while b:
        stack_b.append(b.data)
        b = b.next
    
    diff = len(stack_a) - len(stack_b)
    if diff < 0:
        for i in range(diff):
            stack_a.insert(0, 0)
    elif diff > 0:
        for i in range(diff):
            stack_b.insert(0, 0)

    c = 0
    head = None
    while stack_a:
        res = stack_a.pop() + stack_b.pop() + c 
        c = res // 10
        head = _push(res % 10, head)
    if c:
        head = _push(c, head)
    return head


def _push(new_data, n):
    new_node = Node(new_data)
    new_node.next = n
    return new_node

a = Node(8)
a.next = Node(9)
a.next.next = Node(9)

b = Node(1)

res = add_list_forward(a, b)
while res:
    print(res.data)
    res = res.next