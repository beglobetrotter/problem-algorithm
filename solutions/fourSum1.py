class solution(object):
    def fourSum(self, nums, target):
        def nSum(nums, target, n, result, results):
            if len(nums) < n or n < 2 or n * nums[0] > target or n * nums[-1] < target:
                return []
            if n == 2:
                begin, end = 0, len(nums) - 1
                while begin < end:
                    sums = nums[begin] + nums[end]
                    if sums < target:
                        begin += 1
                    elif sums > target:
                        end -= 1
                    else:
                        plet = [nums[begin], nums[end]]
                        results.append(result + plet)
                        while begin < end and nums[begin] == plet[0]: begin += 1
                        while begin < end and nums[end] == plet[1]: end -= 1
            else:
                for i in range(len(nums) - n + 1):
                    if (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + (n - 1) * nums[len(nums) - 1] < target):
                        continue
                    if n * nums[i] > target:
                        break
                    if n * nums[i] == target and i + n -1 < len(nums) and nums[i + n - 1] == nums[i]:
                        plet = [nums[i]] * n
                        results.append(result + plet)
                        break
                    nSum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

        results = []
        nums.sort()
        nSum(nums, target, 4, [], results)
        return results

example = solution()
print(example.fourSum([0, 1, 5, 0, 1, 5, 5, -4], 11))
#print(example.fourSum([-1, 0, 1, 2, -1, -4], -1))