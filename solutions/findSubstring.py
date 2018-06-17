class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0 or len(s) == 0 or len(s) < len(words) * len(words[0]):
            return []
        totalLen, singleLen, calLen = len(words) * len(words[0]), len(words[0]), 0
        for i in words:
            calLen += len(i)
        if calLen != totalLen: return []
        res = []
        wordDict = {}
        for key in words:
            wordDict[key] = wordDict.get(key, 0) + 1
        start, temp, init = 0, dict(wordDict), 0
        while start < (len(s) - singleLen + 1):
            word = s[start:start+singleLen]
            if temp.get(word, 0) > 0:
                temp[word] -= 1
                start += singleLen
                init += 1
            else:
                start = start - init * singleLen + 1
                temp = dict(wordDict)
                init = 0
            if init == len(words):
                res.append(start - totalLen)
                start = start - totalLen + 1
                temp = dict(wordDict)
                init = 0
        return res

example = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
print(example.findSubstring(s, words))






