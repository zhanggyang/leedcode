# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        jump = dummy
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

if __name__ == '__main__':
    l = ListNode(1)
    L = l
    i = 2
    while i<10:
        l.next = ListNode(i)
        l = l.next
        i+=1
    t = Solution.reverseKGroup(Solution,L,5)
    while t:
        print(t.val)
        t= t.next


