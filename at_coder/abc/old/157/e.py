# class BIT:
#   def __init__(self, n):
#     self.s = [0] * (n+1)
#     self.n = n

#   def add(self, i, v):
#     if v == 0 or i < 0: return
#     # i += 1
#     while i < self.n+1:
#       self.s[i] += v
#       i += i&(-i)

#   def sum(self, i):
#     res = 0
#     # i += 1
#     while i > 0:
#       res += self.s[i]
#       i -= i&(-i)
#     return res

# n = int(input())
# S = [ ord(s)-ord('a') for s in input()[::-1] ]

# bits = [ BIT(n) for _ in range(26) ]
# for i,c in enumerate(S):
#   bits[c].add(i+1, 1)

# Q = int(input())
# ans = []
# for _ in range(Q):
#   order,x,y = list(map(str, input().split()))

#   if int(order) == 1:
#     i = int(x)
#     c = ord(y) - ord('a')
#     bits[S[i-1]].add(i, -1)
#     bits[c].add(i, 1)
#     S[i-1] = c
#   else:
#     l = int(x)
#     r = int(y)
#     res = 0
#     for i in range(26):
#       if l==1 and r==7:
#         import pdb; pdb.set_trace()
#       if bits[i].sum(r) > bits[i].sum(l-1):
#         res += 1
#     ans.append(res)

# for a in ans: print(a)
    

class BinaryIndexedTree:
  def __init__(self,n,default = 0):
      self.s = [default]*(n+1)
      self.n = n
  
  def add(self,val,idx):
      while idx < self.n+1:
          self.s[idx] = self.s[idx] + val
          idx += idx&(-idx)
      return
  
  def get(self,idx):
      res = 0
      while idx > 0:
          res = res + self.s[idx]
          idx -= idx&(-idx)
      return res
 
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
 
n = int(input())
S = [ord(s) - ord('a') for s in input()[:-1]]
 
BIT = [BinaryIndexedTree(n) for i in range(26)]
 
for i,s in enumerate(S):
    BIT[s].add(1,i+1)
 
Q = int(input())
ans = []
for _ in range(Q):  
    flag,x,y = input().split()
 
    if flag == "1":
        i = int(x)
        c = ord(y) - ord('a')
        BIT[S[i-1]].add(-1,i)
        BIT[c].add(1,i)
        S[i-1] = c
    else:
        l = int(x)
        r = int(y)
        res = 0
        for i in range(26):
            # print([BIT[i].get(r),BIT[i].get(l)])
            res += (BIT[i].get(r) > BIT[i].get(l-1))
        ans.append(str(res))
print("\n".join(ans))
