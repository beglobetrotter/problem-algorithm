from functools import reduce

class solution(object):
    def letterCombinations(self, digits):
        numletter = {'0':' ', '1':'*', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if not digits: return []
        elif len(digits) == 1: return list(numletter[digits])
        letters = [numletter[i] for i in digits]
        return reduce(lambda x, y: [i + j for i in x for j in y], letters)

example = solution()
print(example.letterCombinations('2'))