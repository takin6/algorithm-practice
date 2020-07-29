M,N = map(int,input().split())
K = int(input())
maze = []
for _ in range(M): 
  maze.append(list(input()))

J = [ [0]*(N+1) for _ in range(M+1) ] 
O = [ [0]*(N+1) for _ in range(M+1) ]
I = [ [0]*(N+1) for _ in range(M+1) ]

for i in range(M):
  for j in range(N):
    if maze[i][j] == "J":
      J[i+1][j+1] = 1
    elif maze[i][j] == "O":
      O[i+1][j+1] = 1
    else:
      I[i+1][j+1] = 1

for i in range(1,M+1):
  for j in range(1,N+1):
    J[i][j] += J[i-1][j]-J[i-1][j-1]+J[i][j-1]
    O[i][j] += O[i-1][j]-O[i-1][j-1]+O[i][j-1]
    I[i][j] += I[i-1][j]-I[i-1][j-1]+I[i][j-1]

for _ in range(K):
  x1,y1,x2,y2 = map(int,input().split())
  j = J[x2][y2]-J[x1-1][y2]-J[x2][y1-1]+J[x1-1][y1-1]
  o = O[x2][y2]-O[x1-1][y2]-O[x2][y1-1]+O[x1-1][y1-1]
  i = I[x2][y2]-I[x1-1][y2]-I[x2][y1-1]+I[x1-1][y1-1]
  print(j,o,i)
