from itertools import permutations
# N = int(input())
# p1 = tuple(map(int,input().split()))
# p2 = tuple(map(int,input().split()))
# lst = [ tuple(p) for p in permutations([i+1 for i in range(N)], N) ]
# lst.sort()

# print(abs(lst.index(p1) - lst.index(p2)))


N = int(input())
p1 = tuple(map(int,input().split()))
p2 = tuple(map(int,input().split()))
def dfs(pair=[]):
  global lst
  if len(pair) == N:
    lst.append(tuple(pair))
  else:
    for j in range(1,N+1):
      if j not in pair:
        pair.append(j)
        dfs(pair)
        pair.pop()

lst = []
dfs()
lst.sort()
print(abs(lst.index(p1) - lst.index(p2)))
# print(len(lst))