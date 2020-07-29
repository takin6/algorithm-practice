# from collections import deque
# def LI():
#   return list(map(int,input().split()))

# N,M,K = map(int,input().split())
# A = deque(LI())
# B = deque(LI())
# res = 0

# while K >= 0:
#   if len(A) == 0:
#     if K >= B[0]:
#       b = B.popleft()
#       K -= b
#     else:
#       break
#   elif len(B) == 0:
#     if K>=A[0]:
#       a = A.popleft()
#       K -= a
#     else:
#       break
#   else:
#     if A[0] > B[0]:
#       b = B.popleft()
#       K -= b
#     elif A[0] < B[0]:
#       a = A.popleft()
#       K -= a
#     else:
#       if A[1] > B[1]:
#         b = B.popleft()
#         K -= b
#       else:
#         a = A.popleft()
#         K -= a

#   if K >= 0:
#     res += 1
#   else:
#     break

#   if len(A) == 0 and len(B) == 0:
#     break


# print(res)


import bisect
def LI():
  return list(map(int,input().split()))

N,M,K = map(int,input().split())
A = LI()
B = LI()

cumA = [0]
for a in A:
  cumA.append(cumA[-1]+a)

cumB = [0]
for b in B:
  cumB.append(cumB[-1]+b)

res = 0
for i in range(N+1):
  cuma = cumA[i]
  if cuma > K: continue
  rem = K-cuma
  deskb = bisect.bisect_right(cumB, rem)-1

  res = max(res, i+deskb)

print(res)