class LinkedList():
  def __init__(self, val=None, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next
  
  def insert(self, val):
    n = LinkedList(val, None, self)
    self.prev = n
    return n

  def delete(self, val):
    l = self
    found = False
    while True:
      if l.val == val:
        item = l
        found = True
        break
      else:
        if l.next is None:
          break
        l = l.next
      
    if not found:
      return self

    if item.prev is None:
      l.next.prev = None
      return l.next
    
    elif item.next is None:
      l.prev.next = None
      return self
    
    else:
      l.prev.next = l.next
      l.next.prev = l.prev
      return self
  
  def deleteFirst(self):
    if self.next:
      self.next.prev = None
      return self.next
    return None
  
  def deleteLast(self):
    l = self
    while l.next is not None:
      l = l.next
    
    if l.prev:
      l.prev.next = None
      return self
    return None
  
  def __str__(self):
    l = self
    tmp = []
    while True:
      tmp.append(str(l.val))
      if l.next is None:
        break
      l = l.next
    
    return " ".join(tmp)

n = int(input())
l = None
for i in range(n):

  inp = input().split(" ")
  if len(inp) == 1:
    if inp[0] == "deleteFirst":
      l = l.deleteFirst()
    elif inp[0] == "deleteLast":
      l = l.deleteLast()

  if len(inp) == 2:
    m, val = inp
    if m == "insert":
      if l is None: 
        l = LinkedList(int(val))
      else:
        l = l.insert(int(val))
    elif m == "delete":
      l = l.delete(int(val))

ans = []
while True:
  ans.append(str(l.val))
  if l.next is None: 
    break
  else:
    l = l.next

print(" ".join(ans))
