# https://www.geeksforgeeks.org/merge-k-sorted-arrays-set-3-using-divide-and-conquer-approach/
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None


def merge_two_lists(a, b):
    head = Node(0)
    tail = head

    while a and b:
        if a.data > b.data:
            tail.next = b
            b = b.next
        else:
            tail.next = a
            a = a.next
        tail = tail.next

    if a:
        tail.next = a
    if b:
        tail.next = b

    return head.next

def merge_k_lists(lists):
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []
    
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            if (i + 1) < len(lists):
                l2 = lists[i + 1]
            else:
                l2 = None
            
            mergedLists.append(merge_two_lists(l1, l2))

        lists = mergedLists
        
    return lists[0]
    # amount = len(lists)
    # interval = 1

    # while interval < amount:
    #     for i in range(0, amount - interval, interval * 2):
    #         lists[i] = merge_two_lists(lists[i], lists[i + interval])
    #     interval = interval * 2

    # if amount > 0:
    #     return lists[0]

    # return None

li = Node(1)
li.next = Node(4)
li.next.next = Node(5)

li1 = Node(1)
li1.next = Node(3)
li1.next.next = Node(4)

li2 = Node(2)
li2.next = Node(6)

li3 = Node(1)
li3.next = Node(2)
li3.next.next = Node(3)
li3.next.next.next = Node(4)

li4 = Node(1)
li4.next = Node(4)
li4.next.next = Node(5)

li5 = Node(1)
li5.next = Node(3)
li5.next.next = Node(4)

li6 = Node(2)
li6.next = Node(6)

# li7 = Node(1)
# li7.next = Node(2)
# li7.next.next = Node(3)
# li7.next.next.next = Node(4)

# res = merge_two_lists(li2, li3)
# while res:
#     print(res.data)
#     res = res.next

res = merge_k_lists([li, li1, li2, li3, li4, li5, li6])
while res:
    print(res.data)
    res = res.next