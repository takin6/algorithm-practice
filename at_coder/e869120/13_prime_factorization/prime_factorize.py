def factorize(n):
  i = 2
  m = n
  factors = []
  
  while i*i <= m:
    if m%i==0:
      m //= i
      factors.append(i)
    else:
      i += 1

  if m > 1:
    factors.append(m)

  return factors

n = int(input())
primes = factorize(n)
print("{0}: {1}".format(n, " ".join(list(map(str,primes)))))