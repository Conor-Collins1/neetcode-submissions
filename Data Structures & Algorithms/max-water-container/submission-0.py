class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max = 0
        R = len(heights) - 1
        L = 0
        
        
        for h in heights:
            if heights[R] > heights[L]:

                total = (R - L) * heights[L]
                L += 1
            else:
                total = (R - L) * heights[R]
                R -= 1
            if total > max:
                max = total
        
        return max
            
            







##  2 7 4 9 2 0 1 4 6 8 2 5 8 4 5 8 2 3 6 2 3 10 8 5 3

         
        



        