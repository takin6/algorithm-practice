a = [ ["*"]*3 for _ in range(3)]
b = [ [0]*3 for _ in range(3)]
c = [ [0]*3 for _ in range(3)]

b[0][0],b[0][1],b[0][2] = list(map(int, input().split()))
b[1][0],b[1][1],b[1][2] = list(map(int, input().split()))
c[0][0],c[0][1] = list(map(int,input().split()))
c[1][0],c[1][1] = list(map(int, input().split()))
c[2][0],c[2][1] = list(map(int, input().split()))
score_sum = sum([sum(i) for i in b])
score_sum += sum([sum(i) for i in c])
memo = {}

def calc_score():
  x_score = 0
  for i in range(2):
    for j in range(3):
      if a[i][j] == a[i+1][j]:
        x_score += b[i][j]

  for i in range(3):
    for j in range(2):
      if a[i][j] == a[i][j+1]:
        x_score += c[i][j]

  return x_score

def dfs(turn):
  if turn == 9:

    return calc_score()

  if turn % 2 == 0:
    max_val = 0
    for i in range(3):
      for j in range(3):
        if a[i][j] != "*": continue
        a[i][j] = "o"
        max_val = max(max_val, dfs(turn+1))
        a[i][j] = "*"
    return max_val
  else:
    min_val = float('inf')
    for i in range(3):
      for j in range(3):
        if a[i][j] != "*": continue
        a[i][j] = "x"
        min_val = min(min_val, dfs(turn+1))
        a[i][j] = "*"
    return min_val

x = dfs(0)
print(x)
print(score_sum-x)
