# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 1. 初始化一个dummy node（虚节点）,让tail=dummy
    # 2. 不停比较l1, l2的值
    # 3. 注意遍历过程中l1、l2其中一个到达尾结点，而另一个没有到达，让tail指向没有到达尾结点的链表
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # 注意遍历过程中l1、l2其中一个到达尾结点，而另一个没有到达，让tail指向没有到达尾结点的链表
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next


if __name__ == '__main__':
    head1 = ListNode(1, ListNode(2, ListNode(4)))
    head2 = ListNode(1, ListNode(3, ListNode(4)))
    head = Solution().mergeTwoLists(head1, head2)
    print(head)

