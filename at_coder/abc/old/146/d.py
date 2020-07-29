# # Tree G: N verteses
# # 1~N i: a -> b
# # coloring
# # 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
adj = [ [] for _ in range(N) ]
for i in range(N-1):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  adj[a].append((b,i))

res = [None] * (N-1)
def dfs(n, c=-1, p=-1):
  if c==-1 or c>1: 
    nc = 1
  else:
    nc = c+1
  for nei,i in adj[n]:
    if nei == p: continue
    res[i] = nc
    dfs(nei, nc, n)
    nc += 1
    if nc==c: nc += 1

dfs(0)
print(max(res))
for r in res: print(r)

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**9)
# n = int(input())
# E = [[] for _ in range(n)]
# C = [0 for i in range(n-1)]
# for i in range(n-1):
#     a,b = map(int, input().split())
#     E[a-1].append([b-1, i])
#     E[b-1].append([a-1, i])
# c = 1
# def dfs(cur, pre, pre_c):
#   c = 1
#   for e, i in E[cur]:
#     if e != pre:
#       if c == pre_c:
#         c += 1
#       print(e,i)
#       C[i] = c
#       dfs(e, cur, c)
#       c += 1

# dfs(0, -1, 0)
# print(max(C))
# print(C)
# for item in C:
#     print(item)

# q = deque([(0,-1,-1)])
# colors = [None] * N
# while q:
#   new_q = deque([])
#   L = len(q)
#   for _ in range(L):
#     n,c,pc = q.popleft()
#     colors[n] = c

#     if c == -1 or c > 1:
#       nc = 1
#     elif c == 1:
#       nc = 2
#     for nei in adj[n]:
#       new_q.append((nei,nc,c))
#       nc += 1
#       if nc == c: nc += 1

#   q = new_q

# print(len(set(colors[1:])))
# for c in colors[1:]:
#   print(c)