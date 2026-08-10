def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)
    
    k = 2  # First two elements are always valid
    
    for i in range(2, len(nums)):
        # Check if current element differs from element 2 positions back
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    
    return k