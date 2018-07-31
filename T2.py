# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L=head=ListNode(0)
        carry = 0
        while l1 and l2:
            carry= (l1.val+l2.val+carry)
            L.next = ListNode(carry%10)
            carry = carry//10
            l1 = l1.next
            l2 = l2.next
            L = L.next
        if l1:
            while l1 :
                carry = (l1.val+carry)
                L.next = ListNode(carry % 10)
                carry = carry//10
                L = L.next
        elif l2:
            while l2:
                carry = (l2.val + carry)
                L.next = ListNode(carry % 10)
                carry = carry // 10
                L = L.next
        if carry :L.next = ListNode(carry)
        return head.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        addends = l1, l2
        dummy = end = ListNode(0)
        carry = 0
        while addends or carry:
            carry += sum(a.val for a in addends)
            addends = [a.next for a in addends if a.next]
            end.next = end = ListNode(carry % 10)
            carry /= 10
        return dummy.next







