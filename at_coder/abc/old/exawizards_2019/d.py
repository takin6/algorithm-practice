x = [i for i in range(49991, 50000)]

ans = 1
for e in x:
  ans += e
  ans %= 10**9+7
print(ans % 10**9+7)