class Solution:
    def longestValidParentheses(self, s):
        if len(s) <= 1:
            return 0
        parentheses = {'(': 1, ')': -1}
        parenthesesStack, parenthesesNum = [], 0
        for i in range(len(s)):
            if parenthesesStack and (parentheses[s[i]] < 0 and parentheses[s[i]] + parentheses[s[parenthesesStack[-1]]] == 0):
                parenthesesStack.pop()
            else:
                parenthesesStack.append(i)
        if len(parenthesesStack) == 0:
            return len(s)
        else:
            end = len(s)
            while parenthesesStack:
                parenthesesNum = max(parenthesesNum, end - parenthesesStack[-1] - 1)
                end = parenthesesStack[-1]
                parenthesesStack.pop()
            parenthesesNum = max(parenthesesNum, end)
        return parenthesesNum

example = Solution()
print(example.longestValidParentheses("(())((()"))
