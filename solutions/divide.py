class Solution:
    def divide(self, dividend, divisor):
        # positive = (dividend > 0) == (divisor > 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # res = 0
        # while dividend >= divisor:
        #     temp, i = divisor, 1
        #     while dividend >= temp:
        #         dividend -= temp
        #         res += i
        #         i <<= 1
        #         temp <<= 1
        # if not positive:
        #     res = -res
        # return min(max(-2**31, res), 2**31 - 1)
        if (not divisor) or (dividend == -2 ** 31 and divisor == -1):
            return 2 ** 31 - 1
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        temp, multiple = divisor, 1
        while dividend >= divisor:
            dividend -= temp
            res += multiple
            multiple += multiple
            temp += temp
            if dividend < temp:
                temp = divisor
                multiple = 1
        return sign * res




example = Solution()
print(example.divide(-100, 3))

