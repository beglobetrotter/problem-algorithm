class Solution:
    def search(self, nums, target):
        low, high, temp, mid = 0, len(nums) - 1, 0, 0
        while low <= high:
            mid = (low + high) // 2
            if target < nums[0]:
                if nums[mid] < nums[0]:
                    temp = nums[mid]
                else:
                    temp = -float('inf')
            elif target > nums[0]:
                if nums[mid] >= nums[0]:
                    temp = nums[mid]
                else:
                    temp = float('inf')
            else:
                return 0
            if target < temp:
                high = mid - 1
            elif target > temp:
                low = mid + 1
            else:
                return mid
        return -1

example = Solution()
print(example.search([6,7,8,9,0,1,2,3,4,5], 10))
