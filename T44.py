class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        :正则化匹配
        :'?'匹配单一字符
        :'*'匹配任意字符串
        """
        slen,plen = len(s),len(p)
        si,pi,s_start,p_start = 0,0,0,0
        while si<slen:
            if pi<plen and (p[pi]==s[si] or p[pi]=='?'):
                si+=1
                pi+=1
            elif pi<plen and p[pi] == '*':#依次检验匹配0次到n次的结果
                s_start,p_start = si+1,pi
                pi+=1
            elif s_start > 0 :#匹配失败且存在“*”
                si = s_start
                pi = p_start
            else:return False
        return p[pi:].count("*") == plen-pi


if __name__ == '__main__':
    s = "ba"
    p = "**b*a**"
    t = Solution.isMatch(Solution,s,p)
    print(t)



