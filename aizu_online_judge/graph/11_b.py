
n = int(input())

vertex = [ i+1 for i in range(n) ]
adj_list = [ list(map(int, input().split())) for _ in range(n) ]

d = [0] * n
f = [0] * n

current_time = 1

def dfs(source, visited):
  global current_time
  # visitedは0 indexのため
  source -= 1

  if source in visited: return
  d[source] = current_time
  visited.append(source)
  current_time += 1

  if adj_list[source][1] > 0:
    for node in adj_list[source][2:]:
      dfs(node, visited)

  f[source] = current_time
  current_time += 1

  return visited

visited = []
for i in range(n):
  if i in visited:
    continue
  visited = dfs(i+1, visited)

for i in range(n):
  print(vertex[i], d[i], f[i])