class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(self,text, pattern[2:]) or first_match and self.isMatch(self,text[1:], pattern))
        else:
            return first_match and self.isMatch(self,text[1:], pattern[1:])

if __name__ == "__main__":
        l1 = "ab"
        l2 = ".*"
        t = Solution.isMatch(Solution,l1,l2)
        print(t)


