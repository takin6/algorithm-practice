# K, S = list(map(int, input().split()))

# res = 0

# for x in range(K+1):

#   for y in range(min(S-x, K+1)):

#     for z in range(min(S-x-y, K+1)):

#       if x + y + z == S:
#         res += 1

K, S = list(map(int, input().split()))

res = 0

for x in range(K+1):
  for y in range(K+1):
    z = S - x - y
    if z >= 0 and z <= K:
      res += 1

print(res)