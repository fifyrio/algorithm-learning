# https://leetcode.com/problems/valid-parentheses/


class Solution:
    # stack + mapper,
    # time complex is O(n), n是字符串s的长度
    def isValid(self, s: str) -> bool:
        # 剪枝，奇数长度的字符串肯定不是
        if len(s) % 2 == 1:
            return False      
        stack = []
        mapper = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for i in s:
            if i in mapper:
                # For the case: ")(){}",首字母是右括号
                if len(stack) == 0 or mapper[i] != stack.pop():
                    return False
            else:
                stack.append(i)                
        return len(stack) == 0   
