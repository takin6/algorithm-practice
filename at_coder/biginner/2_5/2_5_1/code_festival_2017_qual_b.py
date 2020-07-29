import sys
sys.setrecursionlimit(100000)

N,M = map(int,input().split())
adj_list = { i: [] for i in range(1, N+1) }

for i in range(M):
  a,b = map(int, input().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

visited = [False]*(N+1)
colors = [None] * (N)
is_bipartite = True

# def dfs(node, c):
#   global is_bipartite
#   colors[node-1] = c
#   visited[node] = True
#   for nei in adj_list[node]:
#     if colors[nei-1] == c:
#       is_bipartite = False
#       return False
#     if not visited[nei]:
#       dfs(nei, 1-c)

#   return True

## improved dfs ###
## ifの条件に再帰を書くのか―... ###
def dfs(node, c):
  colors[node-1] = c
  visited[node] = True
  for nei in adj_list[node]:
    if colors[nei-1] == c:
      return False
    if not visited[nei] and not dfs(nei, 1-c):
      return False

  return True

if dfs(1, 1):
  black = colors.count(1)
  print(black*(N-black) - M)
else:
  print(N*(N-1)//2 - M)

