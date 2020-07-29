# 1. FrogRiverOne
def solution(X, A):
    # got 81% of speed
    arr = [False] * X

    for i in range(len(A)):
        if A[i]-1 < X:
            arr[A[i]-1] = True
            left -= 1

        if all(arr): return i

    return -1

    # 100%
    # arr = [False] * X
    # left = X

    # for i in range(len(A)):
    #     if A[i]-1 < X and arr[A[i]-1] == False:
    #         arr[A[i]-1] = True
    #         left -= 1

    #     if left == 0:
    #         return i

    # return -1

    # arr = [False] * (X)
    # left = X

    # for i in range(len(A)):
    #     try:
    #         if arr[A[i]-1] == False:
    #             arr[A[i]-1] = True
    #             left -= 1
    #         if left == 0:
    #             return i
    #     except:
    #         pass

    # return -1


print(solution(5,[1,3,1,4,2,3,5,4]))
print(solution(5,[1,1,2,3,5,2,2,2,2]))
print(solution(5,[1,1,2,3,5,2,2,2,2,4]))

#==========================================

