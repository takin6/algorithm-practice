from collections import Counter
N,K,Q = map(int,input().split())
counter = Counter()
for _ in range(Q):
  counter[int(input())] += 1

for i in range(1, N+1):
  p = counter[i]
  if K+p-Q > 0:
    print("Yes")
  else:
    print("No")