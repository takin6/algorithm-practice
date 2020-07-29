def solution(A):
    if len(A) == 0:
        return 0

    maxprofit = -float('inf')
    sell = A[0]

    for i in range(1, len(A)):
        buy = A[i]
        maxprofit = max(maxprofit, buy-sell)
        sell = min(sell, A[i])

    if maxprofit < 0:
        return 0
    return maxprofit

print(solution([3171,1011,1123,1366,1013,1367]))
print(solution([1,1,0,1,2,3]))
print(solution([]))
print(solution([-1,-1,0,-1,-1]))
print(solution([5,4,3,2,1]))
