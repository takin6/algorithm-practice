from itertools import accumulate
from collections import defaultdict

N,K = map(int,input().split())
A = list(map(int,input().split()))

S = [0] + list(accumulate(A))
S = [ s%K for s in S ]

ans = 0
counter = defaultdict(int)
queue = []
for i,s in enumerate(S):
  t = (s-i) % K

  ans += counter[t]
  counter[t] += 1

  queue.append(t)
  if len(queue) >= K:
    counter[queue[0]] -= 1
    queue.pop(0)

print(ans)

# https://hiramekun.hatenablog.com/entry/2019/11/30/115331
