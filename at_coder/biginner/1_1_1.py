
# while True:
#   N,M = list(map(int, input().split()))
#   if N == 0 and M == 0: break
#   points = []
#   for _ in range(N):
#     points.append(int(input()))

#   max_points = 0

#   possible_points = []

#   # 1 dart
#   for p in points:
#     if p == M:
#       max_points = p
#       break
#     elif p < M:
#       max_points = max(max_points, p)
#       possible_points.append(p)

#   if max_points != M:
#     # 2 darts
#     for p1 in range(len(points)):
#       if max_points == M: break
#       for p2 in range(p1, len(points)):
#         if p1 >= p2:
#           if points[p1]+points[p2] == M:
#             max_points = points[p1]+points[p2]
#             break
#           elif points[p1]+points[p2] < M:
#             max_points = max(max_points, points[p1]+points[p2])
#             possible_points.append(points[p1]+points[p2])

#   possible_points = sorted(possible_points)

#   # 3 darts
#   if max_points != M:
#     for i in range(N):
#         candidate = possible_points[i]
#         rem = M - candidate
#         l,r = 0, len(possible_points)-1

#         while l < r:
#           m = (l+r)//2
          
#           if possible_points[m] == rem:
#             l = m
#             break
#           elif possible_points[m] > rem:
#             r = m-1
#           else:
#             l = m+1

#         if candidate + possible_points[l] <= M:
#           max_points = max(max_points, candidate + possible_points[l])
#         elif candidate + possible_points[l] > M:
#           max_points = max(max_points, candidate)

#   # 4 darts
#   if max_points != M:
#     for i in range(N):
#       if max_points == M: break

#       for j in range(i, N):
#         candidate = 0

#         candidate = points[i] + points[j]
#         if candidate > M: continue

#         rem = M - candidate
#         l,r = 0, len(possible_points)-1

#         while l < r:
#           m = (l+r)//2
          
#           if possible_points[m] == rem:
#             l = m
#             break
#           elif possible_points[m] > rem:
#             r = m-1
#           else:
#             l = m+1

#         if candidate + possible_points[l] <= M:
#           max_points = max(max_points, candidate + possible_points[l])
#         elif candidate + possible_points[l] > M:
#           max_points = max(max_points, candidate)

#   print(max_points)



# while True:
#   N,M = list(map(int, input().split()))
#   if N == 0 and M == 0: break
#   points = []
#   for _ in range(N):
#     points.append(int(input()))
#   points.append(0)

#   possible_points = []
#   for i in range(N):
#     for j in range(i, N+1):
#       possible_points.append(points[i]+points[j])
#   possible_points.append(0)
#   possible_points = sorted(possible_points)

#   max_points = 0

#   for i in range(len(possible_points)):
#     candidate = possible_points[i]
#     if candidate > M: continue

#     rem = M - candidate
#     l,r = i, len(possible_points)-1
#     while l < r:
#       m = (l+r)//2
      
#       if possible_points[m] == rem:
#         l = m
#         break
#       elif possible_points[m] > rem:
#         r = m-1
#       else:
#         l = m+1

#     if candidate + possible_points[l] <= M:
#       max_points = max(max_points, candidate + possible_points[l])
#     else:
#       max_points = max(max_points, candidate)

#     if max_points == M: break

#   print(max_points)

# import bisect

# N,M = list(map(int, input().split()))
# if N == 0 and M == 0: break
# points = [0]*(N+1)
# for i in range(N):
#   points[i] = int(input())
# points[N] = 0

# possible_points = []
# for i in range(N):
#   for j in range(i, N+1):
#     possible_points.append(points[i]+points[j])
# possible_points.append(0)
# possible_points.sort()

# max_points = 0

# for i in range(len(possible_points)):
#   candidate = possible_points[i]
#   if candidate < M:
#      max_points = max(max_points, candidate)

#   if  M-candidate > 0:
#     l = bisect.bisect_left(possible_points, M-candidate)
#     if l>0 and candidate + possible_points[l-1] <= M:
#       max_points = max(max_points, candidate + possible_points[l-1])

#     if max_points == M: break

# print(max_points)


# import bisect

# while True:
#   N,M = list(map(int, input().split()))
#   if N == 0 and M == 0: break
#   points = [0] + [ int(input()) for _ in range(N) ]

#   possible_points = sorted([ points[i]+points[j] for i in range(N+1) for j in range(i, N+1) if points[i]+points[j]<=M ])

#   max_points = 0

#   for x in possible_points:
#     y = possible_points[bisect.bisect_right(possible_points, M - x)-1]
#     max_points = max(max_points, x+y)

#   print(max_points)

import bisect
while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0: break
  P = [0] + [int(input()) for _ in range(N)]
  P.sort()
  
  L = [P[i]+P[j] for i in range(N+1) for j in range(i,N+1) if P[i]+P[j] <= M]
  L.sort()

  ans = 0
  for x in L:
      y = L[bisect.bisect_right(L, M-x) - 1]
      ans = max(ans, x+y)
  
  print(ans)


