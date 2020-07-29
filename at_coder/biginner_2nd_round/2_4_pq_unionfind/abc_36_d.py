import heapq
N = int(input())
A = list(map(int,input().split()))

C = A[0:N]
S = sum(C)
prefix = [S]
heapq.heapify(C)
for i in range(N, 2*N):
  heapq.heappush(C,A[i])
  popped = heapq.heappop(C)
  S = S + A[i] - popped
  prefix.append(S)

C = [-e for e in A[2*N:]]
S = -sum(C)
suffix = [S]
heapq.heapify(C)
for i in range(2*N-1, N-1, -1):
  heapq.heappush(C,-A[i])
  popped = heapq.heappop(C)
  S = S + A[i] - (-popped)
  suffix.append(S)

res = -10**15 
j = len(suffix)-1
for i in range(len(prefix)):
  res = max(res, prefix[i] - suffix[j])
  j -= 1

print(res)