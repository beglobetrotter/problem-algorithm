class solution(object):
    def myAtoi(self, str):
        str = str.strip()
        if(len(str) == 0):
            return 0
        sign = -1 if str[0] == '-' else 1
        if str[0] == '-' or str[0] == '+':
            str = str[1:]
        result, index = 0, 0
        while index < len(str) and str[index].isdigit():
            result = result * 10 + int(str[index])
            index += 1

        return max(-2 ** 31, min(sign * result, 2 ** 31 - 1))



str = "    -12312243546434545    "
example = solution()
print(example.myAtoi(str))