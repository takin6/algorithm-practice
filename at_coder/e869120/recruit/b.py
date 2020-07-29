import bisect

N,M = map(int,input().split())
R = []
for _ in range(M):
  a,b = map(int,input().split())
  R.append([a,b])

Q = int(input())
for _ in range(Q):
  c,d = map(int,input().split())

  flg = True
  for r in R:
    # 既存の区間の内側に新しい区間がいる場合
    if r[0] <= c <= r[1] or r[0] <= d <= r[1]:
      flg = False
      break
    # 既存の区間の外側に新しい区間がいて、かつ、既存の区間を含んでいる場合
    if c <= r[0] <= d or c <= r[1] <= d:
      flg= False
      break

  if not flg:
    print("NG")
  else:
    R.append([c,d])
    print("OK")

# C,D = [],[]
# Q = int(input())
# for _ in range(Q):
#   c,d = map(int,input().split())
#   C.append(c)
#   D.append(d)

# for i in range(Q):
