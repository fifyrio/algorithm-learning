# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    # 遍历数组第一个元素+遍历数组
    # edge case: ["ab", "a"] -> "a"; ["cir", "car"] -> "c"
    # If n is the length of the array and m is the length of the shortest string, the worst case time complexity will be O(m × n)
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res                    
            res += strs[0][i]
        return res