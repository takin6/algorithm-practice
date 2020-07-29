# 0 ~ N-1
# 4 or 7

# dp[i][t] = 頂点iに時間をnで割ったあまり(time)にいるときの最小時間
import heapq

N,M = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(M):
  u,v,t = map(int,input().split())
  adj[u].append((v,t))
  adj[v].append((t,v))
INF = 10**15
# %4
dp = [ [INF]*4 for _ in range(N+1) ]
dp[0][0] = 0
# time,node
pq = [(0,0)]
while pq:
  t,n = heapq.heappop(pq)

  for nei,nt in adj[n]:
    if 0 < n < N:
      next_time = t+nt
      if next_time < dp[nei][next_time%4]:
        dp[nei][next_time%4] = next_time
