class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        :生成n对匹配括号
        """
        def generate(first,second,result,results):
            if not first :
                result += ')'*second
                return results.append(result)
            elif first == second:
                result+='('
                return generate(first-1,second,result,results)
            else:return generate(first-1,second,result+'(',results) or generate(first,second-1,result+')',results)

        res = []
        generate(n,n,"",res)
        return res
if __name__ == '__main__':
    n = 0
    t = Solution.generateParenthesis(Solution,n)
    print(t)

