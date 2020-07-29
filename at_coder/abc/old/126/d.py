N = int(input())
adj = [ [] for _ in range(N) ]
for _ in range(N):
  u,v,w = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append((v,w))
  adj[v].append((u,w))

def dfs(node, w, color):
  colors[node] = color

  for n,nw in adj[node]:
    if colors[n] != -1:
      if (w+nw)%2 == 1 and colors[n] == 0: continue
      if (w+nw)%2 == 0 and colors[n] == 1: continue
      return False
    else:
      nc = 1 if w+nw%2==0 else 0
      if not dfs(node, nw, nc):
        return False

  return True

colors = [-1] * N
for i in range(N):
  if colors[i] == -1:
    dfs(i, 1)

for c in colors: print(c)