class Solution {
    maxProfit(prices) {
        let left=0
        let right=1
        let maxProfit =0
        while(right<prices.length){
            if(prices[right]>prices[left]){
                let sellProfit=prices[right]-prices[left]
                if(maxProfit<sellProfit){
                    maxProfit=sellProfit
                }
            }
            else{
                left=right
            }
            right++

        }
        return maxProfit
    }
}
