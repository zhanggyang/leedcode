class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        :实现 strStr()
        :KMP实现
        """
        #next数组构造，递推构造next数组，next数组表示当前位匹配失败时，下一个应该匹配的字符串的位置
        #KMP算法通过遍历一次haystack即可找到结果
        if not needle :return 0
        if not haystack:return -1
        Next = [0]*len(needle)
        j,k = 0,-1
        Next[0] = -1#k表示当前前缀的位置
        while j<len(needle)-1:
            if k==-1 or needle[j] == needle[k]:
                k+=1
                j+=1
                Next[j] = k#表示第j位的前K项是匹配的，第j项是匹配的后一项
            else:
                k = Next[k]
        #开始匹配
        pre,cur = 0,0
        while pre<len(haystack) and cur<len(needle):
            if cur==-1 or haystack[pre] == needle[cur]:
                pre+=1
                cur+=1
            else:
                cur = Next[cur]

        if cur == len(needle):return pre - len(needle)
        else:return -1

if __name__ == '__main__':
    haystack = "aabaaabaaac"
    needle = "aabaaac"
    t = Solution.strStr(Solution,haystack,needle)
    print(t)










