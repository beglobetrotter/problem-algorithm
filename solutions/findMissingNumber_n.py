class solution:
    def findMissingNumber(self, nums):
        numsDict = {}
        for i in nums:
            numsDict[i] = numsDict.get(i, 0) + 1

        for key, value in numsDict.items():
            if value == 2:
                return key

example = solution()
print(example.findMissingNumber("22255577711333"))
