class solution(object):
    def isValid(self, s):
        parentheses = {')':'(',']':'[', '}':'{'}
        validList = []
        if len(s) == 0:
            return True
        if len(s) % 2 == 1:
            return False
        for i in s:
            if validList and (i in parentheses and parentheses[i] == validList[-1]):
                validList.pop()
            else:
                validList.append(i)

        return not validList

example = solution()
print(example.isValid("[{}]()"))
