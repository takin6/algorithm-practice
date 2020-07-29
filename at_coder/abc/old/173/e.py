n,k = map(int,input().split())
A = list(map(int,input().split()))
MOD = 10**9+7
# s=正の数、t=負の数
s,t = [], []
for a in A:
  if a<0:
    t.append(a)
  else:
    s.append(a)

S = len(s)
T = len(t)
ok = False
if (S>0):
  if n==k:
    # すべての負の数をペアにできる
    ok = T%2==0
  else:
    # 負の数は考慮しない
    ok = True
else:
  # kが偶数個
  ok = (k%2==0)

ans = 1
if not ok:
  A.sort(key=lambda x: abs(x))
  for i in range(k):
    ans *= A[i]
    ans %= MOD
else:
  s.sort()
  t.sort(reverse=True)
  if k%2==1:
    ans *= s.pop()
    ans %= MOD

  p = []
  while len(s) >= 2:
    x = s.pop()
    x *= s.pop()
    p.append(x)

  while len(t) >= 2:
    x = t.pop()
    x *= t.pop()
    p.append(x)

  p.sort(reverse=True)
  for i in range(k//2):
    ans *= p[i]
    ans %= MOD

print(ans % MOD)