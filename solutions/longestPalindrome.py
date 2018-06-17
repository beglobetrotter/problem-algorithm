class solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
        maxLen = 1
        start = 0
        for i in range(1, len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue
            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]


s = "aabaacaab"
example = solution()
print(example.longestPalindrome(s))
