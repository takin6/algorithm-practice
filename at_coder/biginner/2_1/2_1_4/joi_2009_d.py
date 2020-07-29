import itertools
N = int(input())
k = int(input())

cards = [ input() for _ in range(N) ]
s = set()

for i in range(1<<N):

  picked = []
  for j in range(N):
    if (i>>j)&1: picked.append(cards[j])

  if len(picked) == k:
    for product in list(itertools.permutations(picked, k)):
      s.add("".join(product))

print(len(s))