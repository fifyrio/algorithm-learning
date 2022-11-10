# https://leetcode.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 快慢指针, 相遇的终点的下一个node，就是环的起点
    # O(n)
    def detectCycle(self, head: ListNode):
        quick = head
        slow = head
        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                break

        # 没有环，就返回空
        if quick is None or quick.next is None:
            return None

        # 相遇的终点的下一个node，就是环的起点
        slow = head
        while slow != quick:
            slow = slow.next
            quick = quick.next
        return slow