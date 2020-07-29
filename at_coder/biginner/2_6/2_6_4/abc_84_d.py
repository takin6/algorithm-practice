# sieve of eratosthenes with cumulative sums
import math
primes = [True]*(10**5+1)
primes[0],primes[1] = False,False
cumsum = [0]*(10**5+1)

for i in range(2, int(math.sqrt(10**5)+1)):
  if primes[i]:
    j = 2
    while i*j <= 10**5:
      primes[i*j] = False
      j += 1

for i in range(2, 10**5+1):
  if primes[i] and primes[(i+1)//2]:
    cumsum[i] = cumsum[i-1]+1
  else:
    cumsum[i] = cumsum[i-1]

Q = int(input())
for _ in range(Q):
  l,r = map(int,input().split())
  print(cumsum[r]-cumsum[l-1])