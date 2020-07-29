while True:

  m = int(input())
  n = int(input())
  if m==n==0: exit()
  graph = []
  for _ in range(n):
    graph.append(list(map(int,input().split())))

  res = 0
  def dfs(r,c,ice):
    global res
    ice += 1
    graph[r][c] = 0

    for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
      nr,nc = r+x,c+y
      if nr<0 or nc<0 or nr>=n or nc>=m: continue
      if graph[nr][nc] == 1:
        dfs(nr,nc,ice)
    else:
      graph[r][c] = 1
      res = max(res, ice)

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        dfs(i,j,0)

  print(res)