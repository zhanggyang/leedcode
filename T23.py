# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        :k排序
        """
        if len(lists) < 0:return []
        if len(lists) == 1 :return lists[0]
        elif len(lists) == 2:
            first = lists[0]
            second = lists[1]
            if not first: return second
            if not second:return first
            res,tem = first,first
            if first.val <= second.val:
                first = first.next
            else:
                res,tem = second,second
                second = second.next
            while first and second:
                if first.val <= second.val:
                    tem.next = first
                    tem = tem.next
                    first = first.next
                else:
                    tem.next = second
                    tem = tem.next
                    second = second.next
            if not first :tem.next = second
            else:tem.next = first
            return res
        else:
             l1 = self.mergeKLists(self,lists[:(len(lists)//2)])
             l2 = self.mergeKLists(self,lists[(len(lists)//2):])
             return self.mergeKLists(self,[l1,l2])

if __name__ == '__main__':
    s1 = ListNode(2)
    s2 = ListNode(3)
    k = [s1,s2]
    t = Solution.mergeKLists(Solution,k)
    while t:
        print(t.val)
        t = t.next




