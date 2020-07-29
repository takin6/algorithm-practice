R,C = map(int,input().split())
senbei = []
for i in range(R):
  senbei.append(list(map(int,input().split())))

res = -10**16
for i in range(1<<R):
  to_flip = set()
  for j in range(R):
    if (i>>j)&1:
      to_flip.add(j)

  cnt = 0
  for k in range(C):
    col = [ 1-senbei[r][k] if r in to_flip else senbei[r][k] for r in range(R) ]
    cnt += max(col.count(0), col.count(1))

  res = max(res, cnt)

print(res)