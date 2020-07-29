import sys
sys.setrecursionlimit(10**7)

A,B,C = map(int,input().split())
K = int(input())

# A=red,B=green,C=blue
# B > A, C > B
def dfs(i,a,b,c):
  if i==K:
    if b>a and c>b:
      return True
    else:
      return False

  for j in range(3):
    if j==0:
      if dfs(i+1,2*a,b,c):
        return True
    elif j==1:
      if dfs(i+1,a,2*b,c):
        return True
    else:
      if dfs(i+1,a,b,2*c):
        return True

  return False

if dfs(0,A,B,C):
  print("Yes")
else:
  print("No")

