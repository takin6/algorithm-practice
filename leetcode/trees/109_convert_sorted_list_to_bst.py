# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None

        if not head.next: return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None

        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)

        return root

    def findMiddle(self, head):
        p1, p2 = head, head
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        return p1

root = ListNode(-10)
root.next = ListNode(-3)
root.next.next = ListNode(0)
root.next.next.next = ListNode(5)
root.next.next.next.next = ListNode(9)

print(Solution().sortedListToBST(root))