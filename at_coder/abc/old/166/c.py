N,M = map(int,input().split())
H = list(map(int,input().split()))
adj = [ [] for _ in range(N) ]
for _ in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append(v)
  adj[v].append(u)

res = 0
for i in range(N):
   if all([ H[n] < H[i] for n in adj[i]]):
    res += 1

print(res)

# def dfs(n, h, visited):
#   print(n)
#   visited[n] = True

#   for nei in adj[n]:
#     if visited[nei]: continue
#     if H[nei] > h:
#       return False
#     if not dfs(nei, h, visited):
#       return False

#   return True 

# res = 0
# for i in range(1, N):
#   import pdb; pdb.set_trace()
#   if dfs(i, H[i], [False]*N):
#     print(i)
#     res += 1

# print(res)