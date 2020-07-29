def solution(A):
    N = len(A)
    east = 0
    res = 0

    for i in range(N):
        if A[i] == 0:
            east += 1
        else:
            res += east

            if res > 1000000000:
                return -1
    return res

print(solution([0,1,0,1,1]))
print(solution([0,0,0,1,1]))