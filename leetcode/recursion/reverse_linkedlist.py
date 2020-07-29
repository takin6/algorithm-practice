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
    # def reverseListIterative(self, head: ListNode) -> ListNode:
    #     if head is None: return head

    #     tmp = head
    #     new_head = ListNode(None)

    #     while tmp is not None:
    #         l = ListNode(tmp.val)
    #         l.next = new_head
    #         new_head = l

    #         tmp = tmp.next

    #     return new_head

    def reverseListIterative(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr != None:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp

        return prev

    # def reverseListRecursive(self, head: ListNode) -> ListNode:
    #     if type(head) is not ListNode or head is None or head.next is None: return head
    #     # recurrence relation
    #     # l = 
    #     def helper(old, new):
    #         if old is None: 
    #             return new
    #         else:
    #             l = ListNode(old.val)
    #             l.next = new
    #             new = l
    #             print(new)
    #             helper(old.next, new)

    #     new = helper(head.next, ListNode(head.val))

    #     return new 
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        p = self.reverseListRecursive(head.next)
        print(p)
        head.next.next = head
        head.next = None

        return p

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# print(Solution().reverseListIterative(head))
print(Solution().reverseListRecursive(head))
# print(Solution().reverseListRecursive([]))
# 1->2->3->4->5->NULL


# recurrence relation
# f(head) = f(head.next(until last))
# 