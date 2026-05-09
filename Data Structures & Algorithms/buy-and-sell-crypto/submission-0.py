class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]

        max = 0
        current = prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            current = i - lowest

            if current > max:
                max = current

        return max
        
            




        