from typing import List
class Memo:
    def __init__(self):
        self.Alex = 0
        self.Lee = 0

class Solution:


    def stoneGame(self, piles: List[int]) -> bool:
        # def helper(piles, turn):
        #     if len(piles) < 0: return 0
        #     if len(piles) == 1: return piles[0]

        #     turn += 1
        #     if turn % 2 == 1:
        #         return max(piles[0] + helper(piles[1:], turn), piles[-1] + helper(piles[:-1], turn))
        #     else:
        #         return max(helper(piles[1:], turn), helper(piles[:-1], turn))

        # Alex = helper(piles, 1)
        # return Alex > sum(piles)-Alex

        N = len(piles)
        dp = [ [(0,0)]*(len(piles)+1) for _ in range(len(piles)+1)]
        for i in range(len(piles)):
            dp[i+1][i+1] = (piles[i], 0)

        # for i in range(1, len(piles)+1):
        #     for j in range(i+1, len(piles)+1):
        #         print(i,j)
        #         if i == 1 and j == N:
        #             import pdb; pdb.set_trace()
        #         front, back = piles[i-1]+dp[i+1][j][1], piles[j-1]+dp[i][j-1][1]
        #         if front >= back:
        #             dp[i][j] = (front,dp[i+1][j][0])
        #         else:
        #             dp[i][j] = (back,dp[i][j-1][0])

        # goes diagonal
        for l in range(2, len(piles)+1):
            for i in range(len(piles)-l+2):
                j = i+l-1
                front, back = piles[i-1]+dp[i+1][j][1], piles[j-1]+dp[i][j-1][1]
                if front >= back:
                    dp[i][j] = (front,dp[i+1][j][0])
                else:
                    dp[i][j] = (back,dp[i][j-1][0])

        return dp[1][N][0] > dp[1][N][1]
        

print(Solution().stoneGame([5,3,4,5]))
print(Solution().stoneGame([10,2,8,10,1,3,2,3,4,2]))

# 2. state: index, player(Alex/Lee) => uniquely identify out state
#    state(index, player)
# 3. formulating a relation among states
#    state(index, player) = 