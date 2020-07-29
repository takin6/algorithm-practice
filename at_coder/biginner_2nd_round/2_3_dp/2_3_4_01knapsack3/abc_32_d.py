N,W = map(int,input().split())
items = []
maxv,maxw = 0,0
for _ in range(N):
  v,w = map(int,input().split())
  items.append([v,w])
  maxv = max(maxv,v)
  maxw = max(maxw,w)

# Nが30以下　=> 半分全列挙
# 価値が1000以下 => 価値に対して重荷が最小化
# 重みが1000以下 => 重荷に対して価値が最ぢ赤
if N <= 30:
  import bisect
  groupA = items[:N//2]
  groupB = items[N//2:]

  # bit全探索でgroupAの組み合わせを全列挙
  combA = []
  for i in range(1 << len(groupA) ):
    vsum = 0; wsum = 0
    for d in range(len(groupA)):
      if (i>>d)&1:
        vsum += groupA[d][0]
        wsum += groupA[d][1]
    if wsum <= W:
      combA.append((vsum,wsum))

  # combAからありえないものを排除
  # (5,3),(5,5)となったとき、(5,5)を排除
  usefulA = [(0,0)]
  # combA.sort(key=lambda x: (-x[0],x[1]))
  # valueの降順
  combA.sort(key=lambda x: -x[0])
  # weightの昇順
  combA.sort(key=lambda x: x[1])
  for v,w in combA:
    # if w >= usefulA[-1][1]:
    if v >= usefulA[-1][0]:
      usefulA.append((v,w))

  combB = []
  for i in range(1 << len(groupB) ):
    vsum = 0; wsum = 0
    for d in range(len(groupB)):
      if (i>>d)&1:
        vsum += groupB[d][0]
        wsum += groupB[d][1]
    if wsum <= W:
      combB.append((vsum,wsum))

  usefulB = [(0,0)]
  # combB.sort(key=lambda x: (-x[0],x[1]))
  combB.sort(key=lambda x: -x[0])
  combB.sort(key=lambda x: x[1])
  for v,w in combB:
    # if w >= usefulB[-1][1]:
    if v >= usefulB[-1][0]:
      usefulB.append((v,w))

  res = 0
  # usefulAとusefulBのマッチングを探す
  # usefulBからW-wAを二分探索
  weightB = [ x[1] for x in usefulB]
  for vA,wA in usefulA:
    pairB = bisect.bisect_right(weightB, W-wA) -1
    if 0 <= pairB < len(weightB):
      vB,wB = usefulB[pairB]
      res = max(res, vA+vB)

  print(res)

elif maxv <= 1000:
  # dp[v] = valueがvとなるときの、重みの最小化
  dp = [float('inf')] * (N*maxv+1)
  dp[0] = 0
  for i in range(N):
    v,w = items[i]
    for j in range(N*maxv, v-1, -1):
      dp[j] = min(dp[j], dp[j-v]+w)

  for k in range(N*maxv, -1, -1):
    if dp[k] <= W:
      print(k)
      exit()

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