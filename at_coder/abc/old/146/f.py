N,M = map(int,input().split())
S = input()

pos = N
res = []
while pos > 0:
  flg = False
  for move in range(M, 0, -1):
    if pos-move < 0:
      continue
    elif S[pos-move] == "0":
      pos -= move
      res.append(move)
      flg = True
      break
    elif S[pos-move] == "1":
      continue
  else:
    print(-1)
    exit()

print(" ".join(map(str, reversed(res))))