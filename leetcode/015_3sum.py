def threesum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)-2):
        # sums of three integer will always be greater than 0
        # if num[i] > 0
        if nums[i]>0: break
        # do not get repeating results
        if i > 0 and nums[i] == nums[i-1]: continue

        l = i + 1
        r = len(nums)-1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l = l + 1
            elif total > 0:
                r = r - 1
            else:
                arr = [nums[i], nums[l], nums[r]]
                ans.append(sorted(arr))

                # while l<r and nums[l]==nums[l+1]: 
                #   print(l)
                #   l+=1

                # while l<r and nums[r]==nums[r-1]:
                #   print(r)
                #   r-=1

                l = l + 1
                r = r - 1

    return ans


print(threesum([-1,0,1,2,-1,-4]))


# A solution set is:
# [
#   [-1, 0, 1],
#   [\-1, -1, 2]
# ]