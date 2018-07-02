class Solution:
    def multiply(self, num1, num2):
        result = [0] * (len(num1) + len(num2))
        position = len(result) - 1
        for i in num1[::-1]:
            multiplyPosition = 0
            for j in num2[::-1]:
                result[position - multiplyPosition] += (ord(i) - ord('0')) * (ord(j) - ord('0'))
                result[position - multiplyPosition - 1] += result[position - multiplyPosition] // 10
                result[position - multiplyPosition] %= 10
                multiplyPosition += 1
            position -= 1
        k = 0
        while k < len(result) and result[k] == 0:
            k += 1
        if k == len(result):
            return "0"
        else:
            return ''.join(map(str, result[k:]))

example = Solution()
num1 = "123"
num2 = "456"
print(example.multiply(num1, num2))
