from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    flag = False
                    
                    for k in range(len(grid)):
                        if k == i: continue
                        if grid[k][j] == 1:
                            flag = True
                            break
                    
                    for h in range(len(grid[0])):
                        if h == j: continue
                        if grid[i][h] == 1:
                            flag = True
                            break
                    
                    import pdb; pdb.set_trace()
                    if flag == True: 
                        res += 1
        
        return res   

print(Solution().countServers([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,1,0,0]]))