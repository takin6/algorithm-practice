# import copy
# class Puzzle():
#   def __init__(self, mat, h,w,k):
#     self.g = copy.deepcopy(mat)
#     self.h = h
#     self.w = w
#     # self.k = k
#     self.k = min(k, 3)
#     self.score = 0

#   def calc(self, t):
#     tmp_score = 0

#     for i in range(self.h):
#       for j in range(self.w):
#         if self.g[i][j] > 0:
#           for k in range(self.w, -1, -1):
#             if k-j >= self.k:
#               s = set(self.g[i][j:k])
#               if len(s) == 1 and -1 not in s:
#                 tmp_score += list(s)[0] * (k-j)
#                 for l in range(j, k):
#                   self.g[i][l] = -1
#             else:
#               break

#     if tmp_score == 0:
#       return False
#     else:
#       self.score += pow(2, t) * tmp_score
#       if self.score == 642: import pdb; pdb.set_trace()
#       return True

#   def flatten(self):
#     for j in range(self.w):
#       lst = []
#       for i in range(self.h-1, -1, -1):
#         if self.g[i][j] > 0:
#           lst.append(self.g[i][j])

#       lst += [-1] * (self.h - len(lst))

#       for i in range(self.h-1, -1, -1):
#         self.g[i][j] = lst[self.h-i-1]


# import copy
# class Puzzle():
  # def __init__(self, mat, h,w,k):
  #   self.g = copy.deepcopy(mat)
  #   self.h = h
  #   self.w = w
  #   # self.k = k
  #   self.k = min(k, 3)
  #   self.score = 0

# from itertools import groupby
# def calc():
#   s = 0
#   for i in range(h):
#     gr = groupby(g[i])
#     j = 0
#     for key,it in gr:
#       if key==-1: continue
#       l = len(list(it))
#       if l >= K:
#         g[i][j:j+l] = [-1]*l
#         # for k in range(l):
#         #   g[i][j+k] = -1
#         # # print("s", key, l, key*l)
#         s += key*l
#       j += l
#       # print("j", j)

#   return s


##### AC CODE #####
# from itertools import groupby

# def calc(time):
#   t = 0
#   for i in range(h):
#     gr = groupby(g[i])
#     lst = []
#     p = 0
#     for key,it in gr:
#       j = len(list(it))
#       lst.append([p,key,j])
#       p += j
#     for j in range(len(lst)):
#       if lst[j][1] == -1:
#         continue
#       if lst[j][2] >= K:
#         t += (2**time)*lst[j][1]*lst[j][2]
#         for k in range(lst[j][0],lst[j][0]+lst[j][2]):
#           g[i][k] = -1

#   return t

# def calc(time):
#   t = 0
#   for i in range(h):
#     gr = groupby(g[i])
#     lst = []
#     p = 0
#     for key,it in gr:
#       j = len(list(it))
#       # lst.append([p,key,j])
#       if key==-1
#       p += j
#     for j in range(len(lst)):
#       if lst[j][1] == -1:
#         continue
#       if lst[j][2] >= K:
#         t += (2**time)*lst[j][1]*lst[j][2]
#         for k in range(lst[j][0],lst[j][0]+lst[j][2]):
#           g[i][k] = -1

#   return t


from itertools import groupby
def calc():
  s = 0
  for i in range(h):
    gr = groupby(g[i])
    j = 0
    for key,it in gr:
      l = len(list(it))
      if key!=-1:
        if l >= K:
          # g[i][j:j+l] = [-1]*l
          for k in range(l):
            g[i][j+k] = -1
          s += key*l
      j += l
 
  return s

def flatten():
  for j in range(w):
    lst = []
    for i in range(h-1, -1, -1):
      if g[i][j] > 0:
        lst.append(g[i][j])

    lst += [-1] * (h - len(lst))

    for i in range(h-1, -1, -1):
      g[i][j] = lst[h-i-1]

h,w,K = map(int,input().split())
mat = [ [int(e) for e in list(input())] for _ in range(h) ]

res = 0
for i in range(h):
  for j in range(w):
    score = 0
    g = [ [ mat[n][m] for m in range(w) ] for n in range(h) ]
    g[i][j] = -1
    time = 0
    flatten()
    while True:
      s = calc()
      if s==0: break
      score += (2**time)*s
      flatten()
      time += 1
    res = max(res, score)

print(res)

# https://atcoder.jp/contests/s8pc-3/submissions/14847719
# 参考

# res = 0
# for i in range(h):
#   for j in range(w):
#     g = copy.deepcopy(mat)
#     old = mat[i][j]
#     mat[i][j] = -1
#     puzzle = Puzzle(mat,h,w,k)
#     puzzle.flatten()
#     time = 0
#     while True:
#       if puzzle.calc(time):
#         puzzle.flatten()
#         time += 1
#       else:
#         break
#     res = max(res, puzzle.score)
#     mat[i][j] = old

# print(res)




      # import pdb; pdb.set_trace()
    # for m in self.mat:
    #   print(m)
    # print("===============")

    # pivot_mat = []
    # for i in range(self.w):
    #   row = []
    #   for j in range(self.h):
    #     if self.mat[j][i] != -1:
    #       row.append(self.mat[j][i])

    #   short = self.h - len(row)
    #   if short > 0:
    #     row.reverse()
    #     for k in range(short):
    #       row.append(-1)
    #     row.reverse()
      
    #   pivot_mat.append(row)

    # mat = [ [-1]*self.w for i in range(self.h) ]
    # for i in range(self.h):
    #   for j in range(self.w):
    #     mat[i][j] = pivot_mat[j][i]

    # self.mat = mat
