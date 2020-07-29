# import itertools

# def prime_factorization(n):
#   seen = []
#   cnt = 0

#   times = 1
#   primes = []
#   while n % 2 == 0:
#     divided = True
#     tmpn = n
#     for _ in range(times):
#       if tmpn%2==0:
#         tmpn //= 2
#       else:
#         divided = False
#         break
#     if divided:
#       seen.append(2**times)
#       times += 1
#       cnt += 1
#       n = tmpn
#     else:
#       break

#   f = 3
#   times = 1
#   divided = True
#   while f*f <= n:
#     tmpn = n
#     for _ in range(times):
#       if tmpn%f==0:
#         tmpn //= f
#       else:
#         divided = False
#         break
#     if divided:
#       seen.append(f**times)
#       times += 1
#       cnt += 1
#       n = tmpn
#     else:
#       f += 2
#       times = 1
#       divided = True

#   if n != 1 and n not in seen:
#     cnt += 1

#   return cnt




# import math

# def eratosthenes(n):
#   primes = [True]*(n+1)
#   primes[0],primes[1] = False,False

#   for i in range(2,int(math.sqrt(n)+1)):
#     if primes[i] == True:
#       # multiple of i
#       j = 2
#       while i*j <= n:
#         primes[i*j] = False
#         j += 1

#   return [ i for i in range(2, n+1) if primes[i] ]

# def replace(n,p):
#   e = 1

#   while p**e <= n:
#     flg = True
#     tmpn = n
#     for _ in range(e):
#       if tmpn%p==0:
#         tmpn //= p
#       else:
#         flg = False
#         break
#     if flg:
#       n = tmpn
#       if p**(e+1) <= n:
#         e += 1
#       else:
#         break
#     else:
#       break

#   return e, n

# n = int(input())
# primes = eratosthenes(n)
# res = 0
# import pdb; pdb.set_trace()
# for p in primes:
#   print(p)
#   if p < n and n%p == 0:
#     e,n = replace(n,p)
#     res += e
#   else:
#     break

# print(res)

# # print(prime_factorization(n))

### これが一番近い  ####
# import math
# def is_prime(x):
#   if x < 2: return False
#   if x == 2 or x == 3 or x == 5: return True 
#   if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False

#   prime = 7
#   step = 4
#   while prime <= math.sqrt(x):
#       if x % prime == 0: return False

#       prime += step
#       step = 6 - step

#   return True

# def prime_factorization(n):
#   d = 2
#   cnt = 0
#   seen = []
#   while d*d <= n:
#     if n%d == 0:
#       t = 1
#       while d**t <= n:
#         if n % (d**t) == 0:
#           seen.append(d**t)
#           n //= (d**t)
#           cnt += 1
#           t += 1
#         else:
#           break
#     d += 1
 
#   if n != 1 and n not in seen:
#     cnt += 1
#   print(seen)
#   return cnt
 
# n = int(input())
# print(prime_factorization(n))

import math
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(math.sqrt(n))+1):
    if temp%i == 0:
      cnt = 0
      while temp%i == 0:
        cnt += 1
        temp //= i
      arr.append([i, cnt])
  if temp != 1:
    arr.append([temp, 1])
  if arr == []:
    arr.append([n, 1])
  return arr

n = int(input())
factors = factorization(n)
res = 0
for j,cnt in factors:
  if j == 1: continue
  i = 1
  while cnt >= i:
    cnt -= i
    i += 1
    res += 1

print(res)

# print(factorization(24))
# print(factorization(64))
# print(factorization(1000007))




# 方針
# 1. eratosthenesの篩で素数を求める
# 2. 素数のn乗を全て

# def fanction(n):
#     listIn = []
#     tmp = n
#     for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
#         if tmp % i == 0:
#             cnt_in = 0
#             while tmp % i ==0:
#                 cnt_in += 1
#                 tmp //= i
#             listIn.append([i, cnt_in])
 
#     if tmp != 1:
#         listIn.append([tmp, 1])
 
#     return listIn
    
# N = int(input())
 
# arr = fanction(N)
# import pdb; pdb.set_trace()
# tmp = 1
# count = 0
# for a, b in arr:
#     while 'true':
#         if b >= tmp:
#             b -= tmp
#             count += 1
#             tmp += 1
#         else:
#             tmp = 1
#             break
 
# print(count)