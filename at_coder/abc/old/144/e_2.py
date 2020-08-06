# N people Team
# 1 ~ N, A = [costs]


# F = [food costs]
# Rule
# - assign 1 food to 1 member
# - digestion = x * y
# - max(teams) = seiseki

# k shugyou
#  - 1 shugyou / - 1 cost

# K = 14
# A = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
# F = [9, 9, 8, 8, 7, 6, 4, 3, 3, 2, 2]

#            -1 -2 -2 -2 -2 -1 -1   -3
# A = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 6]


N,K = map(int,input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

if sum(A) <= K:
  print(0)
  exit()

A.sort()
F.sort(reverse=True)

def check(x):
  k = 0
  for a,f in zip(A, F):
    k += max(0, a-(x//f))

  return k <= K

# AをX以下にできるか？?
ng,ok = 0, 10**18+1
while ok-ng > 1:
  x = (ok+ng)//2
  if check(x):
    ok = x
  else:
    ng = x

print(ok)







