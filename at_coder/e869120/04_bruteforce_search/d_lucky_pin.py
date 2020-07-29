# from itertools import combinations
# N = int(input())
# S = input()

# res = set()
# for pair in combinations(range(N), 3):
#   res.add("".join([S[i] for i in pair]))

# print(len(res))

from itertools import product
N = int(input())
S = input()
res = 0
for pair in product(range(10), repeat=3):
  s = S[::]
  found = True
  for i,num in enumerate(pair):
    idx = s.find(str(num))
    if idx == -1:
      found = False
      break
    else:
      if idx+1 == N:
        if i != len(pair)-1:
          found = False
        break
      s = s[idx+1:]

  if found:
    res += 1

print(res)