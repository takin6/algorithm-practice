from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # --------- my answer --------
        # ans = 0
        # # calc from top
        # for x in range(len(grid)):
        #     for y in range(len(grid[x])):

        #       height_from_t_to_b = []
        #       for t in grid: height_from_t_to_b.append(t[y])
        #       height_from_t_to_b = max(height_from_t_to_b)
        #       height_from_l_to_r = max( grid[x] )

        #       a = min(height_from_t_to_b, height_from_l_to_r)

        #       if a - grid[x][y] > 0:
        #           ans += a - grid[x][y]

        # return ans

        row_maxes = [ max(row) for row in grid ]
        col_maxes = [ max(col) fro col in zip(*grid) ]

        return sum( min(i, j) for i in row for j in col) - sum(map(sum, grid))



grid = [ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]
print(Solution().maxIncreaseKeepingSkyline(grid))