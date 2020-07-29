N = int(input())
conditions = [[] for _ in range(N) ]
for i in range(N):
  a = int(input())
  for _ in range(a):
    x,y = map(int,input().split())
    x -= 1
    conditions[i].append([x,y])

res = 0
for i in range(1<<N):
  mapper = {1: [], 0: []}
  flg = True
  cnt = 0
  for j in range(N):
    if (i>>j)&1:
      cnt += 1
      for x,y in conditions[j]:
        if y==1 and not (i>>x)&1:
          flg = False
          break
        elif y==0 and (i>>x)&1:
          flg = False
          break
    if not flg: 
      break

  if flg:
    res = max(res, cnt)

print(res)
