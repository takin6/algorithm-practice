N = int(input())
A = []
for _ in range(N):
  x,y = list(map(int, input().split()))
  A.append((x,y))

B = []
for _ in range(N):
  x,y = list(map(int, input().split()))
  B.append((x,y))

A = sorted(A, key=lambda x: -x[1])
B = sorted(B, key=lambda x: x[0])
cnt = 0

for bx,by in B:
  can = None
  for i in range(len(A)):
    if A[i][0] < bx and A[i][1] < by:
      can = i
      break

  if can is not None:
    A.pop(can)
    cnt += 1

print(cnt)
