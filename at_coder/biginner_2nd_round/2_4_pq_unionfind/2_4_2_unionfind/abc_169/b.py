n = int(input())
A = list(map(int,input().split()))

if 0 in A:
  print(0)
  exit()

res = 1
for e in A:
  res = res * e
  if res > 10**18:
    print(-1)
    exit()

print(res)


# TLE
# 0が入っていたら即Return
# 他は