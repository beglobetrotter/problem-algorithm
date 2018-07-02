class Solution:
    def permute(self, nums):
        # Solution 1
        # def generate(nums):
        #     if len(nums) == 0:
        #         yield []
        #     for index, value in enumerate(nums):
        #         for subList in generate(nums[:index] + nums[index + 1:]):
        #             yield [value] + subList
        # return list(generate(nums))

        #Solution 2
        def generate(p, nums, paren = []):
            if len(nums) > 0:
                for index, value in enumerate(nums):
                    generate(p + [value], nums[:index] + nums[index + 1:])
            else:
                paren.append(p)
            return paren
        return generate([], nums)

        #Solution 3
        #return [[value] + subList for index, value in enumerate(nums) for subList in self.permute(nums[:index] + nums[index + 1:])] or [[]]


example = Solution()
nums = [1,2,3]
print(example.permute(nums))
