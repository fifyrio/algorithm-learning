# https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    # 左右指针+二分搜索
    # Time complexity: O(nlogh)
    def minEatingSpeed(cls, piles: list[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            # 二分法
            mid = (left + right) // 2

            current_h = 0

            # 计算所用的时间
            for item in piles:
                current_h += (math.ceil(item / mid))

            if current_h <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
