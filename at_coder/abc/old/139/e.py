from collections import deque

N = int(input())
A = [ deque() for _ in range(N) ]

for i in range(N):
  for aa in list(map(int,input().split())):
    aa -= 1
    A[i].append(aa)

def check(i):
  if len(A[i])==0: return
  j = A[i][0]
  if len(A[j])==0: return

  if A[j][0] == i:
    if j<i: i,j = j,i
    q.add((i,j))

q = set()
for i in range(N):
  check(i)

ans = 0
while q:
  ans += 1

  prevq = q
  q = set()
  for p in prevq:
    i,j = p
    A[i].popleft()
    A[j].popleft()

  for p in prevq:
    i,j = p
    check(i)
    check(j)

for i in range(N):
  if len(A[i]) != 0:
    print(-1)
    exit()

print(ans)
