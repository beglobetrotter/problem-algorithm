class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

haystack = "hello"
needle = "lo"
example = Solution()
print(example.strStr(haystack, needle))
