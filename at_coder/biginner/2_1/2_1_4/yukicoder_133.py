# import itertools
# from math import factorial

# N = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# total = N*N
# chance = 0

# for p in itertools.permutations(A):
#   for q in itertools.permutations(B):
#     if sum([ p[i] > q[i] for i in range(N) ]) > N//2:
#       chance += 1

# print(chance/factorial(N)**2)


def permutation(lst):
  if len(lst) == 1:
    return [lst]

  l = []

  for i in range(len(lst)):
    m = [lst[i]]

    # import pdb; pdb.set_trace()
    remlist = lst[:i] + lst[i+1:]
    for p in permutation(remlist):
      l.append(m+p)

  return l

print(permutation([1,2,3]))
