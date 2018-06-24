import itertools

class Solution:
    def countAndSay(self, n):
        begin = '1'
        for _ in range(n - 1):
            temp = ""
            for num, subList in itertools.groupby(begin):
                temp += (str(len(list(subList))) + num)
            begin = temp
        return begin

example = Solution()
print(example.countAndSay(7))