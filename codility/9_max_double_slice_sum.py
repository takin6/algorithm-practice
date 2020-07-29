
def solution(A):
    N = len(A)
    front, back = [0]*len(A), [0]*len(A)

    for i in range(1,len(A)):
        front[i] = max(front[i-1]+A[i], 0)

    for i in range(len(A)-2, -1, -1):
        back[i] = max(back[i+1]+A[i], 0)

    maxslicesum = 0
    for i in range(1, len(A)-1):
        maxslicesum = max(maxslicesum, front[i-1]+back[i+1])

    return maxslicesum

print(solution([3,2,6,-1,4,5,-1,2]))


# choose a pair which can provide the largest differences
# 