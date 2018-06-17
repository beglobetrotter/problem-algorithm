class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                count += 1
                nums[count - 1] = nums[i]
        return count

nums = [1, 2, 2, 2, 3, 3, 4, 4]
example = Solution()
print(example.removeDuplicates(nums))
print(nums)