
# def solution(N, A):
#     res = [0] * N
#     curmax = 0
#     for i in range(len(A)):

#         if 1 <= A[i] <= N:
#             res[A[i]-1] += 1
#             curmax = max(curmax, res[A[i]-1])
#         else:
#             res = [curmax] * N

#     return res

# from collections import defaultDict
# def solution(N, A):
#     # 1. get lats largest sum & idx
#     counter = [0] * N
#     lastmax = False
#     prev_counter = Counter()
#     M = len(A)

#     for i in range(M-1, -1, -1):
#         if not lastmax:
#             if A[i] > N:
#                 lastmax = True
#             else:
#                 X = A[i]-1
#                 counter[X] = counter[X] + 1
#         else:
#             if A[i] > N:
#                 break
#             else:
#                 prev_counter[A[i]] += 1

#     accu = 0
#     if len(prev_counter) > 0:
#         accu = prev_counter[max(prev_counter)]
#     return [ i + accu for i in counter ]

from collections import deque, Counter
def solution(N, A):
    d = deque()
    M = len(A)
    curmax = 0

    for i in range(M):
        if A[i] > N:
            counter = Counter()
            while len(d) > 0:
                counter[d.popleft()] += 1
            if len(counter) > 0:
                curmax += counter[max(counter)]
        else:
            d.append(A[i])

    res = [curmax] * N
    for e in d:
        res[e-1] += 1

    return res

print(solution(10,[9,9,9,9,109,9,9,9,9,18,9,29]))
# print(solution(3,[1,3,1,3,3,4,5]))
# print(solution(5,[1,2,3,4,1,2,3,4,6,5]))
# print(solution(5,[3,4,4,6,5,1,4,4]))