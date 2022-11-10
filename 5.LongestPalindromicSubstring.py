# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    # 双指针，从中间向两边进行双指针检查，注意奇数、偶数长度的字符串，中间点不一样
    # 回文是，正着读，反着读都一样
    # time complexity:O(n*n)
    def longestPalindrome(self, s: str) -> str:
        # 回文是，正着读，反着读都一样
        # 从中间向两边进行双指针检查，注意奇数、偶数长度的字符串，中间点不一样
        longest = ''

        def findLongest(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        for i in range(len(s)):
            # 字符串长度为奇数
            s1 = findLongest(s, i, i)
            if len(s1) > len(longest): longest = s1

            # 字符串长度为偶数
            s2 = findLongest(s, i, i + 1)
            if len(s2) > len(longest): longest = s2

        return longest
