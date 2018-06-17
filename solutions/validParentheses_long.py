class solution(object):
    def isValid(self, s):
        parentheses = {'(':1, ')':-1,'[':2, ']':-2, '{':3, '}':-3}
        validList = []

        if len(s) == 0:
            return True

        if len(s) % 2 == 1:
            return False

        for i in range(len(s)):
            if validList == []:
                validList.append(parentheses[s[i]])
            else:
                if parentheses[s[i]] + validList[-1] == 0:
                    validList.pop()
                else:
                    validList.append(parentheses[s[i]])

        if len(validList) == 0:
            return True
        else:
            return False

example = solution()
print(example.isValid("[]{}()"))
