from typing import List

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 1
        node_count = 1
        res = []
  
        while label >= node_count *2:
            node_count *= 2
            level += 1

        while label != 0:
            res.append(label)
            level_max = 2 ** (level) - 1
            level_min = 2 ** (level-1)
            label = int((level_max + level_min - label) // 2)
            level -= 1

        return res[::-1]
        
        # while True:
        #     import pdb; pdb.set_trace()
        #     parent = (((2**(level+1)-1) - (2**level))) // 2
        #     result.insert(0, parent)
        #     level = level - 1

        #     if parent == 1:
        #         break

        # return result

print(Solution().pathInZigZagTree(14))