N,M = map(int,input().split())
bulbs = []
for _ in range(M):
  bulbs.append(list(map(int,input().split())))
P = list(map(int,input().split()))
res = 0
for i in range(1<<N):
  on = []
  for j in range(N):
    if (i>>j)&1:
      on.append(j)

  ok = True
  for i,b in enumerate(bulbs):
    b = [ k-1 for k in b[1:] ]
    p = P[i]
    o = 0
    for s in on:
      if s in b: o += 1
    if o%2 != p:
      ok = False
      break

  if ok:
    res += 1

print(res)
