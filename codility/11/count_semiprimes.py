

# def solution(N, P, Q):
#     primes = [True] * (N+1)
#     primes[0],primes[1] = False,False
#     p = 2
#     while p*p <= N:
#       if primes[p] == True:
#         for i in range(p*2, N+1, p):
#           primes[i] = False
#       p += 1
#     primes = [ i for i in range(2, N+1) if primes[i] ]
#     primes.append(1)
#     semiprimes = set()
#     for p1 in primes:
#       for p2 in primes:
#         semiprimes.add(p1*p2)
#     semiprimes = sorted(list(semiprimes))

#     m = max(max(P), max(Q))
#     cumsum = [0] * (m+1)
#     for i in range(m+1):
#       if i in semiprimes:
#         cumsum[i] = cumsum[i-1]+1
#       else:
#         cumsum[i] = cumsum[i-1]

#     m = max(max(P), max(Q))
#     cumsum = [0] * (m+1)
#     for i in range(m+1):
#       if i in semiprimes:
#         cumsum[i] = cumsum[i-1]+1
#       else:
#         cumsum[i] = cumsum[i-1]

#     M = len(P)
#     res = [0] * M
#     for i in range(M):
#       res[i] = cumsum[Q[i]] - cumsum[P[i]-1]

#     return res

def solution(N, P, Q):
  primes = [True] * (N+1)
  primes[0],primes[1] = False,False
  p = 2
  while p*p <= N:
    if primes[p] == True:
      for i in range(p*2, N+1, p):
        primes[i] = False
    p += 1
  primes = [ i for i in range(2, N+1) if primes[i] ]

  semiprimes = [0] * (N+1)
  for idx1 in range(len(primes)):
    for idx2 in range(idx1, len(primes)):
      if primes[idx1]*primes[idx2] > N: break
      semiprimes[primes[idx1]*primes[idx2]] = 1

  for idx in range(1, N+1):
    semiprimes[idx] += semiprimes[idx-1]

  M = len(P)
  res = [0] * M
  for i in range(M):
    res[i] = semiprimes[Q[i]] - semiprimes[P[i]-1]

  return res


print(solution(26, [1,4,16], [26,10,20]))