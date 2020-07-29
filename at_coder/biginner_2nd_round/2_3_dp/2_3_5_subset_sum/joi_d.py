import heapq
from collections import deque

N,M,X = map(int,input().split())
H = [0]
for i in range(N):
  H.append(int(input()))

adj_list = [ [] for _ in range(N+1)]
for _ in range(M):
  u,v,c = map(int,input().split())
  # adj_list[u].append((v,c))
  # adj_list[v].append((u,c))
  if H[u] >= c: adj_list[u].append((v,c))
  if H[v] >= c: adj_list[v].append((u,c))

INF = float('inf')
visited = [False] * (N+1)
costs = [INF] * (N+1)

# q=time,neighbor,cur_h
q = [(0,1,X)]
costs[1] = 0
last_position = 0
while q:
  cost,n,h = heapq.heappop(q)
  visited[n] = True
  if n == N: 
    last_position = h
    break

  for nei,nc in adj_list[n]:
    if visited[nei]: continue
    # p-nt < 0        => ntの高さまで上る
    # p-nt > H[nei]   => 最低限下りられるところまで
    #    　　　　　       もしも下りられなかったらFalse
    # 0 <= p-nt <= nt => 普通に飛び移れる
    if h-nc < 0:
      # import pdb; pdb.set_trace()
      climbUp = (nc-h)
      if climbUp > H[n]: continue
      nextCost = cost + climbUp + nc
      nextH = 0
    elif h-nc > H[nei]:
      # import pdb; pdb.set_trace()
      climbDown = (h-(H[nei]+nc))
      if climbDown < 0: continue
      nextCost = cost + climbDown + nc
      nextH = H[nei]
    else:
      nextCost = cost + nc
      nextH = h - nc
    
    if nextCost < costs[nei]:
      costs[nei] = nextCost
      heapq.heappush(q, (nextCost, nei, nextH))
    # print(q)

if costs[N] == INF:
  print(-1)
else:
  print(costs[N] + H[N]-last_position)


# これと比較して何が足りないのかを考えよう。。。。 ###
# https://atcoder.jp/contests/joi2014ho/submissions/7843457