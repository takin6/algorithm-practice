n = int(input())
A = list(map(int,input().split()))
m = int(input())
q = list(map(int,input().split()))

S = set()
for i in range(1<<n):
  s = 0
  for j in range(n):
    if (i>>j)&1:
      s += A[j]
  S.add(s)


for j in q:
  if j in S:
    print("yes")
  else:
    print("no")