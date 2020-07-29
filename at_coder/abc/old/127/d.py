#### 
# N,M = map(int,input().split())
# A = list(map(int,input().split()))
# A.sort()

# cards = []
# for _ in range(M):
#   b,c = map(int,input().split())
#   cards.append([c,b])
# cards.sort(key=lambda x: -x[0])

# res = 0
# idx = 0
# left = cards[idx][1]
# for i,a in enumerate(A):
#   if a > cards[idx][0]:
#     res += sum(A[i:])
#     break
#   else:
#     res += cards[idx][0]

#     left -= 1
#     if left <= 0:
#       idx += 1
#       if idx >= M:
#         if i+1 < N:
#           res += sum(A[i+1:])
#         break
#       else:
#         left = cards[idx][1]

# print(res)

### heapq
from collections import Counter
import heapq
N,M = map(int,input().split())
A = Counter(list(map(int,input().split())))

cards = []
for x,y in A.items():
  heapq.heappush(cards, (-x,y))

for _ in range(M):
  b,c = map(int,input().split())
  heapq.heappush(cards, (-c,b))

cnt = N
res = 0
while cnt <= N:
  v,c = heapq.heappop(cards)
  v *= -1

  if cnt-c < 0:
    res += v*cnt
    break
  else:
    res += v*c
    cnt -= c

print(res)

# for i in range(len(C)):
#   if 