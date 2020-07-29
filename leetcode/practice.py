from typing import List
def findPairs(nums: List[int], k: int) -> int:
    from collections import Counter
    c = Counter(nums)
    ans = 0

    for val in c:
        if k == 0:
            if c[val] >= 2: ans += 1
        else:
            if k > 0 and (val + k) in c:
                ans += 1
            elif k < 0 and (k - val) in c:
                ans += 1
    
    return ans

print(findPairs([1,2,3,4,5], -1))