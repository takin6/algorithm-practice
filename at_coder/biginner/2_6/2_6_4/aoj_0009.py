import sys
import math
primes = [True]*(10**6+1)
primes[0],primes[1] = False,False
cumsum = [0]*(10**6+1)

for i in range(2, int(math.sqrt(10**5)+1)):
  if primes[i]:
    j = 2
    while i*j <= 10**5:
      primes[i*j] = False
      j += 1

for i in range(2, 10**6+1):
  if primes[i]:
    cumsum[i] = cumsum[i-1]+1
  else:
    cumsum[i] = cumsum[i-1]


while True:
  try:
    print(cumsum[int(input())])
  except:
    break


# while True:
#   try:
#      print(cumsum[int(input())])
#   except:
#     break