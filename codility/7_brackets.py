from collections import deque
def solution(S):
    if S == "":
        return 1
    
    # counter = {"(": 0, "[": 0, "{": 0}
    # opening = {")": "(", "]": "[", "}": "{"}
    # for c in S:
    #     if c in ["(", "[", "{"]:
    #         counter[c] += 1
    #     else:
    #         if counter[opening[c]] == 0:
    #             return 0
    #         else:
    #             counter[opening[c]] -= 1
    
    # if all([ i == 0 for i in counter.values() ]):
    #     return 1
    # else:
    #     return 0

    stack = deque()
    opening = ["(", "{", "["]
    for c in S:
        if c in opening:
            stack.append(c)
            continue

        if len(stack) == 0:
            return 0

        if c == ")":
            if stack.pop() != "(":
                return 0
        if c == "]":
            if stack.pop() != "[":
                return 0
        if c == "}":
            if stack.pop() != "{":
                return 0

    if len(stack) != 0:
        return 0

    return 1
                

# print(solution('([)()]'))
# print(solution('{[()()]}'))
# print(solution('{[()()]}}'))

print(solution('())'))
