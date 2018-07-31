class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        ：锯齿形转换
        """
        if numRows ==1 or numRows>=len(s):
            return s
        L = ['']*numRows
        idex,flag = 0,True
        for x in s:
            L[idex] += x
            if(flag):
                idex += 1
                if idex == numRows:
                    flag = False
                    idex = idex - 2
            else:
                idex -= 1
                if idex < 0:
                    flag = True
                    idex = idex + 2
        return ''.join(L)

if __name__ == "__main__":
    s ="ABC"
    t = Solution.convert(Solution,s,2)
    print(s)
    print(t)






