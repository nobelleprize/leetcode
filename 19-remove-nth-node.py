# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    slow = head
    fast = head

    for i in range(n):

        if fast.next == None:

            if (i == n - 1):
                head = head.next
            return head

        fast = fast.next

    while fast.next != None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return head

l = ListNode(1)
l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(5)
l = removeNthFromEnd(l, 2)

while l:
    print(l.val)
    l = l.next
    