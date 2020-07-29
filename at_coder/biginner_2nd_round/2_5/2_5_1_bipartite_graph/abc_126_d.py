import sys
sys.setrecursionlimit(100000)

N = int(input())
adj = [ [] for _ in range(N) ]
for _ in range(N-1):
  u,v,w = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append((v,w))
  adj[v].append((u,w))

color = [None] * N
def dfs(n,l):
  if l%2==0:
    color[n] = 1
  else:
    color[n] = 0

  for nei, nl in adj[n]:
    if color[nei] is not None:
      if (l+nl) % 2 == 0 and color[nei] != 1:
        return False
      if (l+nl) % 2 == 1 and color[nei] != 0:
        return False
    else:
      dfs(nei, l+nl)

  return True

for i in range(N):
  if color[i] is None:
    if not dfs(i,0):
      print(-1)
      exit()

for c in color: print(c)


# if not dfs(0,0):
#   print(-1)
# else:
#   for c in color: print(c)