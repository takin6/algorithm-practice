# from collections import deque
# import bisect

# N = int(input())
# A = list(map(int,input().split()))
# adj = [ [] for _ in range(N+1) ]
# for _ in range(N-1):
#   a,b = map(int,input().split())
#   adj[a].append(b)
#   adj[b].append(a)

# res = [ [] for _ in range(N+1) ]
# res[1] = [1]

# def LIS(n, path):
#   swapped = 0
#   dp = []
#   for i in path:
#     if len(dp) == 0 or i > dp[-1]:
#       dp.append(i)
#     else:
#       dp[bisect.bisect_left(dp, i)] = i
#       swapped += 1
#   res[n] = dp

import sys
sys.setrecursionlimit(10**6)
from bisect import bisect_left
 
# N = int(input())
# A = list(map(int,input().split()))
N = int(sys.stdin.buffer.readline())
A =  [int(x) for x in sys.stdin.buffer.readline().split()]
adj = [ [] for _ in range(N+1) ]
for _ in range(N-1):
  # a,b = map(int,input().split())
  a,b =  [int(x) for x in sys.stdin.buffer.readline().split()]
  a -= 1
  b -= 1
  adj[a].append(b)
  adj[b].append(a)
 
INF = 10**15
# dp = [ INF for _ in range(2*10**5+1)]
dp = [INF]*(2*10**5+1)
dp[0] = -INF
ans = [None]*(N)
 
def dfs(v, p=-1):
  i = bisect_left(dp, A[v])
  old = dp[i]
  dp[i] = A[v]
  ans[v] = i
  if p!=-1: ans[v] = max(ans[v], ans[p])
 
  for u in adj[v]:
    if u == p: continue
    dfs(u, v)
 
  dp[i] = old
 
dfs(0)
for i in range(N):
  print(ans[i])


# https://atcoder.jp/contests/abc165/submissions/12639403
# DFSをQを使って実装した例
# https://evolite.hatenablog.com/entry/20200507/1588849206