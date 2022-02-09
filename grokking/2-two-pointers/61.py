# https://leetcode.com/problems/rotate-list/
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head:
        return None
    if not head.next:
        return head
        
    temp = head
    n = 1
    
    # close linked list into ring
    while temp.next != None:
        temp = temp.next
        n += 1
    temp.next = head
    
    # new tail: n - (k % n) - 1
    # new head: n - (k % n)
    new_tail = head
    for _ in range(n - k%n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None

    return new_head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
res = rotateRight(l, 2)

c = 0
while c < 5:
    print(res.val)
    res = res.next
    c += 1