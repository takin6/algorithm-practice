N = int(input())
S = input()

r,b = 0,0

for s in S:
  if s == "R":
    r += 1
  else:
    b += 1

if r > b:
  print("Yes")
else:
  print("No")