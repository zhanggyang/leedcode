class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        :数字组合
        """
        diction = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",
                    '7':"pqr",'8':"stu",'9':"wxyz"}
        re = ['']

        for i in digits:
            tem = []
            for k in re:
              for j in diction[i]:
                    tem.append(k+j)
            re = tem
        return re

if __name__ == "__main__":
    l1 = ""
    t = Solution.letterCombinations(Solution, l1)
    print(t)







