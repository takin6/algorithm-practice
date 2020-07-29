def f(x):
  return x + P/2**(x/1.5)

P = float(input())
high,low = 100,0
while high-low>0.000000001:
  mid_left = high/3 + low*2/3
  mid_right = high*2/3 + low/3
  if f(mid_left) > f(mid_right):
    low = mid_left
  else:
    high = mid_right

print(f(high))


# https://juppy.hatenablog.com/entry/2019/04/11/ARC054_-B_%E3%83%A0%E3%83%BC%E3%82%A2%E3%81%AE%E6%B3%95%E5%89%87_-_%E4%B8%89%E5%88%86%E6%8E%A2%E7%B4%A2_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder


# https://naoyat.hatenablog.jp/entry/2012/01/04/231801