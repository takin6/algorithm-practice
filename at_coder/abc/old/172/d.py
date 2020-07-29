def LI():
  return list(map(int,input().split()))


N = int(input())
cumsum = [1] * (N+1)

for i in range(2, N+1):
  for j in range(i, N+1, i):
    cumsum[j] += 1

res = 0
for i in range(1, N+1):
  res += i * cumsum[i]

print(res)


# for i,a in enumerate(A):
#   if lst[a] == 0: continue
#   if i==N-1 or A[i+1] != a:
#     res += 1
#   for j in range(a, 10**6+1, a):
#     lst[j] = 0

# print(res)
