# N, A, B= list(map(int, input().split()))
# MAX = 10 ** 9 + 7

# def cmod(n, k):
#   x, y = 1, 1
#   for i in range(k):
#     x *= (n-i)
#     y *= (k-i)

#   return  (x * pow(y, MAX-2, MAX)) % MAX

# total = 2 ** N - 1
# print( (total - cmod(N, A) - cmod(N, B)) % (MAX))

# ==================== solution ====================
# def cmod(n, r, p):
#     x,y  = 1, 1
#     for i in range(r):
#         x = x * (n - i) % p
#         y = y * (r - i) % p

#     # オプション引数 z を指定すると、x の y 乗を z で割ったときの剰余（余り）を返します
#     return (x // pow(y, p - 2, p)) % p
 
 
# n, a, b = map(int, (input().split()))
# p = 10 ** 9 + 7
# print((pow(2, n, p) - 1 - cmod(n, a, p) - cmod(n, b, p)) % p)

# 1．2^nを効率化する方法について
# math.powについて
# https://python.atelierkobato.com/power/
# 
# math.powと繰り返し二乗法
# https://math.nakaken88.com/textbook/cp-binary-exponentiation-and-recursive-function/
#
# 2. n choose k
# nCa = n! / a!(n-a!)
#     = n * (n-1) * ... * (n-a+1) / a!

# 3. 余りを計算する計算について
# 余りに関係する計算
# https://math.nakaken88.com/textbook/cp-remainder/
#
# モジュラ逆数について
# https://nevertoolate.hatenablog.jp/entry/2020/03/27/060000
#
# 1000000007 で割ったあまり
# https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-%E5%89%B2%E3%82%8A%E7%AE%97-a--b
#
# modの問題
# https://rikeilabo.com/congruence

# nCr in competitive programming
# https://ikatakos.com/pot/programming_algorithm/number_theory/mod_combination

# https://img.atcoder.jp/abc156/editorial.pdf

N, A, B = list(map(int, input().split()))
MAX_INT = 10**9 + 7

def choose(n, k):
  x, y = 1, 1
  for i in range(k):
    x = x * (n-i) % MAX_INT
    y = y * (k-i) % MAX_INT

  return ( x * pow(y, MAX_INT-2, MAX_INT) ) % MAX_INT

print( (pow(2, N, MAX_INT) - 1 - choose(N, A) - choose(N, B)) % MAX_INT)

# def cmod(n, r, p):
#   x,y  = 1, 1
#   for i in range(r):
#     x = x * (n - i) % p
#     y = y * (r - i) % p
#   return (x * pow(y, p - 2, p)) % p

# n, a, b = map(int, (input().split()))
# p = 10 ** 9 + 7
# print((pow(2, n, p) - 1 - cmod(n, a, p) - cmod(n, b, p)) % p)