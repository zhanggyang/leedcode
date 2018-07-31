# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        :Merge Two Sorted Lists
        """
        if not l1 :return l2
        if not l2 :return l1
        first,second,res,tem= l1,l2,l1,l1
        if l1.val>l2.val:
            res,tem = l2,l2
            second = second.next
        else:first = first.next
        while first and second :
            if first.val > second.val:
                tem.next = second
                tem = tem.next
                second = second.next
            else:
                tem.next = first
                tem = tem.next
                first = first.next
        if not first:tem.next = first
        else :tem.next = second
        return res






