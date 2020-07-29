from collections import Counter

N = int(input())
A = list(map(int,input().split()))

S1 = Counter()
S2 = Counter()
for i,a in enumerate(A):
  S1[i+1+a] += 1
  S2[(i+1)-a] += 1

res = 0
for k,v in S1.items():
  if S2[k] > 0:
    res += v*S2[k]

print(res)

