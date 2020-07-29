# N,K = list(map(int, input().split()))
# S = list(input())
# swapped = [False] * len(S)
# swap_times = 0

# for i in range(len(S)-1):
#   if S[i] == "a": continue
#   if swap_times >= K: break

#   candidates = []

#   # swap=2になるような候補
#   min_weight = min(S[i:])
#   for j in range(len(S)-1, i, -1):
#     if S[j] == min_weight:
#       candidates.append(j)
#       break

#   # swap=1になるような候補
#   swapped_ele = None
#   for j in range(i+1, len(S)):
#     if swapped[j] and S[j] < S[i]:
#       if not swapped_ele:
#         swapped_ele = j
#       else:
#         if S[swapped_ele] > S[j]:
#           swapped_ele = j
#   if swapped_ele:
#     candidates.append(swapped_ele)

#   flg = False
#   for can_idx in candidates:
#     if flg: break

#     if can_idx > i:
#       swap_t = 0
#       if not swapped[i]: swap_t += 1
#       if not swapped[can_idx]: swap_t += 1
#       if swap_t + swap_times > K: continue

#       S[i], S[can_idx] = S[can_idx], S[i]
#       if not swapped[i]:
#         swapped[i] = True
#       if not swapped[can_idx]:
#         swapped[can_idx] = True
#       swap_times += swap_t
#       flg = True

# print("".join(S))

from collections import Counter

N,K = list(map(int, input().split()))
S = list(input())
S_sorted = sorted(S)
res = ''

# store change times
diff = 0
for i in range(N):
  c = Counter(s_list[:i+1]) - Counter(res)
  for s in S_sorted:
    # current diff + ( if checking is not original char)
    diff1 = diff + (s != S[i])
    # all counting values + if c[s] has been counted
    diff2 = sum(c.values()) - (c[s] > 0)

    if diff1 + diff2 <= K:
      result += s
      S_sorted.remove(s)
      diff = diff1
      break

print(result)