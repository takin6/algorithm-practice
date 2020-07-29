import sys
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append(v)
  adj[v].append(u)

color = [None] * N
def dfs(n, c):
  color[n] = c
  for nei in adj[n]:
    if color[nei] is not None:
      if color[nei] == c: 
        return False
    elif not dfs(nei, 1-c):
      return False
    # else:
    #   dfs(nei, 1-c)

  return True

if dfs(0,1):
  import pdb; pdb.set_trace()
  print(color.count(1)*color.count(0) - M)
else:
  print(N*(N-1)//2 - M)
