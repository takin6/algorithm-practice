import math
from collections import deque
N,D,A = map(int,input().split())
monsters = sorted([ list(map(int,input().split())) for _ in range(N) ])
monsters = [ [x, math.ceil(h/A)] for x,h in monsters ]
# print(monsters)
que = deque()
cur = 0
ans = 0
for x,h in monsters:
  while que and x > que[0][0]:
    _,n = que.popleft()
    cur -= n

  need = max(0, h-cur)
  ans += need
  cur += need

  if h:
    # 対象のモンスターを最も左端にいることを想定
    que.append([x+2*D, need])

print(ans)