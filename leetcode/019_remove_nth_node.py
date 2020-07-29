# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        length = 0

        tmp = dummy
        while head is not None:
            # changes variable
            length += 1
            tmp.next = head

            # shifting nodes
            head = head.next
            tmp = tmp.next

        i = length - n
        # nthNode = dummy.next
        nthNode = dummy
        while i > 0:
            nthNode = nthNode.next
            i -= 1

        # if list is a single list, return null
        if nthNode.next is None:
            return dummy.next.next

        # swap value
        nthNode.next = nthNode.next.next

        return dummy.next

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
print(Solution().removeNthFromEnd(l, 2))

l = ListNode(1)
print(Solution().removeNthFromEnd(l, 1))

# [1,2]

l = ListNode(1)
l.next = ListNode(2)
print(Solution().removeNthFromEnd(l, 2))
