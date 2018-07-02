class Solution:
    def jump(self, nums):
        # n, step, currentMax, start, maxJump = len(nums), 0, 0, 0, 0
        # while currentMax < n - 1:
        #     step += 1
        #     for i in range(start, currentMax + 1):
        #         maxJump = max(maxJump, nums[i] + i)
        #         if maxJump >= n - 1:
        #             return step
        #     start, currentMax = currentMax + 1, maxJump
        # return step

        n, step, currentMax, start, maxJump = len(nums), 0, 0, 0, 0
        while currentMax < n - 1:
            step += 1
            start, currentMax = currentMax + 1, max(nums[i] + i for i in range(start, currentMax + 1))
        return step

        # cur, next, step = 0, 1, 0
        # while next < len(nums) and cur < next:
        #     cur, next = next, max(id + nums[id] for id in range(cur, next)) + 1
        #     step += 1
        # return step if next >= len(nums) else -1

example = Solution()
nums = [2,3,1,1,1,2,2]
print(example.jump(nums))

