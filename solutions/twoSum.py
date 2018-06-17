class solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                return [dic[num], i]
            else:
                dic[target - num] = i

nums = [2, 7, 11, 5]
target = 9
example = solution()
print(example.twoSum(nums, target))


