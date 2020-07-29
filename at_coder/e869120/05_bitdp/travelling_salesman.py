# V,E = map(int,input().split())
# dist = [[float('inf')]*V for _ in range(V)]
# for _ in range(E):
#   u,v,w = map(int,input().split())
#   dist[u][v] = w

# # dp[mask][dest] = weight
# dp = [ [-1]*V for _ in range(1<<V) ]
# VISITED_ALL = (1<<V)-1

# # pos = from, city = dest
# def tsp(mask, pos):
#   print(bin(mask))
#   # print(mask,pos)
#   # when visited all, pos is the destination
#   if mask == VISITED_ALL:
#     return dist[pos][0]

#   if dp[mask][pos] != -1:
#     return dp[mask][pos]

#   ans = float('inf')
#   for city in range(V):
#     # unvisited
#     if (mask&(1<<city)) == 0:
#       newAns = dist[pos][city] + tsp(mask|(1<<city), city)
#       ans = min(ans, newAns)

#   dp[mask][pos] = ans
#   return ans


# res = tsp(1, 0)
# if res == float('inf'):
#   print(-1)
# else:
#   print(res)

# print(dp)


# https://www.youtube.com/watch?v=JE0JE8ce1V0

V,E = map(int,input().split())
dist = [[float('inf')]*V for _ in range(V)]
for _ in range(E):
  s,t,d = map(int,input().split())
  s -= 1
  t -= 1
  dist[s][t] = d

# dp[mask][destination]
dp = [ [-1]*V for _ in range(1<<V) ]
VISITED_ALL = (1<<V)-1

def tsp(mask, pos):
  if mask == VISITED_ALL:
    return dist[pos][0]

  if dp[mask][pos] != -1:
    return dp[mask][pos]

  ans = float('inf')
  for city in range(V):
    if (1<<city)&mask == 0:
      newAns = dist[pos][city] + tsp(mask | (1<<city), city)
      ans = min(ans, newAns)

  dp[mask][pos] = ans
  return ans

res = tsp(1,0)
if res == float('inf'):
  print(-1)
else:
  print(res)
