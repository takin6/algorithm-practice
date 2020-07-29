# 参考URL
# https://atcoder.jp/contests/abc032/submissions/13095526
# https://misora192.hatenablog.com/entry/2019/01/23/082925

# TODO: 分枝限定法
# https://www.youtube.com/watch?v=yV1d-b_NeK8&feature=youtu.be
# https://qiita.com/Kou__/items/84b6da4845f469e52a69

N, W = map(int, input().split())

items = []
maxv, maxw = 0, 0
for _ in range(N):
  v,w = map(int, input().split())
  maxv, maxw = max(maxv, v), max(maxw, w)
  items.append((v,w))

# A) Nが30以下のケース
#    => w,vに制限がないので、半分全列挙
# B) 全ての荷物の価値が1000以下のケース
#    => dp[i][v] = 価値に対して重荷が最小化するDP
# C) 全ての荷物の重荷が1000以下の
#    => dp[i][w] = 重荷に対して価値が最大化するDP

if N <= 30:
  import bisect

  groupA = items[:N//2]
  groupB = items[N//2:]

  combA = []
  for i in range(2**len(groupA)):
    vsum = 0; wsum = 0
    for d in range(len(groupA)):
      if (i>>d)&1:
        vsum += groupA[d][0]
        wsum += groupA[d][1]
    if wsum <= W:
      combA.append((vsum, wsum))

  ### 重くて価値のないものを排除する##
  ### ex) v,wが(5,3)があるとき、(3,4)を排除 ###
  usefulA = [(0,0)]
  # valueの降順
  combA.sort(key=lambda x: -x[0])
  # weightの昇順
  combA.sort(key=lambda x: x[1])
  for v,w in combA:
    if v >= usefulA[-1][0]:
      usefulA.append((v,w))

  combB = []
  for i in range(2**len(groupB)):
    vsum = 0; wsum = 0
    for d in range(len(groupB)):
      if (i>>d)&1:
        vsum += groupB[d][0]
        wsum += groupB[d][1]
    if wsum <= W:
      combB.append((vsum, wsum))

  usefulB = [(0,0)]
  combB.sort(key=lambda x: -x[0])
  combB.sort(key=lambda x: x[1])
  for v,w in combB:
    if v >= usefulB[-1][0]:
      usefulB.append((v,w))

  weightB = [ x[1] for x in usefulB ]
  res = 0
  for vA,wA in usefulA:
    pairB = bisect.bisect_right(weightB, W-wA) - 1
    if 0 <= pairB < len(weightB):
      vB, wB = usefulB[pairB]
      res = max(res, vA+vB)

  print(res)

elif maxv <= 1000:
  # dp[i][v] = i番目のitemまでを使って価値の和jを達成する重みの和の最小値
  # => dp[i] = 価値iの時に出すことのできる最小値
  dp = [float('inf')] * (N*maxv+1)
  dp[0] = 0
  for i in range(N):
    val,wei = items[i][0], items[i][1]
    # N*maxv ~ valまで
    for j in range(N*maxv, val-1, -1):
      dp[j] = min(dp[j], dp[j-val]+wei)

  for k in range(N*maxv, -1, -1):
    if dp[k] <= W:
      print(k)
      break
elif maxw <= 1000:

  dp = [ [0]*(W+1) for _ in range(N+1) ]

  for i in range(1, N+1):
    val, wei = items[i-1]
    for w in range(1, W+1):
      if w >= wei:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w-wei]+val)
      else:
        dp[i][w] = dp[i-1][w]

  print(dp[-1][-1])