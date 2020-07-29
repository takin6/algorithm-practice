# inf rate group
# 0: 8 1
# 1: 6 2
# 2: 9 3
# 3: 1 1
# 4: 2 2
# 5: 1 3

# group: [rates]
# 1: [(8,0), (1,3)]
# 2: [(6,1), (2,4)]
# 3: [(9,2), (1,5)]

# inf, group
# 4 3
# group: [(rates,infs)]
# 1: [(8,1),(1,4)]
# 2: [(6,2),(2,5)]
# 3: [(9,3),(1,6),(1,]
# => min(8,6,9) 6 

# 2 1
# group: [rates]
# 1: [8,6,1]
# 2: [2]
# 3: [9,1,1]
# => min(8,2,9) 6 

# 1 2
# group: [rates]
# 1: [6,1]
# 2: [2]
# 3: [9,1,1,8]
# => min(8,2,9) 6 

# 1. move
# => 各groupでの最大値の変動
#    => moveするinfがgroup内での最大値かどうか
# 3. calc


import heapq
MAX_INT = 200001
N,Q = map(int,input().split())
rates = []
groups = []
for _ in range(N):
  r,g = map(int,input().split())
  rates.append(r)
  groups.append(g)

pqs = [ [] for _ in range(MAX_INT) ]
for i in range(N):
  r,g = rates[i],groups[i]
  heapq.heappush(pqs[g], (-r,i))

max_rates = []
for i in range(1, MAX_INT):
  if len(pqs[i]) > 0:
    r,i = pqs[i][0]
    heapq.heappush(max_rates, (-r,i))
ans = max_rates[0][0]

for _ in range(Q):
  c,new = map(int,input().split())
  c -= 1

  old = groups[c]
  groups[c] = new
  while pqs[old]:
    _,i = pqs[old][0]
    if groups[i] == old: break
    heapq.heappop(pqs[old])

  # adding c to the new group
  heapq.heappush(pqs[new], (-rates[c], c))

  # max_ratesに新しいprevの最大値とnewを足す
  if pqs[old]:
    heapq.heappush(max_rates, (-pqs[old][0][0], pqs[old][0][1]))
  heapq.heappush(max_rates, (-pqs[new][0][0], pqs[new][0][1]))

  # max_ratesの矛盾を取り除く
  # maxのgroupが、
  while True:
    r,i = max_rates[0]
    g = groups[i]
    if not pqs[g] or -pqs[g][0][0] != r:
      heapq.heappop(max_rates)
    else:
      break

  # print(max_rates)
  print(max_rates[0][0])
