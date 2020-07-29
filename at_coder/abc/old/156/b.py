
from collections import deque
N, K = list(map(int, input().split()))

i = 0
while N != 0:
  i += 1
  N = N // K

print(i)
