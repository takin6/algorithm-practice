import sys
sys.setrecursionlimit(10**6)

N,M = map(int,input().split())
relation = [ set() for _ in range(N+1) ]
for _ in range(M):
  x,y = map(int,input().split())
  x -= 1
  y -= 1
  relation[x].add(y)
  relation[y].add(x)

def is_group(temp):
  flg = True
  for m in temp:
    for n in temp:
      if m != n:
        if n not in relation[m]:
          flg = False
          break
  return flg

members = -10**16
for i in range(1<<N):
  temp = []
  for j in range(N):
    if (i>>j)&1:
      temp.append(j)

  if is_group(temp):
    members = max(members, len(temp))

print(members)