def LI():
  return list(map(int, input().split()))

N = int(input())
P = LI()
Q = LI()

result = []
def permutations(N, cur):
  if len(cur) == N:
    result.append(cur)
    return

  for i in range(1, N+1):
    if i not in cur:
      permutations(N, cur+[i])

permutations(N,[])
result.sort()
print(abs(result.index(P) - result.index(Q)))

# 1 -> 1,2 -> 1,2,3
# 1 -> 