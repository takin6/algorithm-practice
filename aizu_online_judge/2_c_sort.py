n = int(input())
arr = [ i for i in input().split(" ")]

class Card():
  def __init__(self, c):
    self.c = c
    self.val = int(c[1])
    self.kind = c[0]
  
  def __str__(self):
    return self.c

barr = [ Card(a) for a in arr ]

# bubble sort
for i in range(len(barr)-1):
  
  j = len(barr)-1
  while j > i:
    if barr[j].val < barr[j-1].val:
      tmpj = barr[j]
      barr[j] = barr[j-1]
      barr[j-1] = tmpj
    j = j - 1

bans = [str(i) for i in barr]
print(" ".join(bans))
print("Stable")


#------------------selection sort -------------
sarr = [ Card(a) for a in arr]
for i in range(len(sarr)-1):
  minj = i
  j = len(sarr)-1
  while j >= i+1:
    if sarr[j].val < sarr[minj].val:
      minj = j
    j = j - 1
  
  # if sarr[i].val > sarr[minj].val:
  tmp = sarr[i]
  sarr[i] = sarr[minj]
  sarr[minj] = tmp

sans = [str(i) for i in sarr]
print(" ".join([str(i) for i in sans]))

is_stable = "Stable"
for e in range(len(sans)):
  if sans[e] != bans[e]:
    is_stable = "Not stable"
    break
print(is_stable)