# N,A,B,C = map(int,input().split())
# S = [ input() for _ in range(N) ]

# res = []
# for i,turn in enumerate(S):
#   if turn == "AB":
#     if A == B == 0:
#       print("No")
#       exit()
#     elif A == B == 1 and C == 0:
#       if "A" in S[i+1]:
#         A,B = A+1,B-1
#         res.append("B")
#       if "B" in S[i+1]:
#         A,B = A-1,B+1
#         res.append("A")
#     elif A>B:
#       A,B = A-1,B+1
#       res.append("A")
#     else:
#       A,B = A+1,B-1
#       res.append("B")

#   if turn == "AC":
#     if A == C == 0:
#       print("No")
#       exit()
#     elif A == C == 1 and B == 0:
#       if "A" in S[i+1]:
#         A,C = A+1,C-1
#         res.append("C")
#       if "C" in S[i+1]:
#         A,B = A-1,C+1
#         res.append("A")
#     elif A>C:
#       A,C = A-1,C+1
#       res.append("A")
#     else:
#       A,C = A+1,C-1
#       res.append("C")

#   if turn == "BC":
#     if B == C == 0:
#       print("No")
#       exit()
#     elif B == C == 1 and A == 0:
#       if "B" in S[i+1]:
#         B,C = B+1,C-1
#         res.append("C")
#       if "C" in S[i+1]:
#         B,C = B-1,C+1
#         res.append("B")
#     elif B>C:
#       B,C = B-1,C+1
#       res.append("B")
#     else:
#       B,C = B+1,C-1
#       res.append("C")

# print("Yes")
# for r in res:
#   print(r)


# import sys
# sys.setrecursionlimit(100000)

# N,A,B,C = map(int,input().split())
# S = [ input() for _ in range(N) ]
# res = [None] * N

# def dfs(i, a, b, c):
#   if a < 0 or b < 0 or c < 0:
#     return
#   elif i == N:
#     print("Yes")
#     for r in res: print(r)
#     exit()
#   else:
#     if S[i] == "AB":
#       res[i] = "A"
#       dfs(i+1, a-1, b+1, c)
#       res[i] = "B"
#       dfs(i+1, a+1, b-1, c)
#     elif S[i] == "AC":
#       res[i] = "A"
#       dfs(i+1, a-1, b, c+1)
#       res[i] = "C"
#       dfs(i+1, a+1, b, c-1)
#     else:
#       res[i] = "B"
#       dfs(i+1, a, b-1, c+1)
#       res[i] = "C"
#       dfs(i+1, a, b+1, c-1)

# dfs(0, A,B,C)
# print("No")



import sys
sys.setrecursionlimit(100000)

N,A,B,C = map(int,input().split())
S = [ input() for _ in range(N) ]
res = [None] * N

def dfs(i, a, b, c):
  if a < 0 or b < 0 or c < 0:
    return
  elif i == N:
    print("Yes")
    for r in res: print(r)
    exit()
  else:
    if S[i] == "AB":
      res[i] = "A"
      dfs(i+1, a+1, b-1, c)
      res[i] = "B"
      dfs(i+1, a-1, b+1, c)
    elif S[i] == "AC":
      res[i] = "A"
      dfs(i+1, a+1, b, c-1)
      res[i] = "C"
      dfs(i+1, a-1, b, c+1)
    else:
      res[i] = "B"
      dfs(i+1, a, b+1, c-1)
      res[i] = "C"
      dfs(i+1, a, b-1, c+1)

dfs(0, A,B,C)
print("No")