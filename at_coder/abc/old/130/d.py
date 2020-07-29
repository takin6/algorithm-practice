N,K = map(int,input().split())
A = list(map(int,input().split()))
cumsum = [0]
for a in A:
  cumsum.append(cumsum[-1]+a)
res = 0
r = 0
# for i in range(N):
#   l = i
#   while r+1 <= N and cumsum[r]-cumsum[l] < K:
#     r += 1

#   if cumsum[r] - cumsum[l] >= K:
#     res += (N+1) - r
sum = 0
right = 0
for left in range(N):
  while right<N and sum<K:
    sum += A[right]
    right += 1
  if sum < K: break
  res += N-right+1
  if right==left:
    right += 1
  else:
    sum -= A[left]

print(res)




# l,r = 0,1
# while l <= N and r <= N:
#   print(l,r)
#   if cumsum[r] - cumsum[l] < K:
#     r += 1
#   elif cumsum[r] - cumsum[l] >= K:
#     print("cnt", l,r)
#     res += 1
#     if r == N:
#       l += 1
#     else:
#       r += 1
#   elif l == r:
#     l += 1
#     r += 1




