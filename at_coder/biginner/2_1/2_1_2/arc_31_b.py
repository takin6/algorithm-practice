matrix = []
lands = 0
for _ in range(10):
  r = list(input())
  lands += r.count("o")
  matrix.append(r)


def dfs(x,y,seen,exclude=[]):
  if x < 0 or y < 0 or x >= 10 or y >= 10: return 0
  if (x,y) not in exclude and matrix[x][y] == "x": return 0
  if (x,y) in seen: return 0
  seen.append((x,y))

  return 1 + dfs(x+1, y,seen) + dfs(x-1, y,seen) + dfs(x, y+1, seen) + dfs(x, y-1, seen)

flag = False
for i in range(10):
  for j in range(10):
    if lands == dfs(i,j,[],[(i,j)])-1:
      flag = True
      break

print('YES') if flag else print('NO')

# def dfs(x,y,de,memo):
#   if x < 0 or y < 0 or x >= 10 or y >= 10: return de
#   if de > 1: return de
#   if (x,y,de) in memo: return de

#   memo.append((x,y,de))
#   if matrix[x][y] == "x" and de == 0:
#     for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#       dfs(x+dx,y+dy,de+1,memo)
#   else:
#     reached.append((x,y))
#     max_de_count = 0
#     for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
#       max_de_count += dfs(x+dx,y+dy,de,memo)
#     return max_de_count

# for i in range(10):
#   for j in range(10):
#     if matrix[i][j] == "o" and (i,j) not in reached:
#       max_de_count = dfs(i,j,0,[])
#       if lands == 1 and 
