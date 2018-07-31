class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        :双指针解法
        """
        res = ""
        slen,tlen = len(s),len(t)
        if slen < tlen :return res
        table = {}
        for i,schar in enumerate(t):
            if schar in table:table[schar]+=1
            else: table[schar] =1
        first,last,count,M = 0,0,0,slen+1
        while last<slen:
            if s[last] not in table:last+=1
            elif table[s[last]]>=1:
                table[s[last]]-=1
                count += 1
                if count == tlen:
                    while s[first] not in table :first+=1
                    tem = last - first + 1
                    if tem<M:
                        M,res = tem,  s[first:first + tem]
                last+=1
            elif count == tlen:
                table[s[last]] -= 1
                while first<=last:
                    if s[first] not in table:first+=1
                    elif table[s[first]] >= 0:
                        table[s[first]]+=1
                        first+=1
                        count-=1
                    else:
                        table[s[first]] += 1
                        first+=1
                        if count == tlen:#
                            while s[first] not in table:first+=1
                            tem = last - first + 1
                            if tem < M:
                                M, res = tem, s[first:first + tem]
                        break
                last+=1
            else:last+=1
        return res

if __name__ == '__main__':
    S = "aaaaaaaaaaaabbbbbcdd"

    T = "abcdd"
    t = Solution.minWindow(Solution,S,T)
    print(t)




















