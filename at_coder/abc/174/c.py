K = int(input())

cnt = set()
k = 7%K
i = 1

while k not in cnt:
  if k == 0:
    print(i)
    exit()

  cnt.add(k)
  k = (10*k+7) % K
  i += 1

print(-1)
