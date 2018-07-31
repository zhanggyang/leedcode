class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def KMP(s,word):
            """
            :param s: 被匹配字符串
            :param word:匹配字符串
            :return:匹配的所有的开始位置
            """
            res = []
            #计算Next数组，Next数组存储的是下一位字符前有多少连续匹配的字符。
            #Next[0]=-1
            if not word:return res
            Next = []*len(word)
            Next[0] = -1
            k,i = -1,0
            while i < len(word)-1:
                if k==-1 or word[i] == word[k]:#k==-1时，表示当前字符前面没有已匹配的字符且与首位也不匹配
                    i+=1
                    k+=1
                    Next[i] = k
                else:k = Next[k]

            #利用Next数组进行匹配
            first,second = 0,0
            while first<len(s):
                if second==-1 or s[first] == word[second]:
                    first+=1
                    second+=1
                    if second ==len(s):
                        res.append(first-second)
                        second=0
                else:
                    second = Next[second]
            return  res


        nums = []*len(words)
        if len(words)<=1:return KMP(s,words)

        for _ in enumerate(words):
            nums.append(KMP(s,_))

        #将单词转换为从第几个开始出现过









