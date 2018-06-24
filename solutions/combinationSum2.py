class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.searchDFS(candidates, target, 0, [], result)
        return result

    def searchDFS(self, candidates, target, begin, selected, result):
        if target < 0:
            return
        if target == 0:
            result.append(selected)
            return
        for i in range(begin, len(candidates)):
            if i > begin and candidates[i] == candidates[i - 1]:
                continue
            self.searchDFS(candidates, target - candidates[i], i + 1, selected + [candidates[i]], result)

example = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(example.combinationSum2(candidates, target))