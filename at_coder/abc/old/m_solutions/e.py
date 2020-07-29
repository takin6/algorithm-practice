N = int(input())
city = []
for i in range(N):
  x,y,p = map(int,input().split())
  city.append((x,y,p))

xx = [ [ abs(city[j][0]) for j in range(N) ] for i in range(2**N) ]
yy = [ [ abs(city[j][1]) for j in range(N) ] for i in range(2**N) ]

for i in range(2**N):
  X = [0]
  rest = []
  for j in range(N):
    if (i>>j)&1:
      X.append(city[j][0])
      xx[i][j] = 0
    else:
      rest.append(j)

  for j in rest:
    res = 10**15
    for k in X:
      res = min(res, abs(city[j][0]-k))
    xx[i][j] = res

for i in range(2**N):
  Y = [0]
  rest = []
  for j in range(N):
    if (i>>j)&1:
      Y.append(city[j][1])
      yy[i][j] = 0
    else:
      rest.append(j)

  for j in rest:
    res = 10**15
    for k in Y:
      res = min(res, abs(city[j][1]-k))
    yy[i][j] = res


ans = [10**15 for _ in range(N+1)]
for i in range(2**N):
  cond = i
  rest = [j for j in range(N) if (i>>j)&1==0]
  count = N-len(rest)

  while True:
    X = cond
    Y = i-cond
    temp = 0
    for j in rest:
      temp += min(xx[X][j], yy[Y][j])*city[j][2]
    ans[count] = min(ans[count], temp)
    if cond == 0:
      break
    else:
      cond = (cond-1)&i

for i in range(N+1):
  print(ans[i])
