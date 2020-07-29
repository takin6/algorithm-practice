
n = int(input())

vertex = [ i+1 for i in range(n) ]
adj_list = [ list(map(int, input().split())) for _ in range(n) ]
depths = [None] * n

def BFS():
  visited = []
  nextToVisit = [(1, 0)]

  while len(nextToVisit) > 0:
    node, depth = nextToVisit.pop(0)

    if node in visited: continue

    depths[node-1] = depth
    visited.append(node)

    if adj_list[node-1][1] > 0:
      for next_node in adj_list[node-1][2:]:
        nextToVisit.append((next_node, depth+1))

BFS()

for i in range(n):
  if depths[i] is None:
    print(i+1, -1)
  else:
    print(i+1, depths[i])
