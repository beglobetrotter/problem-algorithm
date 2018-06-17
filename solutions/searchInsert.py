class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #if len(nums) == 0:
        #    return 0
        begin, end, mid = 0, len(nums) - 1, 0
        #if target <= nums[begin]:
        #    return begin
        #if target >= nums[end]:
        #    return end if target == nums[end] else end + 1
        while begin <= end:
            mid = (begin + end) // 2
            #print("mid:", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return begin

example = Solution()
nums = [1,3,5,6,9]
target = 0
print(example.searchInsert(nums, target))