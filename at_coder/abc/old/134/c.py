N = int(input())
A = []
for i in range(N):
  A.append(int(input()))

first = max(A)
firstCnt = 0
firstIdx = 0
second = 0
secondIdx = 0

for i,a in enumerate(A):
  if a < first:
    if a > second:
      second = a
      secondIdx = i
  else:
    firstIdx = i
    firstCnt += 1

if firstCnt > 1:
  for i in range(N):
    print(first)
else:
  for i in range(N):
    if i == firstIdx:
      print(second)
    else:
      print(first)
