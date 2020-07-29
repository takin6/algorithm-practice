class Combination:
  """
  O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
  n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
  使用例：
  comb = Combination(1000000)
  print(comb(5, 3))  # 10
  """
  def __init__(self, n_max, mod=10**9+7):
    self.mod = mod
    self.modinv = self.make_modinv_list(n_max)
    self.fac, self.facinv = self.make_factorial_list(n_max)

  def __call__(self, n, r):
    return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

  def make_factorial_list(self, n):
    # 階乗のリストと階乗のmod逆元のリストを返す O(n)
    # self.make_modinv_list()が先に実行されている必要がある
    fac = [1]
    facinv = [1]
    for i in range(1, n+1):
      fac.append(fac[i-1] * i % self.mod)
      facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
    return fac, facinv

  def make_modinv_list(self, n):
    # 0からnまでのmod逆元のリストを返す O(n)
    modinv = [0] * (n+1)
    modinv[1] = 1
    for i in range(2, n+1):
      modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
    return modinv

# from collections import Counter
# N = int(input())
# A = list(map(int,input().split()))
# combination = Combination(2*10**5+1)
# counter = Counter(A)
# for a in A:
#   counter[a] -= 1
#   res = 0
#   for k,v in counter.items():
#     # print(v,k)
#     res += combination(v,2)
#   counter[a] += 1
#   print(res)
from collections import defaultdict

N = int(input())
nums = list(map(int, input().split()))

counter = defaultdict(list)
for i in range(len(nums)):
  counter[nums[i]].append(i)

total = 0
for _,v in counter.items():
  v = len(v)
  total += (v * (v-1)) // 2

for k in range(len(nums)):
  t = len(counter[nums[k]])
  # import pdb; pdb.set_trace()
  print(total - t*(t-1)//2 + (t-1)*(t-2)//2)
  # print(total - ((len(counter[k])-1) * (len(counter[k])-2)//2))
