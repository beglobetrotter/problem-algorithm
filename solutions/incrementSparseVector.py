class solution(object):
    """Compute the operation v1 += scale * v2"""
    def incrementSparseVector(self, v1, scale, v2):
        for key in v2:
            v1[key] = v1.get(key, 0) + scale * v2[key]
        return v1

v1 = {'a':5}
v2 = {'c':3, 'a':2}
scale = 2
example = solution()
print(example.incrementSparseVector(v1, scale, v2))
