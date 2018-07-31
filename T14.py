class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :最大公共字符串前缀
        """
        if len(strs) == 0 :return ''
        str = strs[0]
        for x in strs:
            i=0
            while i < len(str)and i<len(x):
               if (x[i]==str[i]):
                   i+=1
               elif i==0:return ''
               else:
                   break
            if i == 1:
                str = '' + str[0]
            else:str = str[:i]
        return str

if __name__ == "__main__":
        l1 = ["abc","ab","abcd"]
        t = Solution.longestCommonPrefix(Solution,l1)
        print(t)


