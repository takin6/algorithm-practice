class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        head = self
        t = []
        while head.next != None:
            t.append(str(head.val))
            head = head.next
        t.append(str(head.val))

        return " ".join(t)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return head
  
        def swap(head):
            if head.next is None: return
            else:
                head.val, head.next.val = head.next.val, head.val
                if head.next.next is None: return
                swap(head.next.next)
        
        swap(head)
        return head

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

# print(Solution().swapPairs(head))

print(Solution().swapPairs([]))