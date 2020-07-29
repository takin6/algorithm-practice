# a,b = list(map(int, input().split()))
# cnt = 0
# while b >= a:
#   a = a * 2
#   cnt += 1

# print(cnt)

# ========== arc tumikasane ===========--
# N = int(input())
# piles = []

# for _ in range(N):
#   w = int(input())

#   if len(piles) == 0:
#     piles.append(w)

#   else:
#     flg = False
#     for i in range(len(piles)):
#       if piles[i] >= w:
#         piles[i] = w
#         flg = True
#         break

#     if not flg:
#       piles.append(w)

# print(len(piles))

T = int(input())
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

res = True
for i in range(M):
  b = B[i]

  flg = False
  for i in range(len(A)):
    if 0 <=b-A[i] <= T:
      flg = True
      A.pop(i)
      break

  if not flg:
    res = False
    break

if res:
  print('yes')
else:
  print('no')
