N, K = list(map(int, input().split()))
R, S, P = list(map(int, input().split()))
T = input()
hist = [""] * N
hands = {"r": 1, "s": 2, "p": 3}

total = 0
for i in range(N):
  t = T[i]
  if t == "r":
    h = "p"
    points = P
  elif t == "s":
    h = "r"
    points = R
  elif t == "p":
    h = "s"
    points = S

  if i >= K and hist[i-K] == h:
    continue
  else:
    hist[i] = h
    total += points

print(total)