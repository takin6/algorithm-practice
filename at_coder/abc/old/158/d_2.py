from collections import deque
S = input()
dq = deque(list(S))
reverse = 1

q = int(input())
for _ in range(q):
  cmd = list(map(str,input().split()))
  if int(cmd[0]) == 1:
    reverse = 1-reverse
  else:
    if int(cmd[1]) == 1:
      if reverse:
        dq.append(cmd[2])
      else:
        dq.appendleft(cmd[2])
    else:
      if reverse:
        dq.appendleft(cmd[2])
      else:
        dq.append(cmd[2])

if reverse:
  print("".join([d for d in dq][::-1]))
else:
  print("".join(dq))
