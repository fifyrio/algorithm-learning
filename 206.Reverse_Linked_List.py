# https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 前、后指针，前指针指向null，遍历， O(n)
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    # 递归
    def reverseList2(self, head: [ListNode]) -> [ListNode]:
        pass



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = Solution().reverseList(node1)
    print(head)
