class Solution:
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(0, len(p)):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '?' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j] or dp[i][j])

        return dp[-1][-1]

example = Solution()
s = "acdcb"
p = "a*c?b"
print(example.isMatch(s, p))
