def solution(A, B):
    # N = len(A)
    # eaten = 0
    # i = 0
    # j = 1

    # while True:
    #     if i >= N or i+j >= N:
    #         break

    #     if B[i] == 0:
    #         i = i + 1
    #         continue

    #     if B[i] == 1 and B[i+j] == 0:
    #         if A[i] > A[i+j]:
    #             j += 1
    #             eaten += 1
    #         else:
    #             i,j = j+1,1
    #             eaten += 1
    #     else:
    #         i,j = i+1, 1

    # return N - eaten 

    N = len(A)
    survives = 0
    stack = []

    for i in range(N):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                survives += 1
        else:
            stack.append(A[i])

    survives += len(stack)
    return survives

print(solution([4,3,2,1,5], [0,1,0,0,0]))
print(solution([4,3,2,1,5], [0,1,1,0,0]))
print(solution([4,3,2,1,5], [1,0,0,0,0]))
# print(solution([4,3,2,1,5], [0,0,0,0,1]))



