class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tran = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i,num= 0,0
        while i<len(s):
            if i<len(s)-1 and tran[s[i]] < tran[s[i+1]] :
                num-=tran[s[i]]
            else:num+=tran[s[i]]
            i+=1
        return num
if __name__ == "__main__":
        l1 = "MMMCCCXXXIII"
        t = Solution.romanToInt(Solution,l1)
        print(t)