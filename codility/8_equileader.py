from collections import Counter, deque
def solution(A):
    # front = []
    # N = len(A)
    # counter = Counter()
    # for c, i in enumerate(range(N)):
    #     counter[A[i]] += 1
    #     common, cnt = counter.most_common()[0]
    #     if cnt > (c+1) // 2:
    #         front.append(common)
    #     else:
    #         front.append(None)

    # back = deque()
    # counter = Counter()
    # for c, i in enumerate(range(N-1, -1, -1)):
    #     counter[A[i]] += 1
    #     common, cnt = counter.most_common()[0]
    #     if cnt > (c+1) // 2:
    #         back.appendleft(common)
    #     else:
    #         back.appendleft(None)

    # equileaders = 0
    # for i in range(0, N-1):
    #     if front[i] is None or back[i+1] is None:
    #         continue
    #     if front[i] == back[i+1]:
    #         equileaders += 1

    # return equileaders

    leader, total_cnt = Counter(A).most_common()[0]
    left = 0
    equileaders = 0
    for idx, value in enumerate(A):
        if value == leader:
            left += 1
        if left > (idx+1)//2 and (total_cnt-left)>(len(A)-(idx+1))//2:
            equileaders += 1

    return equileaders

print(solution([4,3,4,4,4,2]))
# print(solution([4,4,3,3,3,4,4,4]))
print(solution([3,3,4,4,4,3,3,3]))

