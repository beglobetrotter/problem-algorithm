class solution:
    def findMissingNumber(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if high - low + 1 < 3:
                break
            while mid + 1 <= high and nums[mid] == nums[mid + 1]:
                mid += 1
            if (mid - low + 1) % 3 == 0:
                low = mid + 1
            elif mid == high: #in this case, there should be 5 numbers (more than 3 nums, less than 6, and cannot be 4)
                return nums[low]
            else:
                high = mid
        return nums[low]

example = solution()
print(example.findMissingNumber("22255577711333"))
