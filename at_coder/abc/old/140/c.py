N = int(input())
B = list(map(int,input().split()))

A = [None] * N
A[0] = B[0]
for i in range(N-1):
  if i+1 < len(B):
    A[i+1] = min(B[i], B[i+1])
  else:
    A[i+1] = B[i]

print(" ".join(map(str, A)))
print(sum(A))