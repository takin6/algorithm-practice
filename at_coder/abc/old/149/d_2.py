N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
win_hand = { "r": P, "s": R, "p": S }
prev_hand = {}
LOST,WON = -1,1

points = 0
for i in range(N):
  if i-K >= 0:
    if T[i] != T[i-K]:
      prev_hand[i] = WON
      points += win_hand[T[i]]
    else:
      if prev_hand[i-K] == WON:
        prev_hand[i] = LOST
      else:
        points += win_hand[T[i]]
        prev_hand[i] = WON
  else:
    prev_hand[i] = WON
    points += win_hand[T[i]]

print(points)