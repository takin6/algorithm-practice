def threesumClosest(nums, target):
    nums.sort()
    ans = 32 ** 2

    for i in range(len(nums)-2):
        # sums of three integer will always be greater than 0
        # if num[i] > 0
        # if nums[i]>target: break
        # do not get repeating results
        if i > 0 and nums[i] == nums[i-1]: continue

        l = i + 1
        r = len(nums)-1

        while l < r:
            print(i, l, r, ans)

            total = nums[i] + nums[l] + nums[r]
            if abs(target-total) < abs(target-ans): ans = total
            if total < target:
                l = l + 1
            elif total > target:
                r = r - 1
            else:
                ans = target
                break

    return ans

# print(threesumClosest([-1, 2, 1, -4], 1))
# print(threesumClosest([-1,2,1,-4], 1))
print(threesumClosest([1,1,1,1], 0))
