class solution(object):
    def isMatch(self, s, p):
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p)):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1])

        print(dp)
        return dp[-1][-1]

example = solution()
print(example.isMatch("", "c*"))

