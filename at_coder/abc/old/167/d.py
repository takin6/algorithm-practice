N,K = map(int,input().split())
A = list(map(int,input().split()))

s = []
# 訪れていない
visited = [-1] * (N+1)
v = 1
while visited[v] == -1: 
  visited[v] = len(s)
  s.append(v)
  # ワープさせる
  v = A[v-1]

# サイクルの長さ
c = len(s) - visited[v]
# はみ出す分の長さ
l = visited[v]

if (K < l): 
  print(s[K])
else:
  K -= l
  K %= c
  print(s[l+K])

# route = [1]
# i = 0
# while True:
#   next = A[i]
#   if next not in route:
#     route.append(next)
#   else:
#     cycle = route[route.index(next):]
#     route = route[:route.index(next)]
#     break

#   i = next-1

# K -= len(route)
# print(cycle[K%len(cycle)])