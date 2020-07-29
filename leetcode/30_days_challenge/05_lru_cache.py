class Node:
    def __init__(self, key=None, val=None):
        self.prev = None
        self.val = val
        self.next = None
        self.key = key

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, n):
        self.head.next.prev = n
        n.next = self.head.next

        self.head.next = n
        n.prev = self.head

        return n

    def popLast(self):
        n = self.tail.prev
        
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return n

    def remove(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev

    def updateOrder(self,n):
        if n.prev == self.head: return
        self.remove(n)
        self.insert(n)

class LRUCache:

    def __init__(self, capacity: int):
        self.dll = DLL()
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1

        self.dll.updateOrder(self.dict[key])
        return self.dict[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            n = self.dict[key]
            self.dll.remove(n)

        n = Node(key, value)
        self.dll.insert(n)
        self.dict[key] = n

        if len(self.dict) > self.capacity:
            n = self.dll.popLast()
            self.dll.remove(n)
            del self.dict[n.key]

# class LRUCache:
#     def __init__(self, capacity):
#         self.__size = capacity
#         self.__cache = OrderedDict()

#     def get(self, key):
#         if key in self.__cache:
#             self.__cache.move_to_end(key)
#             return self.__cache[key]
#         return -1

#     def put(self, key, value):
#         if key not in self.__cache:
#             if len(self.__cache) == self.__size:
#                 # move to the first
#                 self.__cache.popitem(last=False)
#         else:
#             # move to the end
#             self.__cache.move_to_end(key)

#         self.__cache[key] = value



cache = LRUCache(10)
cache.put(10, 13)
cache.put(3, 17)
cache.put(6, 11)
cache.put(10, 5)
cache.put(9, 10)
cache.get(13)
cache.put(2, 19)
cache.get(2)
cache.get(3)
cache.put(5, 25)
cache.get(8)
cache.put(9, 22)
cache.put(5, 5)
cache.put(1, 30)
cache.get(11)
cache.put(9, 12)
cache.get(7)
cache.get(5)
cache.get(8)
cache.get(9)
cache.put(4, 30)
cache.put(9, 3)
cache.get(9)
cache.get(10)
cache.get(10)
cache.put(6, 14)
cache.put(3, 1)
cache.get(3)
cache.put(10, 11)
cache.get(8)
cache.put(2, 14)
cache.get(1)
cache.get(5)
cache.get(4)
cache.put(11, 4)
cache.put(12, 24)
cache.put(5, 18)
cache.get(13)
cache.put(7, 23)
cache.get(8)
cache.get(12)
cache.put(3, 27)
cache.put(2, 12)
cache.get(5)
cache.put(2, 9)
cache.put(13, 4)
cache.put(8, 18)
cache.put(1, 7)
cache.get(6)
cache.put(9, 29)
cache.put(8, 21)
cache.get(5)
cache.put(6, 30)
cache.put(1, 12)
cache.get(10)
cache.put(4, 15)
cache.put(7, 22)
cache.put(11, 26)
cache.put(8, 17)
cache.put(9, 29)
cache.get(5)
cache.put(3, 4)
cache.put(11, 30)
cache.get(12)
cache.put(4, 29)
cache.get(3)
cache.get(9)
cache.get(6)
cache.put(3, 4)
cache.get(1)
cache.get(10)
cache.put(3, 29)
cache.put(10, 28)
cache.put(1, 20)
cache.put(11, 13)
cache.get(3)
cache.put(3, 12)
cache.put(3, 8)
cache.put(10, 9)
cache.put(3, 26)
cache.get(8)
cache.get(7)
cache.get(5)
cache.put(13, 17)
cache.put(2, 27)
cache.put(11, 15)
cache.get(12)
cache.put(9, 19)
cache.put(2, 15)
cache.put(3, 16)
cache.get(1)
cache.put(12, 17)
cache.put(9, 1)
cache.put(6, 19)
cache.get(4)
cache.get(5)
cache.get(5)
cache.put(8, 1)
cache.put(11, 7)
cache.put(5, 2)
cache.put(9, 28)
cache.get(1)
cache.put(2, 2)
cache.put(7, 4)
cache.put(4, 22)
cache.put(7, 24)
cache.put(9, 26)
cache.put(13, 28)
cache.put(11, 26)



# cache =LRUCache( 2 )
# # cache.put(1, 1)
# # cache.put(2, 2)
# # cache.get(1)       # returns 1
# # cache.put(3, 3)    # evicts key 2
# # cache.get(2)       # returns -1 (not found)
# # cache.put(4, 4)    # evicts key 1
# # cache.get(1)       # returns -1 (not found)
# # cache.get(3)       # returns 3
# # cache.get(4)       # returns 4

# cache.put(2,1)
# cache.put(2,2)
# cache.get(2)
# cache.put(1,1)
# cache.put(4,1)
# cache.get(2)

