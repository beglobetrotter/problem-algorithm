class Solution:
    def firstMissingPositive(self, nums):
        # nums.sort()
        # numPos = 0
        # for i, value in enumerate(nums):
        #     if value > 0:
        #         numPos += 1
        #         if numPos == 1:
        #             if value > 1:
        #                 return 1
        #         else:
        #             if value - nums[i - 1] > 1:
        #                 return nums[i - 1] + 1
        # return nums[-1] + 1 if len(nums) != 0 else 1
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n + 1



example = Solution()
nums = [1,2,0]
print(example.firstMissingPositive(nums))

