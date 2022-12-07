# https://leetcode.com/problems/3sum/


class Solution:
    # 新建空映射, 遍历nums, 去映射里找target-item对应的key存在？->存在则返回对应索引和当前索引；不存在则保存item:index的映射关系。注意：只有<=1种结果，所以不用考虑数组里重复元素问题，只返回第一个便可
    # Time complex: O(n), Space complex: O(n)
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapper = {}
        for i, value in enumerate(nums):
            need = target - value
            if need in mapper.keys():
                return [mapper[need], i]
            else:
                mapper[value] = i
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))