class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low
        # sell high
        low, profit = prices[0], 0
        for i in range(len(prices)):
            # if we found a new low, set low to that and continue.
            if prices[i] < low:
                low = prices[i]
                continue
            # calculate profit 
            else:
                profit = max(profit, prices[i] - low)
        return profit

