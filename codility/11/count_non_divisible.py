# from collections import Counter

# def factorization(n):
#   d = n
#   factors = [1]

#   for p in range(2, int(n**0.5+1)+1):
#     if d%p == 0:
#       i = 1
#       while d % p == 0:
#         factors.append((p*i))
#         d //= p
#         i += i

#   factors.append(n)
#   return factors

from collections import Counter,defaultdict

def factorization(n, a_max):  
  factors = []
  for p in range(1, int(n**0.5+1)+1):
    if p > a_max: break
    if n % p == 0:
      factors.append(p)
      if n//p != p: factors.append(n//p)

  return factors

def solution(A):
  # a_max = max(A)
  # counter = Counter(A)
  # memo = defaultdict(int)
  # facs = defaultdict(list)
  # res = [0] * len(A)
  # for i in range(len(A)):
  #   if memo[A[i]]: 
  #     res[i] = memo[A[i]]
  #     continue
 
  #   factors = factorization(A[i], a_max)
  #   cnt = 0
  #   for k,v in counter.items():
  #     if k in factors: cnt += v
  #   memo[A[i]] = res[i] = len(A)-cnt

  # return res

  a_max = max(A)
  counter = Counter(A)

  divisors = {}
  for element in A:
    divisors[element] = set([1,element])

  divisor = 2
  while divisor*divisor <= a_max:
    ele = divisor
    while ele <= a_max:
      if ele in divisors:
        divisors[ele].add(divisor)
        divisors[ele].add(ele//divisor)
      ele += divisor
    divisor += 1

  result = [0]*len(A)
  for idx,ele in enumerate(A):
    result[idx] = (len(A) - sum([counter.get(d,0) for d in divisors[ele]]))

  print(divisors)
  return result

print(solution([3,1,2,3,6]))