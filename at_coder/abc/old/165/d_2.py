import math
A,B,N = map(int,input().split())
x = min(N, B-1)
print(math.floor(A*x/B)-A*math.floor(x/B))
# res = 0

# for x in range(1, A+1):
#   res = max(res, math.floor(A*x/B)-A*math.floor(x/B))
#   if x == N:
#     print(res)
#     exit()

# print(res)