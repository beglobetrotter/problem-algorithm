class solution(object):
    def reverse(self, x):
        numStr = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1])
        return numStr if numStr.bit_length() < 32 else 0

example = solution()
print(example.reverse(-12133245345466))

