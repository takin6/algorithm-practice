from collections import Counter

counter = Counter()
n = int(input())

for _ in range(n):
  s = input()
  counter[s] += 1

for item in ["AC", "WA", "TLE", "RE"]:
  print("{0} x {1}".format(item, counter[item]))