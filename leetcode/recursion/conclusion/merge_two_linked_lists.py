# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1

        if l1.val > l2.val:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        elif l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)

        return head



    #     def helper(ll1, ll2, head):
    #         if ll1 is None or ll2 is None: return head

    #         l1nextTemp = ll1.next
    #         ll1.next = ll2
    #         l2nextTemp = ll2.next
    #         ll2.next = l1nextTemp

    #         helper(l1nextTemp, l2nextTemp, head)

    #     head = l1
    #     if l1 is None or l1.val < l2.val: head = l2
    #     return helper(l1, l2, head)


    # if not l1 or not l2:
    #     return l1 or l2
    # if l1.val < l2.val:
    #     l1.next = self.mergeTwoLists(l1.next, l2)
    #     return l1
    # else:
    #     l2.next = self.mergeTwoLists(l1, l2.next)
    #     return l2