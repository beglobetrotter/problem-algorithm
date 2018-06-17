class solution(object):
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = 0 - nums[i]
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                sum = nums[begin] + nums[end]
                if sum < target:
                    begin += 1
                elif sum > target:
                    end -= 1
                else:
                    triple = [nums[i], nums[begin], nums[end]]
                    result.append(triple)
                    while begin < end and nums[begin] == triple[1]: begin += 1
                    while begin < end and nums[end] == triple[2]: end -= 1

        return result

example = solution()
print(example.threeSum([1, 1, -2, 1, 1, -3, 2]))