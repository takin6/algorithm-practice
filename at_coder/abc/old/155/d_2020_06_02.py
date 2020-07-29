from bisect import bisect_left, bisect_right
N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
neg_end = bisect_left(A, 0)
pos_start = bisect_right(A, 0)

pos_cnt = N - pos_start
neg_cnt = neg_end
zero_cnt = N - (pos_cnt + neg_cnt)

neg_pairs_cnt = pos_cnt * neg_cnt
zero_pairs_cnt = zero_cnt * (pos_cnt + neg_cnt) + (zero_cnt * (zero_cnt-1) // 2)

if K <= neg_pairs_cnt:
  # X以下のpairはK個以上あるか？
  ok, ng = 0, -10**18
  while abs(ok - ng) > 1:
    X = (ok+ng) // 2
    or_higher_cnt, r = 0, pos_start
    # それぞれのnegごとに尺取り法
    for l in range(neg_end):
      while r < N and A[l] * A[r] > X:
        r += 1
      # positive_integers - (max_point - positive_start_index)
      or_higher_cnt += pos_cnt - (r - pos_start)

    if or_higher_cnt >= K:
      ok = X
    else:
      ng = X
  print(ok)

elif K <= neg_pairs_cnt + zero_pairs_cnt:
  print(0)

else:
  K -= (neg_pairs_cnt + zero_pairs_cnt)
  ok, ng = 10**18, 0
  while abs(ok - ng)> 1:
    X = (ok+ng) // 2
    or_higher_cnt = 0

    r = N - 1
    for l in range(pos_start, N):
      while r < N and A[l] * A[r] > X and l < r:
        r -= 1
      or_higher_cnt += max(0, r-l)

    l = 0
    for r in range(neg_end-1, -1, -1):
      while l < N and A[l] * A[r] > X and l < r:
        l += 1
      or_higher_cnt += max(0, r-l)

    if or_higher_cnt >= K:
      ok = X
    else:
      ng = X

  print(ok)


  # https://at274.hatenablog.com/entry/2020/02/27/060000