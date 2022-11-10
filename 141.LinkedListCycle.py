# https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 快慢指针
    # 时间复杂度O(n)
    def hasCycle(self, head: ListNode) -> bool:
        quick = head
        slow = head
        # quick.next 为了避免一个node的case
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                return True
        return False