class solution(object):
    def threeSumCloseat(self, nums, target):
        if len(nums) <= 3:
            return sum(nums)
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            begin = i + 1
            end = len(nums) - 1
            while begin < end:
                print(begin, begin, end)
                sums = nums[i] + nums[begin] + nums[end]
                double = [nums[begin], nums[end]]
                if abs(target - result) > abs(target - sums):
                    result = sums
                    if result == target:
                        return result
                while sums > target and begin < end and nums[end] == double[1]:
                    end -= 1
                while sums <= target and begin < end and nums[begin] == double[0]:
                    begin += 1
        return result

example = solution()
print(example.threeSumCloseat([1,1,1,1], 3))