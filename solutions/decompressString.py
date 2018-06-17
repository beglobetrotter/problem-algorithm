class solution:
    def decompressString(self, s):
        digit = repeated = single = ""
        stack = []
        for i in s:
            if stack and i == "]":
                while stack[-1] != "[":
                    single = stack.pop() + single
                stack.pop() #pop "["
                while stack[-1].isdigit():
                    digit = digit + stack[-1]
                    stack.pop()
                for _ in range(int(digit)):
                    repeated += single
                stack.append(repeated)
                digit = repeated = single = ""
            else:
                stack.append(i)
        return "".join(stack)

example = solution()
print(example.decompressString("a3[b2[c1[d]]]e"))