# 1,2,3,4,5,6,7,8,9
# 10,11,12
# 21,22,23
# 32,33,34
# ...
# 98,99,90(edge)
# 10-1(edge),100,101
# 110,111,112
# 121,122,123
# ...
# 998,999,100

from collections import deque
K = int(input())
dq = deque([ i for i in range(1, 10) ])

res = None
while K > 0:
  i = dq.popleft()
  res = i
  K -= 1

  strI = str(i)
  last = int(strI[-1])
  for next in [last-1,last,last+1]:
    if next < 0 or next > 9:
      continue
    else:
      dq.append(int(strI+str(next)))
print(res)

