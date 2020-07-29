import bisect
N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

neg_end = bisect.bisect_left(A,0)
pos_start = bisect.bisect_right(A,0)

pos_cnt = N - pos_start
neg_cnt = neg_end
zero_cnt = N - pos_cnt - neg_cnt

neg_pairs_cnt = pos_cnt * neg_cnt
zero_pairs_cnt = zero_cnt*(zero_cnt-1)//2 + zero_cnt*(pos_cnt+neg_cnt)

#X以下になるペアがK個以上あるか？
if K <= neg_pairs_cnt:
  ok,ng = 0,-10**18
  while abs(ok-ng) > 1:
    m = (l+r)//2

    cnt = 0
    r = pos_start
    for l in range(neg_end):
      while r < N and A[l]*A[r] > m:
        r += 1
      cnt += pos_cnt - (r - pos_start)

    if cnt >= K:
      ok = m
    else:
      ng = m

  print(ok)

elif K <= neg_pairs_cnt+zero_pairs_cnt:
  print(0)
else:
  K -= (neg_pairs_cnt + zero_pairs_cnt)
  ok,ng = 10**18, 0
  while abs(ok-ng) > 1:
    m = (ok+ng)//2
    cnt = 0

    r = N-1
    for l in range(pos_start, N):
      while r < N and A[l]*A[r]>m and l<r:
        r -= 1
      cnt += max(0, r-l)

# else:
#   ## plus