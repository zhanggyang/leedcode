# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        :交换链表相邻的值
        """
        res = ListNode(0)
        res.next = head
        tem = res
        first = head
        if not head or not head.next: return head
        second = first.next
        while first and second:
            tem.next = second
            first.next = second.next
            second.next = first
            tem = first
            first = tem.next
            if not first: break
            second = first.next
        return res.next
if __name__ == '__main__':
    l= ListNode(1)
    L = l
    l.next = ListNode(2)
    l = l.next
    l.next = ListNode(3)


    t = Solution.swapPairs(Solution,L)
    while t:
        print(t.val)
        t = t.next


