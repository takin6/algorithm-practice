# from collections import defaultdict
# N,M = list(map(int, input().split()))
# adj_list = defaultdict(list)

# for _ in range(M):
#   a,b = list(map(int, input().split()))
#   adj_list[a].append(b)
#   adj_list[b].append(a)


# def dfs(node, visited):
#   if all(visited):
#     return 1

#   res = 0
#   for nei in adj_list[node]:
#     if not visited[nei]:
#       visited[nei] = True
#       res += dfs(nei, visited)
#       visited[nei] = False

#   return res

# cnt = 0
# for node in adj_list[1]:
#   visited = [False]*(N+1)
#   visited[0],visited[1],visited[node] = True,True,True
#   cnt += dfs(node, visited)

# print(cnt)

from collections import defaultdict
N,M = list(map(int, input().split()))
adj_list = defaultdict(list)

for _ in range(M):
  a,b = list(map(int, input().split()))
  adj_list[a].append(b)
  adj_list[b].append(a)


def dfs(node, visited):
  if all(visited):
    return 1

  res = 0
  for nei in adj_list[node]:
    if not visited[nei]:
      visited[nei] = True
      res += dfs(nei, visited)
      visited[nei] = False

  return res

# cnt = 0
# for node in adj_list[1]:
#   visited = [False]*(N+1)
#   visited[0],visited[1],visited[node] = True,True,True
#   cnt += dfs(node, visited)
visited = [False]*(N+1)
visited[0],visited[1] = True,True
print(dfs(1, visited))
# print(cnt)
