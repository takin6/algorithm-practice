n = 15

import math

primes = [True]*(n+1)
primes[0],primes[1] = False,False

for i in range(2,int(math.sqrt(n)+1)):
  if primes[i] == True:
    # multiple of i
    j = 2
    while i*j <= n:
      primes[i*j] = False
      j += 1

for i in range(2, n+1):
  if primes[i] == True: print(i)
print("total: ", primes.count(True))

# O(n*loglogn) + O(n)
# = O(n*loglogn)