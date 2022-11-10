# https://leetcode.com/problems/climbing-stairs/


class Solution:
    # 递归+记忆化，f(n)=f(n-1)+f(n-2)，由于只需要n-1, n-2，所以只保存这两个变量即可(a, b)；也可以保存所有的状态到数组
    # time complexity:O(n)
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(2, n + 1):
            # 交换
            a, b = b, a + b
        return b
