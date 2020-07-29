import heapq
N = int(input())
a = list(map(int, input().split()))
m = len(a) // 2

cumsumA = []
prefix = [x for x in a[:N]]
heapq.heapify(prefix)
cumsumA.append(sum(prefix))
cursum = sum(prefix)
for k in range(N, 2*N):
  heapq.heappush(prefix, a[k])
  ele = heapq.heappop(prefix)
  cursum = cursum + a[k] - ele
  cumsumA.append(cursum)
  # cumsumA.append(sum(prefix))

cumsumB = []
suffix = [-x for x in a[2*N:]]
heapq.heapify(suffix)
cumsumB.append(-sum(suffix))
cursum = -sum(suffix)
for k in range(2*N-1, N-1, -1):
  heapq.heappush(suffix, -a[k])
  ele = heapq.heappop(suffix)
  cursum = cursum + a[k] + ele
  cumsumB.append(cursum)

res = -float('inf')
for i in range(0, len(cumsumA)):
  res = max(res, cumsumA[i] - cumsumB[len(cumsumA)-i-1])

print(res)
