def solution(A):
    curmin, res = float("inf"), 0
    for i in range(len(A)-1):

        if (A[i] + A[i+1]) / 2 < curmin:
            curmin = (A[i] + A[i+1]) / 2
            res = i

        if i+2 < len(A) and (A[i] + A[i+1] + A[i+2]) / 3 < curmin:
            curmin = (A[i] + A[i+1] + A[i+2]) / 3
            res = i

    return res

print(solution([4,2,2,5,1,5,5]))