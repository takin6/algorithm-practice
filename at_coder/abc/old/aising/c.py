from collections import Counter
N = int(input())
MAX_INT = 10**4+1
cumsum = [0] * (MAX_INT)

# 3~6
for i in range(3, 150):
  seen = []
  for n in range(1, i+1):
    for m in range(n, i+1):
      k = i - n - m
      if k <= 0: continue
      tmp = [n,m,k]
      tmp.sort()
      if tmp in seen: continue
      seen.append(tmp)

      p = i*i - (n*m + m*k + k*n)
      if p >= MAX_INT: break
      l = len(list(set(tmp)))
  
      if l==3:
        add = 6
      elif l==2:
        add = 3
      else:
        add = 1

      cumsum[p] += add
      
for i in range(1, N+1):
  print(cumsum[i])