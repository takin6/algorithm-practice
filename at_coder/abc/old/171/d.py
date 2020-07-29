# i回目の操作では、値が Biである要素すべてを Ciに置き換えます。

from collections import Counter
N = int(input())
A = list(map(int,input().split()))
counter = Counter(A)
total = 0
for k,v in counter.items():
  total += k*v
Q = int(input())

for _ in range(Q):
  b,c = map(int,input().split())
  if b in counter:
    total -= b*counter[b]
    item = counter[b]
    del counter[b]
    if c in counter:
      counter[c] += item
      total += c*item
    else:
      counter[c] = item
      total += c*counter[c]
  
  print(total)
