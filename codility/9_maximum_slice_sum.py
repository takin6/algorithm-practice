def solution(A):
    # write your code in Python 3.6
    res = A[0]
    prev = A[0]
    for i in range(1, len(A)):
        res = max(res, A[i], prev+A[i])
        prev = max(prev+A[i], A[i])

    return res

print(solution([3,2,-6,4,0]))
print(solution([-6,3,2,5,0]))
print(solution([100,-99,10,20]))