class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:return 0
        profit = 0
        Min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i]>Min_price:profit = max(profit,prices[i]-Min_price)
            else:Min_price = prices[i]
        return profit
    
if __name__ == '__main__':
    p = [2,1]
    t = Solution.maxProfit(Solution,p)
    print(t)