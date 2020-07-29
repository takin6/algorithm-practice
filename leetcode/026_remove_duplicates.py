def removeDuplicates(nums):
    idx = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[idx] = nums[i]
            idx += 1

    return idx


# print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))