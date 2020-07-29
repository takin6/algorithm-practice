from itertools import combinations

while True:
  n,m = map(int,input().split())
  if n==m==0: exit()

  res = 0
  for x,y,z in list(combinations(range(1,n+1), 3)):
    if x+y+z == m: res += 1

  print(res)
