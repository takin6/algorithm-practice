D,N = map(int,input().split())
T = [ int(input()) for i in range(D) ]
clothes = []
for _ in range(N):
  a,b,c = map(int,input().split())
  clothes.append([a,b,c])

# i日目に服jを来た時の、派手さの絶対値
dp = [ [-1]*(N) for _ in range(D+1) ]
dp[0][0] = 0

for j in range(N):
  a,b,c = clothes[j]
  if a <= T[0] <= b:
    dp[1][j] = c

for i in range(2, D+1):
  for j in range(N):
    a,b,c = clothes[j]
    if a <= T[i-1] <= b:
      for k in range(N):
        if dp[i-1][k] > -1:
          prev_c = clothes[k][2]
          if i > 2:
            dp[i][j] = max(dp[i][j], dp[i-1][k]+abs(prev_c-c))
          else:
            dp[i][j] = max(dp[i][j], abs(prev_c-c))

print(max(dp[-1]))
for d in dp:
  print(d)