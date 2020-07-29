from collections import deque
n = int(input())
adj = [ [] for _ in range(n+1) ]
for _ in range(n):
  lst = list(map(int,input().split()))
  if lst[1] > 0:
    adj[lst[0]] = lst[2:]

q = deque([1])
dist = [-1] * (n+1)
dist[1] = 0

q = deque([1])
while q:
  node = q.popleft()

  for nei in adj[node]:
    if dist[nei] != -1: continue
    dist[nei] = dist[node] + 1
    q.append(nei)

for i,s in enumerate(dist):
  if i==0: continue
  print(i, s)


# visited = [False] * (n+1)
# steps = [-1] * (n+1)
# step = -1
# while q:
#   l = len(q)
#   step += 1
#   next_q = deque()

#   for _ in range(l):
#     node = q.popleft()
#     if visited[node]: continue
#     steps[node] = step
#     visited[node] = True
#     for nei in adj[node]:
#       if not visited[nei]:
#         next_q.append(nei)

#   q = next_q

# for i,s in enumerate(steps):
#   if i==0: continue
#   print(i, s)