# ---- manual implementation

# def insert(key):
#   global size
#   size = size + 1
#   # pq[size] = key
#   pq.insert(size, key)
#   sift_up(size)

# def extrace_max():
#   global size
#   result = pq.pop(1)
#   last_val = pq.pop()
#   # pq.insert(1, pq[size])
#   pq.insert(1, last_val)
#   size = size - 1
#   sift_down(1)
#   return result

# def sift_up(i):
#   global size
#   while i > 1 and parent(i) <= size and pq[parent(i)] < pq[i]:
#     pq[parent(i)], pq[i] = pq[i], pq[parent(i)]
#     i = parent(i)

# def sift_down(i):
#   global size

#   max_index = i

#   l = left_child(i)
#   if l <= size and pq[l] > pq[max_index]:
#     max_index = l

#   r = right_child(i)
#   if r <= size and pq[r] > pq[max_index]:
#     max_index = r

#   if i != max_index:
#     pq[i], pq[max_index] = pq[max_index], pq[i]
#     sift_down(max_index)

# def parent(i):
#   return i // 2

# def left_child(i):
#   return 2 * i

# def right_child(i):
#   return 2 * i + 1

# size = 0
# pq = [None]

# while True:
#   commands = list(map(str, input().split()))
#   method = commands.pop(0)

#   if method == "insert":
#     insert(int(commands.pop()))
#   elif method == "extract":
#     print(extrace_max())
#   else:
#     break

# ---------------- bad sift_down ---------------
  # l, r = left_child(i), right_child(i)

  # while l <= size or r <= size:
  #   if r <= size:
  #     if l <= size and pq[l] > pq[i]:
  #       pq[i], pq[l] = pq[l], pq[i]
  #       i = l
  #       l, r = left_child(i), right_child(i)
  #     elif r <= size and pq[r] > pq[i]:
  #       pq[i], pq[r] = pq[r], pq[i]
  #       i = r
  #       l, r = left_child(i), right_child(i)
  #   else:
  #     break


# ------------ using heapq library ------

from heapq import *
import sys

q = []
while True:
  # commands = list(map(str, input().split()))
  commands=sys.stdin.readline().split()

  if commands[0] == "end":
    break

  if commands[0] == "insert":
    heappush(q, -int(commands[1]))
  else:
    print(-heappop(q))



