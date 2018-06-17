from functools import reduce

class sulotion(object):
    def longestCommonPrefix(self, strs):
        def lcp(s, t):
            if len(s) > len(t):
                s, t = t, s
            for i in range(len(s)):
                if s[i] != t[i]:
                    return s[:i]
            return s
        return reduce(lcp, strs) if strs else ""


strs = ["abcde", "abcde", "abcb"]
example = sulotion()
print(example.longestCommonPrefix(strs))
