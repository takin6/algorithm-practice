from collections import deque

S = input()
Q = int(input())

deque = deque([c for c in S])
flag = 0

for _ in range(Q):
  pack = input().split()

  T = int(pack[0])
  if T == 1:
    flag = flag ^ 1

  if T == 2:
    F, C = int(pack[1]), pack[2]
    if F == 1:
      if flag:
        deque.append(C)
      else:
        # 最初に追加するパターン
        deque.appendleft(C)
    if F == 2:
      if flag:
        deque.appendleft(C)
      else:
        # 最後尾に追加するパターン
        deque.append(C)

print("".join(reversed(deque) if flag else deque))


# ex)
# S = "a"
# Q = 4
# 2 1 p
# S = "pa"
# 1
# S = "ap"
# 2 2 c
# S = "apc"
# 1
# S = "cpa"


# answer
# gcwojuitrmsnzprkdnngenxztucxkbmdymqkodyyjjhdfvfximjfwcgacqyizcykqasatjbenkhwmvl
# gcwmithknnbjtaztuckcziykbcmqagkcodyyjjhdfvfximjfwydmqxyqasxnegnndkrpzesmrwujovl