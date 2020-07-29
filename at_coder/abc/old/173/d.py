import heapq
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)

pq = []
res = 0
heapq.heapify(pq)

for i in range(n):
  if len(pq) == 0:
    heapq.heappush(pq, -a[i])
  else:
    score = -heapq.heappop(pq)
    res += score
    for _ in range(2):
      heapq.heappush(pq, -a[i])

print(res)

# for i in range(n):
#   if len(pq) < 1:
#     heapq.heappush(pq, a[i])
#   elif len(pq) == 1:
#     heapq.haeappush(pq, a[i])
#   else:
#     res += pq[0]
#     heapq.heappush(pq, a[i])

# print(res)







  # if len(pq) == 1:
  #   res += pq[0]
  #   heapq.heappush(pq, a[i])
  #   continue


# 3 2 2 1
# 3 => 2 => 2