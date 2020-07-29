from itertools import combinations
N,M = map(int,input().split())
A = []
for _ in range(N):
  A.append(list(map(int,input().split())))

res = 0
for x,y in list(combinations(range(M), 2)):
  score = 0
  for i in range(N):
    score += max(A[i][x], A[i][y])
  res = max(res, score)

print(res)