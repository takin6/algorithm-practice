h,w,k = map(int,input().split())
maze = []
for _ in range(h):
  maze.append(list(input()))

def check(rows, cols):
  black = 0
  for i in range(h):
    if i in rows: continue
    for j in range(w):
      if j in cols: continue
      if maze[i][j] == "#":
        black += 1

  return black == k

res = 0

for i in range(1<<h):
  paint_rows = []
  for j in range(h):
    if (i>>j)&1:
      paint_rows.append(j)

  for n in range(1<<w):

    paint_cols = []
    for m in range(w):
      if (n>>m)&1:
        paint_cols.append(m)

    if check(paint_rows, paint_cols):
      res += 1

print(res)
