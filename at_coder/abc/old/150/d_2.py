import math

N,M = map(int,input().split())
A = [ i//2 for i in list(map(int,input().split()))]

# 各要素について2で割り切れる回数が等しいか
cnt = None
for a in A:
  c = 0
  while a%2==0:
    a//=2
    c += 1

  if cnt is None:
    cnt = c
  else:
    if cnt != c:
      print(0)
      exit()

lcm = 1
for i in range(N):
  g = math.gcd(lcm, A[i])
  lcm = lcm // g*A[i]
  if lcm > M:
    print(0)
    exit()

print(math.ceil(M // lcm / 2))