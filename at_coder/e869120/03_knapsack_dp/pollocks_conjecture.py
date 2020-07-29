# query = []
# while True:
#   q = int(input())
#   if q==0: break
#   query.append(q)

# MAX_INT = max(query)+1

# square = []
# odd_square = []
# for i in range(1,181):
#   blocks = i*(i+1)*(i+2)//6
#   if blocks > MAX_INT: break
#   if blocks%2==1:
#     odd_square.append(blocks)
#   square.append(blocks)

# dp1 = [MAX_INT] * MAX_INT
# dp1[0] = 0
# for i in range(len(square)):
#   s = square[i]
#   for j in range(MAX_INT):
#     if j-s >= 0:
#       dp1[j] = min(dp1[j], dp1[j-s]+1)

# dp2 = [MAX_INT] * MAX_INT
# dp2[0] = 0
# for i in range(len(odd_square)):
#   s = odd_square[i]
#   for j in range(MAX_INT):
#     if j-s >= 0:
#       dp2[j] = min(dp2[j], dp2[j-s]+1)

# for q in query:
#   print(dp1[q], dp2[q])
INF = 10**20
MAX_INT = 10**6
a = [INF] * MAX_INT
b = [INF] * MAX_INT
a[0],b[0] = 0,0
for i in range(1, 200):
  t = i*(i+1)*(i+2)//6
  mm = min(t*5, MAX_INT)
  for j in range(t, mm):
    if a[j] > a[j-t]+1:
      a[j] = a[j-t]+1

  if t%2==0: continue

  for j in range(t, MAX_INT):
    if b[j] > b[j-t]+1:
      b[j] = b[j-t]+1

while True:
  N = int(input())
  if N==0: exit()
  print(a[N], b[N])