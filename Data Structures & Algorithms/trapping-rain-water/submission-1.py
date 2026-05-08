class Solution:
    def trap(self, height: List[int]) -> int:
        
        last_h_l = 0
        last_h_r = 0

        total = 0
        L = 0
        R = len(height) - 1

        for i in (height):

            hL = height[L]
            hR = height[R]
            if hR > hL:
                
                if last_h_l - hL > 0:
                    total += last_h_l - hL
                
                if height[L] > last_h_l:
                    last_h_l = height[L]
                L +=1
            else:
                if last_h_r - hR > 0:
                    total += last_h_r - hR
                
                if height[R] > last_h_r:
                    last_h_r = height[R]
                R -=1
        return total


    
# 0 1 0 3 5 3 0 4 0 2 3 1 0 3 1 0 1 3 2
