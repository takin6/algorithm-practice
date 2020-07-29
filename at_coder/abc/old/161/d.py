# X : 隣り合うどの２つの桁の値について、差の絶対値が１以下
# ex) 1234


# 1 2 3 4 5 6 7 8 9

# 2 digits : 3 each
# 00 01 => 2(not count )
# 10 11 12 => 3
# 21 22 23 => 3
# 32 33 34 => 3
# ...
# 98 99 => 2

# 3 digits
# 0xx => 0x(2)+1x(3) = 5
# 1xx => 0x(2)+1x(3)+2x(3) = 8
# 2xx => 1x(3)+2x(3)+3x(3) = 9
# 3xx => 2x(3)+3x(3)+4x(3) = 9
# ...
# 9xx => 8x(3)+9x(2) = 5

# 4 digits
# 1xxx => 0xx + 1xx + 2xx => 5+8+8 = 20 
# 2xxx => 1xx + 2xx + 3xx => 8*3 = 24


# MAX_INT = 10**4
# dp = [ [None for _ in range(10)] * MAX_INT ]

from collections import deque

K = int(input())
queue = deque([i for i in range(1,10)])

while K != 0:
  if K <= len(queue):
    print(queue[K-1])
    exit(0)

  K -= 1
  num = queue.popleft()

  o = int(str(num)[-1])
  for n in [o-1, o, o+1]:
    if n == -1 or n == 10: continue
    queue.append( int(str(num)+str(n)) )
