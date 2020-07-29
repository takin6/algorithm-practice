class Node():
  def __init__(self, val=None, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next

class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
    self.nodes = {}
  
  def insert(self, val):
    # node=  val, prev, next
    n = Node(val, None, self.head)

    if self.head is not None:
      # prev of current head becomes new node
      self.head.prev = n
      # self.head becomes n
      self.head = n
    else:
      self.head = n
      self.tail = n
  
    if self.nodes.get(val) is None:
      self.nodes[val] = [n]
    else:
      tmp = self.nodes[val]
      tmp.append(n)
      self.nodes[val] = tmp

  def delete(self, val):    
    if val == self.head.val:
      return self.deleteFirst()

    ns = self.nodes[val]
    if ns is not None and len(ns) != 0:
      n = ns.pop(0)
      if n.next is None:
        return self.deleteLast()
      n.prev.next = n.next
      n.next.prev = n.prev
  
  def deleteFirst(self):
    if self.head == self.tail:
      self.head, self.tail = None, None

    if self.head:
      old_head = self.head
      new_head = self.head.next 

      self.head.next = None
      new_head.prev = None

      self.head = new_head

      # delete from nodes
      if self.head is not None:
        self.nodes[old_head.val].remove(old_head)
    return None
  
  def deleteLast(self):
    if self.tail == self.head:
      self.head, self.tail = None, None

    if self.tail:
      new_tail = self.tail.prev

      self.tail.prev = None
      new_tail.next = None

      self.tail = new_tail

      # delete from nodes
      # delete methodでpopしている可能性があるため、あるか確かめる
      if self.tail is not None and self.tail in self.nodes[self.tail.val]:
        self.nodes[self.tail.val].remove(self.tail)
    return None
  
  def __str__(self):
    n = self.head
    tmp = []
    while True:
      tmp.append(str(n.val))
      if n.next is None:
        break
      n = n.next
    
    return " ".join(tmp)

n = int(input())
l = LinkedList()
for i in range(n):

  inp = input().split(" ")
  if len(inp) == 1:
    if inp[0] == "deleteFirst":
      l.deleteFirst()
    elif inp[0] == "deleteLast":
      l.deleteLast()

  if len(inp) == 2:
    m, val = inp
    if m == "insert":
      l.insert(int(val))
    elif m == "delete":
      l.delete(int(val))

print(l)