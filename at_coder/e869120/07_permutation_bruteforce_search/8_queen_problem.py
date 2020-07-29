import pprint

inp = int(input())
N = 8
board = [ [0]*8 for _ in range(8) ]
defined = []
dic = {}
for _ in range(inp):
  x,y = map(int,input().split())
  board[x][y] = 1
  defined.append(x)
  dic[x] = y

def check(board, row, col):
  for i in range(8):
    if i==col: continue
    if board[row][i] == 1:
      return False

  for i in range(8):
    if i==row: continue
    if board[i][col] == 1:
      return False

  # left upper
  for i,j in zip(range(row, -1, -1), range(col, -1, -1)):
    if i==row and j==col: continue
    if board[i][j] == 1:
      return False

  # left lower
  for i,j in zip(range(row, N), range(col, -1, -1)):
    if i==row and j==col: continue
    if board[i][j] == 1:
      return False

  # right upper
  for i,j in zip(range(row, -1, -1), range(col, N)):
    if i==row and j==col: continue
    if board[i][j] == 1:
      return False

  # right lower
  for i,j in zip(range(row, N), range(col, N)):
    if i==row and j==col: continue
    if board[i][j] == 1:
      return False

  return True

def solve(board, row):
  if row >= 8:
    return True

  if row in defined:
    col = dic[row]
    if check(board, row, col):
      if solve(board, row+1):
        return True
  else:
    for col in range(8):
      if check(board, row, col):
        board[row][col] = 1
        if solve(board, row+1):
          return True
        board[row][col] = 0

  return False

solve(board, 0)

for row in board:
  print("".join(["Q" if r==1 else "." for r in row ]))

# print(board)
# import pprint
# pprint.pprint(board)
# import pdb; pdb.set_trace()