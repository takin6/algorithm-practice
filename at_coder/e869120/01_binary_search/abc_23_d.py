N = int(input())
baloons = []
for _ in range(N):
  h,s = map(int,input().split())
  baloons.append([h,s])

def is_ok(x):
  T = []
  for h,s in baloons:
    # if x==23: import pdb; pdb.set_trace()
    if x < h: return False
    t = (x-h)/s
    T.append(t)
  T.sort()

  for i in range(N):
    # if x==23: import pdb; pdb.set_trace()
    if T[i] >= i: 
      continue
    else:
      return False

  return True

# X 点を達成できるかどうか
ng,ok = 0,10**6
while abs(ok-ng)>1:
  mid = (ok+ng)//2
  if is_ok(mid):
    ok = mid
  else:
    ng = mid

print(ok)