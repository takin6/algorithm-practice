# =========================================

# # lesson2: Arrays oddOccurencesInArray
# from collections import Counter
# def solution(A):
#     c = Counter(A)
#     res = [ k for k in c if c[k] % 2 == 1]
#     if res:
#         return res[0]
#     return 0

# print(solution([9,3,9,3,9,7,9]))
# print(solution([9,3,9,3,9,7,9,7,9]))

# =========================================

# # lesson3: frogjmp
# import math
# def solution(X, Y, D):
#     return math.ceil( (Y-X) / D)

# print(solution(10, 85, 30))

# =========================================

# # lesson3-2
# def solution(A):
#     N = len(A)+2
#     exp = ((N-1) * N) // 2
#     return exp - sum(A)

# print(solution([2,3,1,5]))
# print(solution([1,2,3,4,6,7,8,9,10]))
# print(solution([1,2,3,4,5,6,7,8,9]))
# print(solution([1,2,3,5,6,7,8]))

# =========================================
# lesson 3-3
def solution(A):
    N, S = len(A), [A[0]]
    for i in range(1,N):
        S.append( A[i] + S[i-1] )

    res = float('inf')
    for i in range(N-1):
        res = min(res, abs( S[i] - (S[-1]-S[i]) ))

    return res

print(solution([3,1,2,4,3]))
print(solution([3,-1,2,-4,-3]))
