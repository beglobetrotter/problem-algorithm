import itertools

class Solution:
    def groupAnagrams(self, strs):
        #solution 1
        # output = []
        # sortedStrs = sorted(strs, key=sorted)
        # for key, valueList in itertools.groupby(sortedStrs, sorted):
        #     output.append(list(valueList))
        # return output

        #solution 2
        output, mediumDict = [], {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp in mediumDict:
                mediumDict[temp].append(i)
            else:
                mediumDict[temp] = [i]
        for value in mediumDict.values():
            output.append(value)
        return output

example = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(example.groupAnagrams(strs))

