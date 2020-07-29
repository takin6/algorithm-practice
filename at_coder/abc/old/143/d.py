# 1,2,3,4
# 1,2 => c=3,4
# 1,3 => c=4
# 2,3 => c=4
import bisect

N = int(input())
L = list(map(int,input().split()))
L.sort()

ans = 0
for i in range(N):
  for j in range(i+1, N-1):
    k = L[i]+L[j]
    l,r = 0,N
    while (r-l) > 1:
      m = (l+r)//2
      if L[m] >= k:
        r = m
      else:
        l = m

    ans += r-j-1

print(ans)


# 4
# 1 2 3 4