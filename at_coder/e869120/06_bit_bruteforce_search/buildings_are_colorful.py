# N,K = map(int,input().split())
# A = list(map(int,input().split()))

# res = float('inf')

# for i in range(1<<N):
#   a = A[::]
#   paint = 0
#   cur = None
#   add = 0
#   for j in range(N):
#     if (i>>j)&1:
#       paint += 1
#       h = a[j]
#       if cur is None:
#         if j>0 and a[j-1]>=h:
#           break
#         else:
#           cur = h
#       else:
#         min_h = max(cur, a[j-1])
#         if h <= min_h:
#           add += (min_h+1) - h
#           cur = min_h + 1
#           a[j] = cur

#   if paint == K:
#     res = min(res, add)

# print(res)

# N,K = map(int,input().split())
# A = list(map(int,input().split()))

# res = float('inf')

# for i in range(1<<N):
#   a = A[::]
#   paint = 0
#   cur = 0
#   add = 0
#   for j in range(N):
#     if (i>>j)&1:
#       paint += 1
#       if a[j] <= cur:
#         add += (cur+1) - a[j]
#         a[j] = cur+1
#       cur = max(cur, a[j])
#     else:
#       cur = max(cur, a[j])

#   if paint == K:
#     res = min(res, add)

# print(res)

# 7 7 7 7 7
# 7 8 9 10 11

N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = float('inf')

for i in range(1<<N):
  a = A[::]
  cur,add = 0,0
  see = 0
  for j in range(N):
    if (i>>j)&1:
      see += 1
      if cur >= a[j]:
        add += (cur-a[j])+1
        a[j] = cur+1
      cur = max(cur,a[j])
    else:
      cur = max(cur,a[j])

  if see == K:
    ans = min(ans, add)

print(ans)

