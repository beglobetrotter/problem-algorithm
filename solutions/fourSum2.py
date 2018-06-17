class solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        result = []
        nums.sort()
        length = len(nums)
        if 4 * nums[0] > target or 4 * nums[length - 1] < target:
            return []
        for i in range(length - 3):
            if (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + 3 * nums[length - 1] < target):
                continue
            if 4 * nums[i] > target:
                break
            if 4 * nums[i] == target and i + 3 < length and nums[i + 3] == nums[i]:
                quadruplet = [nums[i], nums[i], nums[i], nums[i]]
                result.append(quadruplet)
                break
            remain_i = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                remain_j = remain_i - nums[j]
                begin = j + 1
                end = len(nums) - 1
                while begin < end:
                    sums = nums[begin] + nums[end]
                    if sums < remain_j:
                        begin += 1
                    elif sums > remain_j:
                        end -= 1
                    else:
                        quadruplet = [nums[i], nums[j], nums[begin], nums[end]]
                        result.append(quadruplet)
                        while begin < end and nums[begin] == quadruplet[2]: begin += 1
                        while begin < end and nums[end] == quadruplet[3]: end -= 1

        return result

example = solution()
print(example.fourSum([-1, 0, 1, 2, -1, -4], -1))