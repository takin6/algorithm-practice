# N, M, Q = list(map(int, input().split()))
# dic = {}

# for _ in range(Q):
#   a,b,c,d = list(map(int, input().split()))

#   if a in dic and b in dic[a]:
#     if d > dic[a][b][1]:
#       dic[a][b] = [c,d]
#   else:
#     if a not in dic:
#       dic[a] = {}
#     dic[a][b] = [c,d]

# print(dic)

# import heapq

# N, M, Q = list(map(int, input().split()))
# pq = []

# for _ in range(Q):
#   a,b,c,d = list(map(int, input().split()))
#   heapq.heappush(pq, (-d,[a,b,c]))

# cnt = [None] * N
# res = 0
# while pq:
#   val, lst = heapq.heappop(pq)
#   a,b,c = lst

#   if cnt[a-1] and cnt[b-1]:
#     if cnt[b-1] - cnt[a-1] == c:
#       res += -val
#     continue

#   if cnt[a-1] is None and cnt[b-1] is None:
#     cnt[a-1], cnt[b-1] = 10**5, 10**5+c
#   elif cnt[b-1] is None:
#     cnt[b-1] = cnt[a-1] + c
#   elif cnt[a-1] is None:
#     cnt[a-1] = cnt[b-1] - c

#   res += -val
# print(res)


### itertools ###
# import itertools
# N, M, Q = map(int, input().split())
# abcd = [ list(map(int, input().split())) for _ in range(Q) ]

# res = 0
# for product in itertools.combinations_with_replacement(range(1, M+1), N):
#   S = 0
#   for a,b,c,d in abcd:
#     if product[b-1] - product[a-1] == c:
#       S += d
#   res = max(res, S)

# print(res)

n,m,q=map(int,input().split())
A=[]
for i  in range(q):
  A.append(list(map(int,input().split())))
ans=0
def judge(Q):
  now=0
  for l in A:
      a,b,c,d=l
      if Q[b-1]-Q[a-1]==c:
          now+=d
  global ans
  ans=max(ans,now)
  return
 
# python program to implement dfs
def dfs(L):
  if len(L)==n:
    judge(L)
    return
  jj=L[-1] if len(L)>0 else 1
  for i in range(jj,m+1):
    L.append(i)
    dfs(L)
    L.pop()
 
dfs([])
print(ans)