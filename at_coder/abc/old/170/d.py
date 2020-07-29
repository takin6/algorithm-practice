# def prime_decomposition(n):
#   i = 2
#   table = []
#   while i * i <= n:
#     while n % i == 0:
#       n //= i
#       table.append(i)
#     i += 1
#   if n > 1:
#     table.append(n)
#   return table

# def make_divisors(n):
#   lower_divisors , upper_divisors = [], []
#   i = 1
#   while i*i <= n:
#     if n % i == 0:
#       lower_divisors.append(i)
#       if i != n // i:
#         upper_divisors.append(n//i)
#     i += 1
#   return lower_divisors + upper_divisors[::-1]

# from collections import defaultdict,Counter
# N = int(input())
# A = list(map(int,input().split()))
# A.sort()
# c = Counter(A)
# seen = []
# res = 0

# for a in A:
#   if c[a] > 1: continue
#   flg = False
#   for s in seen:
#     if a % s == 0:
#       flg = True
#       break

#   if flg:
#     continue
#   else:
#     res += 1
#     seen.append(a)

# print(res)
from collections import Counter
N = int(input())
A = list(map(int,input().split()))
A.sort()
c = Counter(A)
lst = [1] * (10**6+1)
res = 0

for i,a in enumerate(A):
  if lst[a] == 0: continue
  if i==N-1 or A[i+1] != a:
    res += 1
  for j in range(a, 10**6+1, a):
    lst[j] = 0

print(res)



# print(A)
# res = 0
# for i,a in enumerate(A):
#   if c[a] > 1: continue
#   table = prime_decomposition(a)
#   counter = Counter(table)
#   flg = False
#   for k,v in counter.items():
#     if seen[k] > 0 and seen[k] <= v:
#       flg = True
#       break

#   if flg:
#     continue
#   else:
#     for k,v in counter.items():
#       seen[k] = v
#     print(a)
#     res += 1

# print(res)

# print(a, table)
# i(1<=i<=N) 
# i!=jである整数jについて、AiはAjで割り切れない

# 24 11 8 3 16
# 3 8 11 16 24
# 3
# => 3,9,27,..
# => 8,16,
# => 11
# => 

# 2 4 8 18 19 28 33 45 86 89
# seen = [2] 
