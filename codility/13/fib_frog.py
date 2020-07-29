# def solution(A):

#     fib_seqs = [0, 1]
#     i = 2
#     while fib_seqs[-1] <= len(A)+1:
#         fib_seqs.append(fib_seqs[i-1] + fib_seqs[i-2])
#         i += 1

#     if len(A)+1 in fib_seqs:
#         return 1

#     leaves = [ i+1 for i in range(len(A)) if A[i] == 1]
#     if len(leaves) == 0:
#         return -1
#     leaves = [0] + leaves
#     leaves.append(len(A)+1)

#     # dp = [ [0] * len(leaves) for _ in range(len(leaves)) ]

#     # for span in range(1, len(leaves)):
#     #     for i in range(len(leaves)):
#     #         j = (span+i)
#     #         if j >= len(leaves): continue

#     #         if leaves[j] - leaves[i] in fib_seqs:
#     #             dp[i][j] = 1
#     #         elif leaves[j] - leaves[j-1] in fib_seqs:
#     #             dp[i][j] = 1 + max(dp[i][j-1], dp[i+1][j])

#     # return dp[0][-1] if dp[0][-1] != 0 else -1

#     dp = [float('inf')] * len(leaves)
#     for i in range(1, len(leaves)):
#         if leaves[i] in fib_seqs:
#             dp[i] = 1
#             continue

#         for j in range(i):
#             if dp[i-j] > 0 and leaves[i]-leaves[i-j] in fib_seqs:
#                 dp[i] = min(dp[i], dp[i-j] + 1)

#         # if dp[i-1] > 0 and leaves[i]-leaves[i-1] in fib_seqs:
#         #     dp[i] = min(dp[i], dp[i-1] + 1)

#         # if dp[i-2] > 0 and leaves[i]-leaves[i-2] in fib_seqs:
#         #     dp[i] = min(dp[i], dp[i-2] + 1)

#     return dp[-1] if dp[-1] != float('inf') else -1

# def solution(A)
#     fib_seqs = [0, 1]
#     i = 2
#     while fib_seqs[-1] <= len(A)+1:
#         fib_seqs.append(fib_seqs[i-1] + fib_seqs[i-2])
#         i += 1

#     if len(A)+1 in fib_seqs:
#         return 1

#     leaves = [ i+1 for i in range(len(A)) if A[i] == 1]
#     if len(leaves) == 0:
#         return -1
#     leaves = [0] + leaves
#     leaves.append(len(A)+1)

#     dp = [float('inf')] * len(leaves)
#     for i in range(1, len(leaves)):
#         if leaves[i] in fib_seqs:
#             dp[i] = 1
#             continue

#         for j in range(i):
#             if dp[i-j] > 0 and leaves[i]-leaves[i-j] in fib_seqs:
#                 dp[i] = min(dp[i], dp[i-j] + 1)

#     return dp[-1] if dp[-1] != float('inf') else -1


def solution(A):
    # adding banks
    A.append(1)

    # generating fib sequences up to len(A)
    fib_seqs = [0, 1]
    i = 2
    while fib_seqs[-1] <= len(A)+1:
        new_fib = fib_seqs[i-1] + fib_seqs[i-2]
        if new_fib > len(A):
            break
        else:
            fib_seqs.append(new_fib)
        i += 1

    # check if the frog can reach the other side with step 1
    if len(A)+1 in fib_seqs:
        return 1
    fib_seqs = fib_seqs[1:]

    # generate dp table. mark the position the frog can reach in
    # 1 step
    dp = [-1] * len(A)
    for jump in fib_seqs:
        dp[jump-1] = 1

    for x, leaf in enumerate(A):
        if dp[x] > 0 and leaf == 1:
            for jump in fib_seqs:
                if jump + x >= len(A):
                    break
                else:
                    if dp[x+jump]<0 or dp[x+jump] > dp[x]+1:
                        dp[x+jump] = dp[x]+1

    return dp[-1]


# print(solution([0,0,0]))
print(solution([0,0,0,1,1,0,1,0,0,0,0]))
print(solution([1, 1, 0, 0, 0]))
print(solution([0, 0, 1, 0, 0, 0, 1, 1, 1, 1]))