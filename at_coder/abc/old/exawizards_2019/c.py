N,Q = map(int,input().split())
s = input()
q = []
for _ in range(Q):
  t,d = map(str,input().split())
  q.append([t,d])

def check(x):
  for t,d in q:
    if s[x] != t: continue
    if d == "L":
      x -= 1
    else:
      x += 1
    if x < 0: return -1
    if x >= N: return 1
  return 0

# checking left position
ok,ng = -1,N
while abs(ok-ng) > 1:
  x = (ok+ng)//2
  if check(x) == -1:
    ok = x
  else:
    ng = x
left = ok

ng,ok = -1,N
while abs(ok-ng) > 1:
  x = (ok+ng)//2
  if check(x) == 1:
    ok = x
  else:
    ng = x
right = ok

d = 0
if left != -1:
  d += left+1

if right != N:
  d += N - right

print(N-d)
