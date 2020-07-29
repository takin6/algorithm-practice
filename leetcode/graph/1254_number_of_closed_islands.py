from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        visited = set()

        def dfs(row, col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return False
            if grid[row][col] == 1:
                return True
            if (row, col) in visited:
                return True
            
            visited.add((row, col))

            top, bottom, left, right = dfs(row-1,col), dfs(row,col-1), dfs(row,col+1), dfs(row+1,col)
            return top and bottom and left and right

            # this expression ends if any one of the element is FALSE!!!
            # return dfs(row-1,col) and dfs(row,col-1) and dfs(row,col+1) and dfs(row+1,col)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i, j) not in visited:
                    print("==============================")
                    self.i = i
                    self.j = j
                    r = dfs(i, j)
                    if r:
                        print(i, j)
                    result += 1 if r else 0

        return result

# grid = [ [1,1,1,1,1,1,1],
#          [1,0,0,0,0,0,1],
#          [1,0,1,1,1,0,1],
#          [1,0,1,0,1,0,1],
#          [1,0,1,1,1,0,1],
#          [1,0,0,0,0,0,1],
#          [1,1,1,1,1,1,1]]
# grid = [ [0,0,1,0,0],
#          [0,1,0,1,0],
#          [0,1,1,1,0]]
grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0] ]
print(Solution().closedIsland(grid))

# wrong
# 1 5
# 0 5
# 1 4
# 1 6
# 2 5
# 1 5
# 2 4
# 2 6
# 1 6
# 2 5
# 2 7
# 3 6
# 2 6
# 3 5
# 2 5
# 3 4
# 2 4
# 3 3
# 2 3
# 3 2
# 3 4
# 4 3
# 3 3
# 4 2
# 3 2
# 4 1
# 3 1
# 4 0
# 3 0
# 2 0
# 3 -1

# ok 
# 1 5
# 0 5
# 1 4
# 1 6
# 2 5
# 1 5
# 2 4
# 2 6
# 1 6
# 2 5
# 2 7
# 3 6
# 2 6
# 3 5
# 2 5
# 3 4
# 2 4
# 3 3
# 2 3
# 3 2
# 3 4
# 4 3
# 3 3
# 4 2
# 3 2
# 4 1
# 3 1
# 4 0
# 3 0
# 2 0
# 3 -1
# 3 1
# 4 0
# 4 -1
# 4 1
# 5 0
# 4 0
# 5 -1
# 5 1
# 6 0
# 4 2
# 5 1
# 4 3
# 5 2
# 4 2
# 5 1
# 5 3
# 6 2
# 4 4
# 3 4
# 4 3
# 4 5
# 3 5
# 4 4
# 4 6
# 5 5
# 5 4
# 4 4
# 5 3
# 5 5
# 6 4
# 5 3
# 3 5
# 4 4
# 3 6
# 4 5
# 3 7
# 4 6
# 3 5