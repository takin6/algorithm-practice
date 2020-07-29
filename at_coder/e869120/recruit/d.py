# from collections import deque
# import heapq

# def dijkstra(s):
#   dist = [float('inf')]*N
#   dist[s] = 0
#   visited = [False] * (N)
#   last_visit = None

#   q = [(0,s)]
#   while q:
#     d,node = heapq.heappop(q)
#     visited[node] = True

#     for nei in range(N):
#       if visited[nei]: continue
#       # if not visited[nei] and nei in must[node]: continue
#       if d + mat[node][nei] < dist[nei]:
#         dist[nei] = d + mat[node][nei]
#         heapq.heappush(q, (dist[nei],nei))

#     last_visit = node

#   return sum(dist), visited

# N = int(input())
# mat = []
# for _ in range(N):
#   mat.append(list(map(int,input().split())))

# M = int(input())
# must = [ [] for _ in range(N) ]
# for _ in range(M):
#   s,t = map(int,input().split())
#   s -= 1
#   t -= 1
#   must[t].append(s)

# ans = float('inf')
# for i in range(N):
#   new, visited = dijkstra(i)
#   print(i, new, all(visited))
#   if not all(visited): continue
#   ans = min(new, ans)

# print(ans)


### 2nd attempt: topological sort ###
# from collections import deque
# N = int(input())
# mat = []
# for _ in range(N):
#   mat.append(list(map(int,input().split())))

# M = int(input())
# must = [ [] for _ in range(N) ]
# for _ in range(M):
#   s,t = map(int,input().split())
#   s -= 1
#   t -= 1
#   must[t].append(s)

# def topological_sort(node):
#   visited[node] = True

#   for nei in must[node]:
#     if not visited[nei]:
#       topological_sort(nei)

#   order.append(node)

# visited = [False] * N
# orders = []

# for i in range(N):
#   order = deque([])
#   topological_sort(i)
#   for j in range(N):
#     if not visited[j]:
#       topological_sort(j)
#   if all(visited) and order not in orders:
#     orders.append(order)
#   visited = [False]*N
#   order = deque([])

# for order in orders:
#   print(order)

# ans = float('inf')
# for order in orders:
#   dist = [float('inf')] * N
#   dist[order[0]] = 0
#   while order:
#     i = order.popleft()
#     for nei in range(N):
#       if nei == i or nei in must[i]: continue
#       if dist[nei] > dist[i] + mat[i][nei]:
#         dist[nei] = dist[i] + mat[i][nei]
#   ans = min(ans, sum(dist))

# print(ans)



### 3rd attempt: travelling salesman ###
from collections import deque

N = int(input())
mat = []
for _ in range(N):
  mat.append(list(map(int,input().split())))

M = int(input())
must = [ [] for _ in range(N) ]
for _ in range(M):
  s,t = map(int,input().split())
  s -= 1
  t -= 1
  must[t].append(s)

dp = [ [-1]*N for _ in range(1<<N) ]
dist = [float('inf')] * N
VISITED_ALL = (1<<N)-1
def tsp(mask, pos):
  if dp[mask][pos] > 0: return dp[mask][pos]

  if mask == VISITED_ALL: return 0

  ans = float('inf')
  for i in range(N):
    if mask&(1<<i) > 0: continue
    flg = True
    for m in must[i]:
      if mask&(1<<m) == 0:
        flg = False
    if flg:
      newAns = mat[pos][i] + tsp(mask|(1<<i), i)
      ans = min(ans,newAns)

  dp[mask][pos] = ans
  return ans

res = tsp(1,0)
print(res)


  #   ans = float('inf')
  # for city in range(V):
  #   if (1<<city)&mask == 0:
  #     newAns = dist[pos][city] + tsp(mask | (1<<city), city)
  #     ans = min(ans, newAns)

  # dp[mask][pos] = ans
  # return ans