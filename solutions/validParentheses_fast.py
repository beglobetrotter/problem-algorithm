class solution(object):
    def isValid(self, s):
        parentheses = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
        validList = []
        if len(s) % 2 == 1:
            return False
        for i in s:
            if validList and (parentheses[i] < 0 and parentheses[i] + validList[-1] == 0):
                validList.pop()
            else:
                validList.append(parentheses[i])

        return not validList

example = solution()
print(example.isValid("}{"))
