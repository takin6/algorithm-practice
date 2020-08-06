
# import sys
# sys.setrecursionlimit(10**6)

# class BIT():
#   def __init__(self, n):
#     self.s = [0] * (n+1)
#     self.n = n

#   def add(self, idx, val):
#     while idx < self.n+1:
#       self.s[idx] += val
#       idx += idx&(-idx)

#   def get(self, idx):
#     res = 0
#     while idx > 0:
#       res += self.s[idx]
#       idx -= idx&(-idx)

#     return res

# n = int(input())
# S = [ ord(s)-ord('a') for s in input()[::-1] ]
# bits = [BIT(n) for i in range(26)]

# for i,s in enumerate(S):
#   bits[s].add(i+1,1)

# Q = int(input())
# ans = []
# for _ in range(Q):
#   flg,x,y = map(str, input().split())
#   if flg == "1":
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
#       res += bits[i].get(r) > bits[i].get(l-1)
#     ans.append(res)

# for a in ans: print(a)


class BIT:
  def __init__(self,n):
    self.s = [0]*(n+1)
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
 
bits = [BIT(n) for i in range(26)]
 
for i,s in enumerate(S):
  bits[s].add(1,i+1)
 
Q = int(input())
ans = []
for _ in range(Q):  
  flag,x,y = input().split()

  if flag == "1":
    i = int(x)
    c = ord(y) - ord('a')
    bits[S[i-1]].add(-1,i)
    bits[c].add(1,i)
    S[i-1] = c
  else:
    l = int(x)
    r = int(y)
    res = 0
    for i in range(26):
      res += (bits[i].get(r) > bits[i].get(l-1))
    ans.append(str(res))

print("\n".join(ans))












