from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) is 0:
#             return -1

#         point = self.find_pivot(0, len(nums)-1, nums)
#         import pdb; pdb.set_trace()
#         if point == -1:
#             return self.bs(0, len(nums)-1, nums, target)

#         if nums[point] == target:
#             return point

#         if nums[0] <= target:
#           # search in nums2
#           return self.bs(0, point, nums, target)

#         return self.bs(point+1, len(nums)-1, nums, target)
        
#     def bs(self, low, high, nums, target):
#         if high < low:
#             return -1

#         mid = int((low+high) / 2)
#         if nums[mid] == target:
#             return mid
#         if target > nums[mid]:
#             return self.bs(mid+1,high,nums,target)

#         return self.bs(low,mid-1,nums,target) 
    
#     def find_pivot(self, low, high, nums):
#         if high < low:
#             return -1
#         if low == high:
#             return low

#         mid = int((low + high) / 2)
#         if mid < high and nums[mid] > nums[mid+1]:
#             return mid
#         if mid > low and nums[mid] < nums[mid-1]:
#             return mid - 1
#         if nums[low] >= nums[mid]:
#             return self.find_pivot(low, mid-1, nums)

#         return self.find_pivot(mid+1, high, nums)



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums)-1, nums, target)
        
    def binary_search(self, left, right, nums, target):
        if left > right:
            return -1
        
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                # target exists in the left
                return self.binary_search(left, mid, nums, target)
            else:
                return self.binary_search(mid+1, right, nums, target)
        
        else:
            if nums[mid] < target <= nums[right]:
                return self.binary_search(mid+1, right, nums, target)
            else:
                return self.binary_search(left, mid, nums, target)

print(Solution().search([6,7,1,2,3,4,5],6))

print(Solution().search([4,5,6,7,0,1,2],0))
print(Solution().search([4,5,6,7,0,1,2],3))
print(Solution().search([],5))
print(Solution().search([1],1))
print(Solution().search([1],0))
print(Solution().search([3,1],1))
