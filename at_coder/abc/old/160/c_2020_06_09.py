# 7-4 = 3
# 3-4 = 1
# 1-4 = 3
# 3-4 = 1

# 7-4 = 3
# 7-8 = 1
# 7-12 = 5
# 7-16 = 9

N,M = map(int,input().split())
seen = []

res = N
cur = N
while cur not in seen:
  seen.append(cur)
  cur = abs(cur - M)
  res = min(res, cur)

print(res)