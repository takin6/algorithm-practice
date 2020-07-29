def solution(A):
    peaks = []
    for i in range(1, len(A)-1):
        if A[i] > A[i+1] and A[i-1] < A[i]:
            peaks.append(i)

    group = 0
    # for g in range(1, len(A)//2+1):
    for g in range(len(A)//2, 0, -1):
        if len(A) % g != 0: continue

        # i = 0
        # member = (len(A) // g)-1
        # while i+member <= len(A)-1:
        #     if any([ j in peaks for j in range(i, i+member+1)]):
        #         i = i+member+1
        #     else:
        #         break

        # if i == len(A):
        #     return g
        block_size = (len(A) // g)
        found = [False] * g
        found_cnt = 0
        for peak in peaks:
            block_number = peak // block_size
            if not found[block_number]:
                found[block_number] = True
                found_cnt += 1

        if found_cnt == g:
            return g

    return 0

print(solution([1,2,3,4,3,4,1,2,3,4,6,2]))
print(solution([0, 1000000000, 0]))