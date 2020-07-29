# from itertools import combinations
# from math import gcd
# A,B = map(int,input().split())

# divisors = []
# n,m = min(A,B), max(A,B)
# for i in range(1,int(n**0.5)+1):
#   if n%i==0 and m%i==0:
#     divisors.append(i)
#     p = n//i
#     if m%p==0:
#       divisors.append(p)

# ans = 1
# D = len(divisors)
# for i in range(1,D-1):
#   for j in range(i+1, D):
#     print(i,j)
#     if gcd(divisors[i], divisors[j]) == 1:
#       import pdb; pdb.set_trace()
#       ans += 1

# print(ans)

from collections import Counter
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table

A,B = map(int,input().split())
p1 = Counter(prime_decomposition(A))
p2 = Counter(prime_decomposition(B))
ans = 1
for p,_ in p1.items():
  if p2[p] > 0:
    ans += 1

print(ans)

print(p1,p2)
