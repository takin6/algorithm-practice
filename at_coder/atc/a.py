import sys
sys.setrecursionlimit(1000000000) 

row, col = list(map(int, input().split()))

matrix, sp = [], None
for i in range(row):
  r = [ i for i in input() ]
  # starting point
  if sp is None and "s" in r: sp = (i, r.index("s"))
  matrix.append(r)

visited = set()

# row pointer, column pointer
def dfs(rp, cp):
  # rp = 3 , row = 3
  # 3 > 3 - 1 => 3 > 2
  # 3 >= 3 => 3 > 4
  # not 0 <= r < h

  if rp >= row or rp < 0 or cp >= col or cp < 0:
    return False

  if matrix[rp][cp] == "#":
    return False

  if matrix[rp][cp] == "g":
    return True

  if (rp, cp) not in visited:
    visited.add((rp, cp))

    top = dfs(rp-1, cp)
    right = dfs(rp, cp+1)
    left = dfs(rp, cp-1)
    bottom = dfs(rp+1, cp)

    return any([top, right, left, bottom])


rp, cp = sp
result = dfs(rp, cp)
print("Yes" if result else "No")