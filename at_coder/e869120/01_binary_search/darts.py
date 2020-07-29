import bisect

while True:
  N,M = map(int,input().split())
  if N == 0 and M == 0: break
  targets = [0]+[ int(input()) for _ in range(N) ]
  targets.sort()

  cans = [targets[i]+targets[j] for i in range(N+1) for j in range(i,N+1) if targets[i]+targets[j] <= M]
  cans.sort()

  res = 0

  for l in cans:
    y = cans[bisect.bisect_right(cans, M-l)-1]
    res = max(res, l+y)

  print(res)


# import bisect
# while True:
#   N, M = map(int, input().split())
#   if N == 0 and M == 0: break
#   P = [0] + [int(input()) for _ in range(N)]
#   P.sort()
  
#   L = [P[i]+P[j] for i in range(N+1) for j in range(i,N+1) if P[i]+P[j] <= M]
#   L.sort()

#   ans = 0
#   for x in L:
#       y = L[bisect.bisect_right(L, M-x) - 1]
#       ans = max(ans, x+y)
  
#   print(ans)

  # targets.append(0)
  # for i in targets:
  #   for j in targets:
  #     if i+j > M: continue
  #     r = M - i - j
  #     idx = bisect.bisect_right(cans, r)-1
  #     if idx < 0: continue
  #     res = max(res, i+j+cans[idx])

  # print(res) 