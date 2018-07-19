class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0: return None
        result, sum = nums[0], 0
        for i in range(len(nums)):
            sum += nums[i]
            result = max(result, sum)
            sum = max(sum, 0)
        return result

example = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(example.maxSubArray(nums))