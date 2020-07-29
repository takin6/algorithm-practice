from collections import deque
import heapq
N,K = map(int,input().split())
A = list(map(int,input().split()))
res = 0
# 左からa個
for a in range(N+1):
  # 右からb個
  for b in range(N+1):
    if a+b>N or a+b>K: continue
    hands = []
    A1 = deque(A[::])
    for _ in range(a):
      hands.append(A1.popleft())
    for _ in range(b):
      hands.append(A1.pop())
    hands.sort()
    hands = deque(hands)
    rem = K - a - b
    for _ in range(rem):
      if hands and hands[0] < 0:
        hands.popleft()
      else:
        break
    res = max(res, sum(hands))

print(res)
# dp[i][j][k] = i番目のものまでをとった結果、