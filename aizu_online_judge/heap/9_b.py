import copy
n = 10
nodes = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

n = int(input())
nodes = list(map(int, input().split()))
heap = copy.deepcopy(nodes)
heap.insert(0, None)
# in case if the right node of the last tree is None
MIN_INF = -10 ** 10
heap.append(MIN_INF)
# heap starts with 1, 2, 3, ... n

def max_heapify(i):
  l = 2 * i
  r = 2 * i + 1

  if l <= n and heap[l] > heap[r] and heap[l] > heap[i]:
    heap[l], heap[i] = heap[i], heap[l]
    max_heapify(l)
  elif r <= n and heap[l] < heap[r] and heap[r] > heap[i]:
    heap[r], heap[i] = heap[i], heap[r]
    max_heapify(r)

  # print(heap)

i = n // 2
while i != 0:
  max_heapify(i)
  i -= 1

print(" " + " ".join([str(i) for i in heap[1:-1]]))