class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit=0
        for i in range(len(prices))    :
            for j in range(i+1,len(prices))   :
                if(Profit < prices[j]-prices[i]):
                    Profit=prices[j]-prices[i]
        return Profit