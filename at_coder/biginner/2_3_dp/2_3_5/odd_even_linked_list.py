# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # tail = head
        # l = 1
        # while tail.next is not None:
        #     tail = tail.next
        #     l += 1
        
        # prev = None
        # cur = head
        # i = 1
        # while i < l:
        #     if i % 2 == 0:
        #         tmp = cur.next
        #         prev.next = cur.next
        #         tail.next = cur
        #         cur.next = None
        #         tail = cur
    
        #         cur = tmp
        #     else:
        #         prev = cur
        #         cur = cur.next
        #     i += 1

        # import pdb; pdb.set_trace()
        # return head
        if head is None: return head
        odd, even = head, head.next
        evenHead = even
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd,even = odd.next,even.next

            # import pdb; pdb.set_trace()
        odd.next = evenHead
        import pdb; pdb.set_trace()
        return head

l = ListNode(1)
l.next = ListNode(1)
Solution().oddEvenList(l)
# l = ListNode(1)
# l.next = ListNode(2)
# l.next.next = ListNode(3)
# l.next.next.next = ListNode(4)
# l.next.next.next.next = ListNode(5)
# Solution().oddEvenList(l)