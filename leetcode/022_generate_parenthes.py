from typing import List

class Solution:
    # --------- my answer with backtrack ---------------
    # def generateParenthesis(self, n: int) -> List[str]:
        

    #     def helper(cur, opening, closure, ans):
    #         if opening == 0 and closure >= 0:
    #             cur += ")" * closure
    #             ans.append(cur)
    #             return ans

    #         if closure < opening: return
    #         if opening > 0 and closure == 0: return

    #         helper(cur + ")", opening, closure-1, ans)
    #         helper(cur + "(", opening-1, closure, ans)
    #         # helper(cur + ")", opening, closure-1, ans) or helper(cur + "(", opening-1, closure, ans)

    #         return ans

    #     # ans = helper('(', n-1, n, set())
    #     ans = helper('(', n-1, n, [])

    #     return ans

    # ----------- Solution with Backtrack -----------------
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return

            if left < n:
                backtrack(S+'(', left+1, right)

            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

print(Solution().generateParenthesis(3))
# print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(1))
