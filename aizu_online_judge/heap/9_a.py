import math

n = int(input())
leaves = list(map(int, input().split()))
leaves.insert(0, None)

for i in range(1, n+1):
  detail = ""
  detail += "node {0}: ".format(i)

  key = leaves[i]
  detail += "key = {0}, ".format(key)

  if i / 2 >= 1:
    print(i, math.ceil(i/2))
    detail += "parent key = {0}, ".format(leaves[i // 2])

  if 2 * i <= n:
    detail += "left key = {0}, ".format(leaves[2 * i])

  if (2*i+1) <= n:
    detail += "right key = {0}, ".format(leaves[2 * i + 1])

  print(detail)