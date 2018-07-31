class Solution:
    def curSum(self,candidates,index,target,tem_res,res):
        """
        :param candidates:
        :param target:
        :param tem_res: 当前的结果
        :param res: 全局的结果
        :return:当前搜索的结果
        """
        if target == 0:
            res.append(tem_res)
            return
        if index>=len(candidates) or  target < candidates[index]:return
        for i in range(index,len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]: continue#去重操作
            if target<candidates[i]:break
            self.curSum(self,candidates,i+1,target-candidates[i],tem_res+[candidates[i]],res)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        :组合相加
        """
        res = []
        candidates.sort()
        self.curSum(self,candidates,0,target,[],res)
        return res

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1,1, 5]
    target =8
    t = Solution.combinationSum(Solution,candidates,target)
    for i in t:
        print(i)