class solution(object):
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

example = solution()
height = [2, 5, 6.5, 3, 10, 8.7, 13]
print(example.maxArea(height))