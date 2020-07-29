# N switches, M bulbs
N,M = map(int,input().split())
K = []
for i in range(M):
  # import pdb; pdb.set_trace()
  lst = list(map(int,input().split()))
  K.append([i-1 for i in lst[1:] ])

P = list(map(int,input().split()))
res = 0

for i in range(1<<N):
  on = []
  for j in range(N):
    if (i>>j)&1:
      on.append(j)

  flg = True
  for m in range(M):
    k = K[m]
    tmp = 0
    for s in k:
      if s in on:
        tmp += 1
    p = P[m]
    if tmp % 2 != p:
      flg = False
      break

  if flg:
    res += 1

print(res)