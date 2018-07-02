class Solution:
    def permuteUnique(self, nums):
        def generate(p, nums, paren = []):
            if len(nums) > 0:
                for index, value in enumerate(nums):
                    if index > 0 and nums[index] == nums[index - 1]:
                        continue
                    generate(p + [value], nums[:index] + nums[index + 1:])
            else:
                paren.append(p)
            return paren
        nums.sort()
        return generate([], nums)


example = Solution()
nums = [1,1,0,1]
print(example.permuteUnique(nums))