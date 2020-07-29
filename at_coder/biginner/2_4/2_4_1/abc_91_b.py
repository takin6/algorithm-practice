from collections import Counter
N = int(input())
dic = Counter()
for _ in range(N):
  dic[input()] += 1
M = int(input())
for _ in range(M):
  dic[input()] -= 1
 
if dic.most_common():
  freq = dic.most_common()[0][1]
  print(max(freq, 0))
else:
  print(0)