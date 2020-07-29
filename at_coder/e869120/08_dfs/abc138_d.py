import sys
sys.setrecursionlimit(10**6)

N,Q = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(N-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  adj[a].append(b)
  adj[b].append(a)

from collections import defaultdict
counter = defaultdict(int)
for _ in range(Q):
  p,x = map(int,input().split())
  p -= 1
  counter[p] += x

weight = [-1] * N
def dfs(node, wei):
  weight[node] = wei

  for nei in adj[node]:
    if weight[nei] == -1:
      dfs(nei, wei+counter[nei])

dfs(0, counter[0])
print(" ".join(map(str,weight)))