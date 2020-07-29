# from collections import deque
# M = int(input())
# deq = deque()

# for _ in range(M):
#   d,c = map(int,input().split())
#   for _ in range(c):
#     deq.append(d)

# def is_handred():
#   if deq[0]==1 and deq[1]==0 and deq[2]==0:
#     return True
#   return False

# times = 0
# while len(deq) > 1:
#   if len(deq) == 3 and is_handred():
#     deq = deque([1,0])
#   else:
#     i,j = deq.popleft(), deq.popleft()
#     for x in list(str(i+j)):
#       deq.append(int(x))

#   times += 1

# print(times)

M = int(input())

cur = 0

keta = 0
csum = 0
for _ in range(M):
  d,c = map(int,input().split())
  s = 0
  for i in str(d):
    s += int(i)
  csum += s * c
  keta += c

# 9をカウントしたくないため
print(keta-1 + (csum-1)//9)


# edge cases
# 17
# 4 1
# 0 1
# 9 1
# 5 1
# 0 1
# 5 1
# 1 1
# 4 1
# 2 1
# 3 2
# 5 1
# 7 1
# 9 1
# 0 1
# 8 1
# 7 1
# 0 1