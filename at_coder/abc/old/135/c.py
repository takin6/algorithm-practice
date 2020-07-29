N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

res = 0
for i in range(len(B)):
  res += min(A[i], B[i])
  rem = B[i] - A[i]
  if rem > 0 and i+1 < len(A):
    res += min(A[i+1], rem)
    A[i+1] = max(0, A[i+1]-rem)

print(res)