class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right

            elif prices[left] < prices[right]:
                if Profit < prices[right] - prices[left]:
                    Profit = prices[right] - prices[left]

            right += 1

        return Profit