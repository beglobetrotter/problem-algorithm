class solution(object):
    def sparseDotProduct(self, V1, V2):
        """return sum(V1[key] * V2.get(key, 0) for key in V1)"""
        total = 0
        for key in V1:
            total = total + V1[key] * V2.get(key, 0)
        return total

V1 = {'a':5}
V2 = {'a':3, 'b':2}
example = solution()
print(example.sparseDotProduct(V1, V2))