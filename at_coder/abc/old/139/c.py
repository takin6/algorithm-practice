N = int(input())
A = list(map(int,input().split()))

res = 0
j = 0
prev = A[0]
for i in range(1, N):
  if A[i] <= prev:
    j += 1
    prev = A[i]
  else:
    res = max(res, j)
    j = 0
    prev = A[i]

print(max(res, j))