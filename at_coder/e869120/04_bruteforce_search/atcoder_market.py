N = int(input())
A = []
B = []
for _ in range(N):
  a,b = list(map(int,input().split()))
  A.append(a)
  B.append(b)

middle = sum([abs(A[i]-B[i]) for i in range(N) ])

east = 10**16
for a in A:
  cur = 0
  for i in range(N):
    cur += abs(A[i] - a)
  east = min(east, cur)


west = 10**16
for b in B:
  cur = 0
  for i in range(N):
    cur += abs(B[i] - b)
  west = min(west, cur)

print(east,middle,west)
print(east+middle+west)