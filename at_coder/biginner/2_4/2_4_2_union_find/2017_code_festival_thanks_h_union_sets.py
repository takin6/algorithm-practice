# last[x] : x が最後に「根」ではなくなった瞬間の時刻
# history[x] := xの親ノードが変わるたびに (その時刻, 新たな親) を push していく

class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)
    self.last = [-1] * (N+1)
    self.history = [ [[-1,-1]] for _ in range(N+1) ]

  def union(self, time, f, t):
    p1 = self.find(time,f)
    p2 = self.find(time,t)
    if p1 == p2:
      return

    if self.parents[p1] > self.parents[p2]:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1
    # 最後に根ではなくなった瞬間の時刻を更新
    self.last[p2] = time
    # 時刻、新たな親をhistoryに追加
    self.history[p2].append([time, p1])

  def find(self, t, x):
    if self.last[x] == -1 or t < self.last[x]: return x
    return self.find(t, self.parents[x])

  def same(self, t, n1, n2):
    return self.find(t, n1) == self.find(t, n2)

  # def size(t, x):
  #   y = self.find(t, x)
  #   idx = bisect(history[y] (t,0))-1
  #   return history[y][idx]

N,M = map(int, input().split())
uf = UF(N)
for t in range(M):
  a,b = map(int, input().split())
  uf.union(t+1, a,b)

Q = int(input())
ans = []
for _ in range(Q):
  x,y  = map(int, input().split())
  if not uf.same(M+10, x, y):
    ans.append(-1)
  else:
    l,r = 0, M+1
    while r >= l:
      mid = (l+r) // 2
      if uf.same(mid, x, y):
        r = mid-1
      else:
        l = mid+1
    ans.append(l)

for a in ans:
  print(a)