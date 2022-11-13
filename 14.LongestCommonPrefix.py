# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    # 遍历数组第一个元素+遍历数组
    # edge case: ["ab", "a"] -> "a"; ["cir", "car"] -> "c"
    # If n is the length of the array and m is the length of the shortest string, the worst case time complexity will be O(m × n)
    # 空间复杂度: O(1)
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # 数组长度这种可以保存为常量，减少查询次数
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            for j in range(1, count):
                # 不要漏了this case:第二个元素比第一个元素段的情况，使用数组index记得防止数组越界
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    # 不用单独一个变量来保存结果，直接用索引，:i表示[0,i)，<i的所有元素
                    return strs[0][:i]
        return strs[0]
