class Solution:
    def nextPermutation(self, nums):
        smallIndex, length, largestSmallIndex = -1, len(nums), 0
        if length > 1:
            for i in range(length - 1):
                if nums[-1 - i - 1] < nums[-1 - i]:
                    smallIndex = length -2 - i
                    break
            if smallIndex == -1:
                nums[:] = nums[::-1]
            else:
                for i in range(length):
                    if length -1 - i > smallIndex and nums[length -1 - i] > nums[smallIndex]:
                        largestSmallIndex = length -1 - i
                        break
                nums[smallIndex], nums[largestSmallIndex] = nums[largestSmallIndex], nums[smallIndex]
                nums[smallIndex + 1:] = nums[smallIndex + 1:][::-1]

example = Solution()
nums = [3,2,1]
print(nums)
example.nextPermutation(nums)
print(nums)
