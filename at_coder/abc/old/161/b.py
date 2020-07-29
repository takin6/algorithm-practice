# 1/4M

# N M
# 4 1
# 5 4 2 1
# 12
# 12 // 4*1 = 3
# sort() and find the biggest


# 3 2
# 380 19 1
# total = 400
# at_least = 400 // 8 = 50

N, M = list(map(int, input().split()))
scores = list(map(int, input().split()))
at_least = sum(scores) / (4*M)

if len([ s for s in scores if s >= at_least]) >= M:
  print('Yes')
else:
  print('No')
