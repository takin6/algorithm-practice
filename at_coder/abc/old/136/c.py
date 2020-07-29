# N, H
# -1 or no

N = int(input())
A = list(map(int,input().split()))

for i in range(1, N):
  if A[i] > A[i-1]:
    A[i] -= 1
  
  if A[i] - A[i-1] < 0:
    print("No")
    exit()

print("Yes")

# at_least = A[-1]
# for i in range(N-2, -1, -1):
#   if A[i] > at_least:
#     if A[i]-1 > at_least:
#       print("No")
#       exit()

# print("Yes")