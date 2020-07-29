from collections import deque,Counter

N,L = map(int,input().split())
A = list(map(int,input().split()))
INT_MIN = -10**15

q = deque()
c = Counter()

cur_max = INT_MIN
for i in range(N):
  if A[i] > cur_max:
    cur_max = A[i]
  q.append(A[i])
  counter[A[i]] += 1

  if (i+1) >= L:
    print(cur_max)

    pop = q.popleft()
    c[pop] -= 1
    if cur_max == pop and not c[pop]:
      if len(q) > 0:
        cur_max = max(q)
      else:
        cur_max = INT_MIN