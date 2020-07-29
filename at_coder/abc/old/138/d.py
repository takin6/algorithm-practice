import sys
sys.setrecursionlimit(10**6)
def input():
  return sys.stdin.readline()[:-1]

N,Q = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(N-1):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append(v)
  adj[v].append(u)

scores = [0] * N
for _ in range(Q):
  u,p = map(int,input().split())
  u -= 1
  scores[u] += p

res = [0] * N
def dfs(n, p, s):
  res[n] = s
  for nei in adj[n]:
    if nei != p:
      dfs(nei, n, s+scores[nei])

dfs(0,-1,scores[0])

print(" ".join(map(str, res)))

# import sys
# sys.setrecursionlimit(10**6)


# from collections import deque
# N,Q = map(int,input().split())
# adj = [ [] for _ in range(N) ]
# for _ in range(N-1):
#   u,v = map(int,input().split())
#   u -= 1
#   v -= 1
#   adj[u].append(v)
#   adj[v].append(u)

# scores = [0] * N
# for _ in range(Q):
#   u,p = map(int,input().split())
#   u -= 1
#   scores[u] += p

# res = [0] * N
# visited = [False] * N
# q = deque([(scores[0], 0)])
# while q:
#   s,n = q.popleft()
#   res[n] = s
#   visited[n] = True

#   for nei in adj[n]:
#     if not visited[nei]:
#       q.append((s+scores[nei], nei))

# print(" ".join(map(str, res)))

# https://qiita.com/hoshikawa1309/items/e87068d0e3ceefe4e1c4