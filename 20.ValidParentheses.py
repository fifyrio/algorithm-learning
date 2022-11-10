# https://leetcode.com/problems/valid-parentheses/


class Solution:
    # stack + mapper,
    # time complex is O(n),
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for i in s:
            if i in mapper.keys():
                stack.append(i)
            else:
                # For the case: ")(){}",首字母是右括号
                if len(stack) == 0:
                    return False
                else:
                    if mapper[stack.pop()] != i:
                        return False
        return len(stack) == 0