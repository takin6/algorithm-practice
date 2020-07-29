# --------------- initial solution -----------------------
# def foursum(nums, target):
#     nums = sorted(nums)
#     print(nums)
#     ans = []

#     for i in range(len(nums)-3):
#         cur_val = nums[i]
#         l, r = i+1, len(nums)-1
#         m = (r+l)//2

#         while l != m and r != m and l != r:
#             print(i, l, m, r)

#             left, mid, right = nums[l], nums[m], nums[r]
#             tmp = cur_val + left + mid + right

#             if tmp == target:
#                 ans.append([cur_val, left, mid, right])

#                 l += 1
#                 while left == nums[l]: l += 1

#                 # m += 1
#                 # while mid == nums[m]: mid += 1

#                 r -= 1
#                 while right == nums[r]: r += 1

#             elif tmp > target:
#                 r -= 1
#             elif tmp < target:
#                 l += 1

#             m = (r+l)//2

#     return ans


def threeSum(nums, target):
    nums = sorted(nums)
    result = []
    for i in range(len(nums) - 2):
        l = i+1
        r = len(nums)-1
        t = target-nums[i]

        while l < r:
            tmp = nums[l] + nums[r]

            if tmp == t:
                tup = (nums[i], nums[l], nums[r])
                result.append(tup)

                while l+1 < len(nums) and nums[l] == nums[l+1]: l += 1
                while r-1 > 0 and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif tmp > t:
                r -= 1
            else:
                l += 1

    return result    

# print(threeSum([1, 0, -1, 0, -2, 2], 0))

def fourSum(nums, target):
    nums = sorted(nums)
    ans = set()
    for i in range(len(nums)):
        result = threeSum(nums[i+1:], target-nums[i])
        for a in result: ans.add((nums[i],) + a)

    return [ list(i) for i in list(ans)]

# print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([5,5,3,5,1,-5,1,-2], 4))


# print(foursum([1, 0, -1, 0, -2, 2], 1))
# [-1,  0, 0, 1],[-2, -1, 1, 2],

# sort: [-2, -1, 0, 0, 1, 2]
# l, r, m = i+1, len(nums)-1, l+r//2
# tmp = cur + l + r + m
# if target

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]