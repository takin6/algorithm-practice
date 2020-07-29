
bingo = [ list(map(int, input().split())) for _ in range(3) ]
t_or_f = [ [False]*3 for _ in range(3) ]

nums = [ r[i]for i in range(3) for r in bingo ]

n = int(input())
appear = [ int(input()) for _ in range(n) ]

for x in range(3):
  for y in range(3):
    if bingo[x][y] in appear:
      t_or_f[x][y] = True

is_bingo = False
if t_or_f[0][0] and t_or_f[1][1] and t_or_f[2][2]:
  is_bingo = True
elif t_or_f[0][2] and t_or_f[1][1] and t_or_f[2][0]:
  is_bingo = True
else:
  for i in range(3):
    if t_or_f[i][0] and t_or_f[i][1] and t_or_f[i][2]: is_bingo = True
    if t_or_f[0][i] and t_or_f[1][i] and t_or_f[2][i]: is_bingo = True

if is_bingo:
  print('Yes')
else:
  print('No')

