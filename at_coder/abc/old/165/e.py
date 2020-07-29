# N,M = map(int,input().split())


# skip = (N//2) // 2 + 1 if N%2==0 else None
# count = 0
# left,right = 0,N+1
# while count < M:
#   left += 1
#   if left == skip:
#     continue
#   right -= 1
#   print(left, right)
  # count += 1

N,M = map(int,input().split())

if N%2==1:
  for i in range(M):
    print(str(i+1) + " " + str(N-(i+1)))
else:
  flag = False
  l = 1
  r = N-1
  cnt = 0
  while cnt < M and l < r:
    if not flag and r-l <= N//2:
      r -= 1
      flag = True
    print(str(l) + " " + str(r))
    l += 1
    r -= 1
    cnt += 1



# loop = [0,N-1]

# if N%2==0:
#   loop.append(N//2)

# j = N-1 if N%2==1 else N
# res = []
# cnt = 0

# for i in range(1, N):
#   if j-i not in loop:
#     res.append((i, j))
#     cnt += 1

#   if cnt == M:
#     break
#   else:
#     j -= 1

# for pair in res:
#   print(" ".join(map(str,pair)))