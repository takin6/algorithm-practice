from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        rem = k
        
        for n in num:
            if stack and rem>0 and n < stack[-1]:
                while stack and rem>0 and n < stack[-1]:
                    stack.pop()
                    rem -= 1
            stack.append(n)
        

        # while stack and rem>0:
        #     stack.pop()
        #     rem -= 1

        # while stack and stack[0] == '0':
        #     stack.popleft()
        
        # if len(stack) == 0:
        #     return "0"

        if rem > 0:
            return "".join(stack)[:-rem].lstrip("0") or "0"
        else:
            return "".join(stack).lstrip("0") or "0"

print(Solution().removeKdigits("45219", 2))
# 45219, 1
# => 4219
# 45219, 2
# => 219
print(Solution().removeKdigits("1432219", 3))
print(Solution().removeKdigits("10", 2))
print(Solution().removeKdigits("10200", 1))