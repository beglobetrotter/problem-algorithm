class solution(object):
    def romanToInt(self, s):
        result, s = 0, s[::-1]
        for i in range(len(s)):
            if s[i] == 'I':
                result += 1 if result < 5 else - 1
            if s[i] == 'V':
                result += 5
            if s[i] == 'X':
                result += 10 * (1 if result < 50 else -1)
            if s[i] == 'L':
                result += 50
            if s[i] == 'C':
                result += 100 * (1 if result < 500 else -1)
            if s[i] == 'D':
                result += 500
            if s[i] == 'M':
                result += 1000
        return result

example = solution()
print(example.romanToInt("VI"))