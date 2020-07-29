H,W,K = map(int,input().split())
chocolate = []
for _ in range(H):
  chocolate.append(list(input()))
INF = 10**15
ans = INF

for div in range(1<<(H-1)):
  g = 0
  id = [None] * (H)

  # 列をgroup分け
  for i in range(H):
    id[i] = g
    if (div>>i)&1: g += 1

  # groupごとにwhite chocolateが何個あるのか
  c = [ [0]*W for _ in range(g+1) ]
  for i,block in zip(id, chocolate):
    for j,b in enumerate(block):
      if b == "1":
        c[i][j] += 1

  # 縦方向の列をgroup化する
  now = [0] * (g+1)
  lines = g
  for j in range(W):
    for i in range(g+1):
      now[i] += c[i][j]

    ok = all( n<=K for n in now )
    if not ok:
      lines += 1
      now = [0] * (g+1)
      # 絶対不可能な場合
      for i in range(g+1):
        now[i] += c[i][j]
      ok = all( n<=K for n in now )
      if not ok:
        lines = INF
        break

  ans = min(ans, lines)

print(ans)


# group分けという思考
