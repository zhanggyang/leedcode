class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        :正则化匹配
        :
        """
        if len(p) == 0:
            return (len(s)==0)
        if len(p) == 1:
            return len(s)==1 and (s[0]==p[0] or p[0]=='.')
        if p[1] !='*':
            if len(s) == 0 :return False
            return  (s[0]==p[0] or p[0]=='.') and self.isMatch(self,s[1:],p[1:])
        return ((s[0]==p[0] or p[0]=='.')and  self.isMatch(self,s,p[2:])) or self.isMatch(self,s[2:],p[2:])

if __name__ == "__main__":
        l1 = "ab"
        l2 = ".*"
        t = Solution.isMatch(Solution,l1,l2)
        print(t)



















