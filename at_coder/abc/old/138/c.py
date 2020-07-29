import heapq
N = int(input())
A = [ i for i in list(map(int,input().split()))]
heapq.heapify(A)

for i in range(N-1):
  a = heapq.heappop(A)
  b = heapq.heappop(A)
  heapq.heappush(A, ((a+b)/2))

print(heapq.heappop(A))