# fs = [0] * (1000001)
# fs[0],fs[1] = 1,1

# for i in range(2, int(math.sqrt(10**7)+1)):
#   seq = []
#   for j in range(2, i):

#     if primes[i]:
#       j = 2
#       while i*j <= 10**5:
#         primes[i*j] = False
#         j += 1

# n = int(input())
import math

# def prime_factors(n):
#   factors = []
#   primes = [True]*(n+1)
#   primes[0],primes[1] = False,False

#   p = 2
#   while p*p <= n:
#     if primes[p]:
#       factors.append(p)
#       for i in range(p*2, n+1, p):
#         primes[i] = False
#     p += 1

#   return [ i for i in range(2,n+1) if primes[i] ]

# def prime_factors(n):
#   num = n
#   i = 2
#   factors = []
#   while i*i <= n:
#     if n%i == 0:
#       factors.append(i)
#       while n!=1 and n%i == 0:
#         n //= i
#     i += 1

#   if not factors: factors.append(num)
#   return factors

# t = int(input())
# nums = []
# m = -10*100
# for i in range(t):
#   n = int(input())
#   m = max(n, m)
#   nums.append(n)

# oiler = [0,1]
# for i in range(2, m+1):
#   factors = prime_factors(i)
#   tmp = i
#   for j in factors:
#     tmp = tmp * (1 - (j**-1))
#   oiler.append(oiler[i-1]+tmp)

# for i in nums:
#   print(int(oiler[i]+1))

from itertools import accumulate

N = 1000001
table = list(range(N+1))
# => table = [ i for i in range(N+1) ]
for i in range(2, N+1):
  if table[i] == i:
    for j in range(i, N+1, i):
      table[j] *= 1-1/i

table[0] = 1
ans = list(accumulate(table))
for i in range(INT()):
    a = INT()
    print(int(ans[a]))


# table[0] = 0
# ans = list(accumulate(table))
# for i in range(int(input())):
#   a = int(input())
#   print(int(ans[a]))