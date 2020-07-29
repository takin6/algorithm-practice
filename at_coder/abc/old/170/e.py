# N : infants
# school: 2*10**5(1~2**15

# Q: 転園
# j回目：infant Cj => school Dj
# 「平等さ」 最もレートの滝あ用事のレートを求め、その最小値として得られる値


from heapq import heappush, heappop
N,Q = map(int,input().split())

belongings = [0] * (N+1)
rates = [0] * (N+1)
groups = [ [] for _ in range(200001) ]
min_rates = []

for i in range(1, N+1):
  a,b = map(int,input().split())
  rates[i] = a
  belongings[i] = b
  heappush(groups[b], (-a, i))

for l in groups:
  if len(l) > 0:
    a,i = l[0]
    heappush(min_rates, (-a, belongings[i]))

for _ in range(Q):
  c,d = map(int,input().split())

  prev = belongings[c]
  belongings[c] = d
  
  # 上の処理で、cのbelongingsを変えたので、
  # 元々のgroupのmaxがprevでなくなるまでpopする
  while groups[prev]:
    _,i = groups[prev][0]
    if belongings[i] == prev: break
    heappop(groups[prev])

  # 新しいグループに追加
  heappush(groups[belongings[c]], (-rates[c], c))

  # minratesに新しいprevの最大値とnewを足す
  if len(groups[prev]) > 0:
    heappush(min_rates, (-groups[prev][0][0], prev))
  heappush(min_rates, (-groups[belongings[c]][0][0], belongings[c]))

  while groups:
    mx,id = min_rates[0]
    # 矛盾するものをpop
    if len(groups[id]) > 0 and -groups[id][0][0] == mx:
      break
    heappop(min_rates)

  print(min_rates[0][0])


# curmin = 
# for _ in range(Q):
#   c,d = map(int,input().split())
#   schools[d].
