class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1: # if odd
                pow *= x
            x *= x
            n >>= 1
        return pow

example = Solution()
print(example.myPow(2, 5))


