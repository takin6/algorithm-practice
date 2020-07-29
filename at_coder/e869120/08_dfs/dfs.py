N = int(input())
adj_list = [ [] for _ in range(N+1) ]
for _ in range(N):
  lst = list(map(int,input().split()))
  node = lst[0]
  if lst[1] != 0:
    adj_list[node] = lst[2:]


visited = [False] * (N+1)
arrived = [-1] * (N+1)
left = [-1] * (N+1)

time = 0
def dfs(node):
  global time

  arrived[node] = time
  visited[node] = True

  for nei in adj_list[node]:
    if not visited[nei]:
      time += 1
      dfs(nei)
  else:
    time += 1
    left[node] = time

for i in range(1, N+1):
  if not visited[i]:
    time += 1
    dfs(i)

for i in range(1, N+1):
  print(i, arrived[i], left[i])