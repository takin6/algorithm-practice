from typing import List
import collections

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # ---- my sol -----
        # backets = {}

        # for p in range(len(groupSizes)):
        #     size = groupSizes[p]

        #     if backets.get(size) is None:
        #         backets[size] = [p]
        #     else:
        #         backets[size].append(p)

        # ans = []
        # for size in backets.keys():
        #     n = backets[size]

        #     while len(n) > size:
        #         group = n[:size]
        #         ans.append(group)
        #         n = n[size:]

        #     if n is not None: ans.append(n)

        # return ans



        # ---- faster and shorter answer ------
        count = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            count[size].append(i)
        return [l[i:i + s] for s, l in count.items() for i in range(0, len(l), s)]


print(Solution().groupThePeople([3,3,3,3,3,1,3]))


# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]