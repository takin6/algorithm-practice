import copy
N = int(input())

graph = []
for i in range(N):
  graph.append( list(map(int,input().split())) )

dp = copy.deepcopy(graph)
for k in range(N):
  for i in range(N):
    for j in range(N):
      dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

res = 0

for i in range(N):
  for j in range(N):
    if dp[i][j] < graph[i][j]:
      print(-1)
      exit()
    elif dp[i][j] == graph[i][j]:
      flg = True
      for k in range(N):
        if k!=i and k!=j and dp[i][j] == dp[i][k]+dp[k][j]:
          flg = False
      if flg:
        res += dp[i][j]

print(res//2)