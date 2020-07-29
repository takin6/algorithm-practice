# def bfs(p, target):
#   visited = []
#   candidates = [p]

#   while len(candidates) > 0:
#     node = candidates.pop(0)
#     if node == target: return True
#     if node in visited: continue
#     visited.append(node)

#     if len(adj_list[node-1]) > 0:
#       for friendCandidate in adj_list[node-1]:
#         candidates.append(friendCandidate)

#   return False


# n_people, n_relationship = list(map(int, input().split()))

# adj_list = [[] for _ in range(n_people)]

# for i in range(n_relationship):
#   p, target = list(map(int, input().split()))
#   adj_list[p-1].append(target)
#   adj_list[target-1].append(p)


# n_q = int(input())
# qs = []

# for i in range(n_q):
#   p, target = list(map(int, input().split()))
#   result = bfs(p, target)

#   if result:
#     print('yes')
#   else:
#     result = bfs(target, p)
#     if result:
#       print('yes')
#     else:
#       print('no')


# ------------- tarjan's algorithm to find the strong connected component values ----------
n_people, n_relationship = list(map(int, input().split()))
adj_list = [[] for _ in range(n_people)]
for i in range(n_relationship):
  p, target = list(map(int, input().split()))
  adj_list[p].append(target)
  adj_list[target].append(p)


group = [-1] * n_people
cnt = 0
for i in range(n_people):
  if group[i] == -1:
    group[i] = cnt
    stack = [i]
    while stack:
      at = stack.pop()
      for to in adj_list[at]:
        if group[to] == -1:
          group[to] = cnt
          stack.append(to)

    cnt += 1

print(group)
for _ in range(int(input())):
    s, t = map(int, input().split())
    print('yes' if group[s] == group[t] else 'no')

# V, E = map(int, input().split())
# edge = [[] for _ in range(V)]
# for _ in range(E):
#     s, t = map(int, input().split())
#     edge[s].append(t)
#     edge[t].append(s)

# group = [-1] * V
# cnt = 0
# for i in range(V):
#   if group[i] == -1:
#     group[i] = cnt
#     stack = [i]
#     while stack:
#       v = stack.pop()
#       for c in edge[v]:
#         if group[c] == -1:
#           group[c] = cnt
#           stack.append(c)
#     cnt += 1

# print(group)
# for _ in range(int(input())):
#     s, t = map(int, input().split())
#     print('yes' if group[s] == group[t] else 'no')


# [0, 0, 1, 1, 0, 0, 2, 2, 3, 3, 2, 3, 3, 3, 3]
# [0, 0, 1, 1, 0, 0, 2, 2, 3, 3, 2, 4, 5, 6, 4]