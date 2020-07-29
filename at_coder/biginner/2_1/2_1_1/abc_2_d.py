from collections import defaultdict
N, M = list(map(int, input().split()))
adj_list = defaultdict(list)

for i in range(M):
  x, y = list(map(int, input().split()))
  if x in adj_list:
    adj_list[x].append(y)
  else:
    adj_list[x] = [y]

  if y in adj_list:
    adj_list[y].append(x)
  else:
    adj_list[y] = [x]

def is_group(temp):
  flag = True
  for m in temp:
    for n in temp:
      if m != n:
        if n not in adj_list[m]:
          flag = False
          break    

  return flag

members = -float('inf')
combs = []
for i in range(1 << (N+1)):
  # if i == 1 or i % 2 == 0:
  #   members = max(members, 1)
  #   continue

  temp = []
  for j in range(N+1):
    if not (i>>j)&1: temp.append(j)

  if is_group(temp):
    members = max(members, len(temp))

print(members)
