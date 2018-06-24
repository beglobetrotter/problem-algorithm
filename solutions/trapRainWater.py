class Solution:
    def trap(self, height):
        left, right, water = 0, len(height) - 1, 0
        maxLeft, maxRight = 0, 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    water += (maxLeft - height[left])
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    water += (maxRight - height[right])
                right -= 1
        return water

example = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(example.trap(height))