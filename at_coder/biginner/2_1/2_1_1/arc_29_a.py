N = int(input())
T = []

for i in range(N):
  T.append(int(input()))


def bit_inverse(n):
  # n = 12
  i = 0
  while i**2 <= n:
    n = n ^ (1 << i)
    i += 1
  return n

ans = float('inf')
patterns = []
for i in range(1 << N):
  inverse = bit_inverse(i)
  if inverse in patterns:
    continue
  else:
    patterns.append(i)

  plate1, plate2 = 0, 0
  for j in range(N):

    if (i>>j)&1:
      plate1 += T[j]
    else:
      plate2 += T[j]

  ans = min(ans, max(plate1, plate2))

print(ans)

# TODO
# - be familiar with bit inverse
# https://www.hackerearth.com/ja/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/
# https://leetcode.com/problemset/all/?topicSlugs=bit-manipulation