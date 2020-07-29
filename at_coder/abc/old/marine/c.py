# import math
# N,K = map(int,input().split())
# A = [-1]+list(map(int,input().split()))
# B = [0] * (N+1)
# B[0] = -1

# for _ in range(K):
#   for i,a in enumerate(A):
#     if i==0: continue
#     for j in range(max(math.ceil(i-a-0.5),0), min(math.floor(i+a+0.5),N)+1):
#       B[j] += 1

#   A = B[::]
#   B = [0] * (N+1)

# print(" ".join(map(str, A[1:])))

# N,K = map(int,input().split())
# A = list(map(int, input().split()))

# for _ in range(K):
#   B = [0] * (N+1)
#   for i,a in enumerate(A):
#     l = max(0, i-a)
#     r = min(i+a+1, N)
#     B[l] += 1
#     B[r] -= 1

#   for i in range(N):
#     B[i+1] += B[i]

#   if all(b==N for b in B[:-1]): break
#   A = B

# for i in range(N):
#   print(A[i])
# # ==========================--
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
  arr = [0]*(N+1)
  for i, a in enumerate(A):
    left = max(0, i-a)
    right = min(N, i+a+1)
    arr[left] += 1
    arr[right] -= 1
  
  A = list(accumulate(arr[:-1]))
  if all(a == N for a in A):
    break

print(*A, sep=" ")


# for _ in range(K):
#   for i,a in enumerate(A):
#     if i==0: continue
#     for j in range(max(math.ceil(i-a-0.5),0), min(math.floor(i+a+0.5),N)+1):
#       B[j] += 1

#   A = B[::]
#   B = [0] * (N+1)

# print(" ".join(map(str, A[1:])))
# print(" ".join(map(str,A[1:])))

# for _ in range(K):