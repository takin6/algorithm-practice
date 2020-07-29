# from typing import List
# from collections import Counter

# class Node:
#     def __init__(self, val=None):
#         self.prev = None
#         self.val = val
#         self.next = None

# class DLL:
#     def __init__(self):
#         self.head = Node()
#         self.tail = Node()
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def insert(self, n):
#         prev = self.tail.prev

#         # changing association with self.tail.prev
#         prev.next = n
#         n.prev = prev

#         # chaning association with self.tail
#         self.tail.prev = n
#         n.next = self.tail

#     def remove(self, n):
#         n.prev.next, n.next.prev = n.next, n.prev
#         n = None

# class FirstUnique:

#     def __init__(self, nums: List[int]):
#         self.dll = DLL()
#         self.counter = Counter()
#         self.dic = {}
#         for num in nums:
#             self.add(num)

#     def showFirstUnique(self) -> int:
#         if self.dll.head.next.val is not None:
#             return self.dll.head.next.val
#         else:
#             return -1
        
#     def add(self, num: int) -> None:
#         if self.counter[num] == 1:
#             self.dll.remove(self.dic[num])
#             self.counter[num] = -1
#             self.dic[num] = None
#         elif self.counter[num] != -1:
#             n = Node(num)
#             self.dll.insert(n)
#             self.counter[num] += 1
#             self.dic[num] = n

from collections import Counter, deque

class FirstUnique:
    def __init__(self, nums):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self):
        while self.d and self.c[self.d[0]] != 1:
            self.d.popleft()
        return self.d[0] if self.d else -1

    def add(self, value):
        self.c[value] += 1
        self.d.append(value)

fu = FirstUnique([2,3,5])
print(fu.showFirstUnique())
print(fu.add(5))
print(fu.showFirstUnique())
print(fu.add(2))
print(fu.showFirstUnique())
print(fu.add(3))
print(fu.showFirstUnique())

