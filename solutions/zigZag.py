class solution(object):
    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s
        zigZag = [""] * numRows
        index, step = 0, 1
        result = ""

        for x in s:
            zigZag[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step

        print(zigZag)

        return "".join(zigZag)

example = solution()
print(example.convert("PAHNAPLSIIGYIR", 4))