# https://leetcode.com/problems/partition-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    l = l_head = ListNode(0)
    r = r_head = ListNode(0)
    while head:
        if head.val >= x:
            r.next = head
            r = r.next
        else:
            l.next = head
            l = l.next
        head = head.next
    r.next = None
    l.next = r_head.next
    return l_head.next

l = ListNode(1)
l.next = ListNode(4)
l.next.next = ListNode(3)
l.next.next.next = ListNode(2)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(2)

res = partition(l, 3)
while res:
    print(res.val)
    res = res.next