# i = 0, 8
# blocks = 1
# stack = [8]

# i = 1, 8
# blocks = 1
# stack = [8]
# case1. same length as last element of stack

# i = 2, 5
# blocks = 2
# stack = [5]
# case2. smaller than the last element of stack
# => increment blocks,
# while stack[-1] < weight: pop()
# append()

# i = 3, 7
# blocks = 3
# stack = [5,7]
# case3. larger than the last element
# => increment blocks
# append()

# i = 4, 9
# blocks = 4
# stack = [5,7,9]
# case3

# i = 5, 8
# blocks = 5
# stack = [5,7,8]

# i = 6, 7
# blocks = 5
# stack = [5,7]
# case4. smaller but the block with the same reach has been found

# i = 7, 4
# blocks = 6
# stack = [4]

# i = 8
# blocks = 7
# stack = [8]

from collections import deque
def solution(H):
    stack = []
    blocks = 0

    for i in range(len(H)):
        if len(stack) == 0 or H[i] > stack[-1]:
            stack.append(H[i])
            blocks += 1

        if H[i] < stack[-1]:
            while stack and stack[-1] > H[i]: 
                stack.pop()

            # if len(stack) == 0:
            #     blocks += 1
            #     stack.append(H[i])
            #     continue

            # if stack[-1] != H[i]:
            #     blocks += 1
            #     stack.append(H[i])

            if len(stack) != 0 and stack[-1] == H[i]:
                pass
            else:
                blocks += 1
                stack.append(H[i])

    return blocks

print(solution([8,8,5,7,9,8,7,4,8]))