class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        :最大连续括号匹配长度
        :DP做法,反向遍历，数组保存的是以下标i开始的匹配（）的长度
        """
        maxlen = 0
        slen = len(s)
        i = slen-2
        DP = [0]*slen
        while i >= 0 :#最后一位是不匹配的
            if s[i] == '(':
                end = i + DP[i+1] + 1#匹配之后的位置
                if end < slen and s[end] == ')':
                    DP[i] = DP[i+1]+2
                    if end<slen-1:DP[i]+=DP[end+1]
            i-=1
        for i in DP:
            maxlen = max(maxlen,i)
        return maxlen

if __name__ == '__main__':
    s = "((））））()()))))"
    t = Solution.longestValidParentheses(Solution, s)
    print(t)

