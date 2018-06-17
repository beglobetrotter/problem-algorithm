class solution(object):
    def lengthOfLongestSubstring(self, s):
        result = start = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                result = max(result, i - start + 1)
            usedChar[s[i]] = i
        return result

class solution2(object):
    def lengthOfLongestSubstring(self, s):
        result = start = 0
        usedChar = {}
        for i, c in enumerate(s):
            if c in usedChar and start <= usedChar[c]:
                start = usedChar[c] + 1
            else:
                result = max(result, i - start + 1)
            usedChar[c] = i
        return result

s = "dvdf"
example = solution()
print(example.lengthOfLongestSubstring(s))

