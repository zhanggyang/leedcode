class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        :Valid Parentheses
        """
        if len(s)<1 :return False
        first = "([{"
        Paren = {')':'(',']':'[','}':'{'}
        stack1 = []
        for k in s:
            if k in first:
                stack1.append(k)
            elif not len(stack1) or Paren[k] !=stack1[-1]:
                return False
            else: stack1.pop()

        if  len(stack1):return False
        return True

if __name__ == '__main__':
    l1 = "(){}"
    t = Solution.isValid(Solution,l1)
    print(t)
