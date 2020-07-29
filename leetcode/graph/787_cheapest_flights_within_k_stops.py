
from typing import List
from heapq import *
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # create adj_list
        dic = collections.defaultdict(dict)
        for s, d, w in flights:
            dic[s][d] = w
        # dic = { 0: { 1: 100, 2: 500 }, 1: {2: 100}}

        # weight, source, max_stop+1
        pq = [(0, src, K+1)]
        while pq:
            cost, source, stop = heappop(pq)

            if source == dst:
                return cost
            

            if stop > 0:
                for k, v in dic[source].items():
                    heappush(pq, (cost+v, k, stop-1))

        return -1

# print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[2,1,500]], 0, 2, 0))

