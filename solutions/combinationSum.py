class Solution:
    def combinationSum(self, candidates, target):
        result = []
        self.searchDFS(candidates, target, 0, [], result)
        return result

    def searchDFS(self, candidates, target, begin, selected, result):
        if target < 0:
            return
        if target == 0:
            result.append(selected)
            return
        for i in range(begin, len(candidates)):
            self.searchDFS(candidates, target - candidates[i], i, selected + [candidates[i]], result)

example = Solution()
candidates = [4,2,8]
target = 8
print(example.combinationSum(candidates, target))