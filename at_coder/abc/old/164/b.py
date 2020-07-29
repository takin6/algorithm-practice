# A = stamina
# B = attack
# C = enemy's stamina
# D = enemy's attack

# T => A => T => A

A, B, C, D = list(map(int, input().split()))

flag = False

while A > 0 or C > 0:
  # T's attack
  C = C - B
  if C <= 0:
    flag = True
    break

  A = A - D
  if A <= 0:
    flag = False
    break

if flag:
  print("Yes")
else:
  print("No")