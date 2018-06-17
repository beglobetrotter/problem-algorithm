class Solution:
    def removeElement(self, nums, val):
        count = nums.count(val)
        for i in range(count):
            nums.remove(val)
        return len(nums)

nums = [1, 3, 5, 2, 5, 2, 4, 2]
example = Solution()
print(example.removeElement(nums, 9))
print(nums)
