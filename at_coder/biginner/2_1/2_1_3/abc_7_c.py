R,C = list(map(int, input().split()))
sy,sx = list(map(int, input().split()))
gy,gx = list(map(int, input().split()))
sy,sx,gy,gx = sy-1,sx-1,gy-1,gx-1
matrix = []
for _ in range(R):
  matrix.append(list(input()))

q = [(sy,sx,0)]
visited = []
res = 10*1000
while q:
  r,c,step = q.pop(0)
  if r == gy and c == gx:
    res = min(res, step)
  visited.append((r,c))

  for y,x in [(-1,0),(0,-1),(1,0),(0,1)]:
    nr,nc = r+y,c+x
    if nr < 1 or nc < 1 or nr >= R-1 or nc >= C-1: continue
    if matrix[nr][nc] == "#": continue
    if (nr,nc) not in visited and (nr,nc,step+1) not in q:
      q.append((nr,nc,step+1))

print(res)