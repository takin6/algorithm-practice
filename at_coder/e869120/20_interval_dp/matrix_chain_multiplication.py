N = int(input())
m = []
for i in range(N):
  x,y = map(int,input().split())
  m.append((x,y))

dp = [ [0]*N for _ in range(N) ]

for L in range(1,N): 
  for i in range(N-L): 
    j = i+L
    dp[i][j] = float('inf')
    for k in range(i,j):
      m0,m1,m2 = m[i],m[k],m[j]
      # print(i,j,k,m0,m1,m2)
      dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+m0[0]*m1[1]*m2[1])

print(dp[0][-1])

# for l in range(1,N):
#   for i in range(N):
#     j = i+l
#     if j >= N: break

#     for k in range(i, j):
#       m0,m1,m2 = matrix[i],matrix[k],matrix[k+1]
#       new = dp[i][k] + dp[k+1][j] + m0[0]*m1[1]*m2[1]
#       dp[i][j] = min(dp[i][j], new)

# for d in dp:
#   print(d)