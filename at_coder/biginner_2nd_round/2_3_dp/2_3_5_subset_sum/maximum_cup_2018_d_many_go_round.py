# dp[i] = それぞれを調べたときにiにたどり着くことができる最終回数
# dp = [float('inf')] * (M)
# dp[0] = 1
# A = list(map(int,input().split()))
# for i in range(N):
#   # for j in range(M):
#   for j in range(M-1,-1,-1):
#     if A[i]==9 and j==9: import pdb; pdb.set_trace()
#     if j == A[i]:
#       dp[j] = min(dp[j], 1)
#     # if A[i]==9 and j==9: import pdb; pdb.set_trace()
#     dp[(j+A[i])%M] = min(dp[(j+A[i])%M], dp[j]+((j+A[i])//M))

N,M,L,X = map(int,input().split())
dp = [ [X+1]*(M) for _ in range(N+1) ]
dp[0][0] = 1
A = list(map(int,input().split()))

for i in range(N):
  for j in range(M):
    if dp[i][j] == X+1: continue

    a = A[i]
    # if j == a:
    #   dp[i+1][j] = min(dp[i+1][j], 1)
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    dp[i+1][(j+a)%M] = min(dp[i][(j+a)%M], dp[i][j]+((j+a)//M))

if dp[-1][L] <= X:
  print("Yes")
else:
  print("No")


# [[1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
#  [1, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf],
# [1, 1, inf, inf, 1, 1, inf, inf, inf, inf, inf], 
# [1, 1, inf, inf, 1, 1, 1, inf, inf, 1, 1],
# [1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1], 
# [1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1]
# ]