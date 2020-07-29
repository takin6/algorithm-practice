# n未満の場合

import math
n = int(input())
if n == 1:
  print(0)
  exit()

primes = [True]*(n)
primes[0],primes[1] = False,False

for i in range(2, int(math.sqrt(n)+1)):
  if primes[i]:
    j = 2
    while i*j < n:
      primes[i*j] = False
      j += 1

print(primes.count(True)) 
# print([ i for i in range(0, n) if primes[i] ])



# def sieve(n):
#   ass = []
#   is_prime = [True]*(n+1)
#   is_prime[0] = False
#   is_prime[1] = False
  
#   for i in range(2, int(n**0.5)+1):
#     if not is_prime[i]:
#       continue
#     for j in range(i*2, n+1, i):
#       is_prime[j] = False
#   for i in range(n+1):
#     if is_prime[i]:
#       ass.append(i)
#   return(ass)
 
# n = int(input())
# if n == 1:
#   print(0)
#   exit()
# print(len(sieve(n-1)))