import bisect
from collections import deque
N = int(input())
A = deque([])
for i in range(N):
  A.append(int(input()))

dp = deque([])
l = len(A)
for i,a in enumerate(A):
  pos = bisect.bisect_left(dp, a)-1
  if pos<0:
    dp.appendleft(a)
  else:
    dp[pos] = a

print(len(dp))