class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        :最大连续括号匹配长度
        :利用堆栈将不合法的括号下标留在数据结构中
        """
        stack = []
        res,start = 0,0
        stack.append(-1)
        for k in range(len(s)):
            if s[k]=='(':stack.append(k)
            else:
                stack.pop()
                if not stack:stack.append(k)
                else:
                    res = max(res,k-stack[-1])
        return res

if __name__ == '__main__':
    s = ""
    t = Solution.longestValidParentheses(Solution,s)
    print(t)