class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0: return [-1, -1]
        low, high, start, end = 0, len(nums) - 1, -1, -1
        while low < high: #start
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        if nums[low] == target:
            start = low
        else:
            return [-1, -1]
        high = len(nums) - 1
        while low < high: #end
            mid = (low + high) // 2 + 1
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid
        end = high  # no need to compare nums[high] with target
        return [start, end]

example = Solution()
print(example.searchRange([5,7,7,8,8,8,8,9], 8))