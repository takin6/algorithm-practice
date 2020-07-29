from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        # for each land cell,
        #   do bfs(r, c)
        #       - expand distance by 1 and check if land exists
        #           ex) if (r,c)==(0,0) distance 1 is (1,0) or (0,1)
        #       - start from cur_distance
        #       - avoid goind beyond the region
        
        # cur_max = 0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             print("=============================")
        #             print(r, c)
        #             cur_dist = cur_max + 1
        #             q = [(r+cur_dist,c),(r-cur_dist,c),(r,c+cur_dist),(r,c-cur_dist)]
        #             step = -1
        #             visited = []
        #             while q:
        #                 step += 1
        #                 cur_dist = cur_dist + step
        #                 s = len(q)
        #                 for _ in range(s):
        #                     i, j = q.pop(0)
        #                     print(i, j)
        #                     if (i,j) in visited or i < 0 or j < 0 or i>=len(grid) or j>=len(grid[0]):
        #                         continue
        #                     print(visited)
        #                     visited.append((i,j))
        #                     if grid[i][j] == 0:
        #                         import pdb; pdb.set_trace()
        #                         cur_max = cur_dist
        #                         #                  bottom  top     right    left
        #                     for n_i, n_j in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
        #                         if (n_i, n_j) in visited or n_i < 0 or n_j < 0 or n_i>=len(grid) or n_j>=len(grid[0]):
        #                             continue
        #                         q.append((n_i, n_j))
        
        # return cur_max

        # find a water cell that is farthest from all the land cell
        LAND,WATER=1,0
        q = []
        # 1. find the land cells
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i,j))

        visited = []
        level = -1
        while q:
            level += 1
            s = len(q)
            for _ in range(s):
                r, c = q.pop(0)

                for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                    rx, cy = r+x, c+y

                    # change 1. time limit exceeded
                    # if (rx,cy) in visited or rx < 0 or rx >= len(grid) or cy < 0 or cy >= len(grid[0]):
                    #     continue
                    # => 
                    # if 0 <= rx < m and 0 <= cy < n and grid[rx][cy] == 0:
                    #

                    # change 2. instead of having visited, change value to 1 if visited
                    #
                    # visited.append((rx,cy))

                    # if grid[rx][cy] == WATER and (rx,cy) not in q:
                    #     q.append((rx, cy))

                    if 0 <= rx < m and 0 <= cy < n and grid[rx][cy] == 0:
                        q.append((rx,cy))
                        grid[rx][cy] = 1
        return level
                                

print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
