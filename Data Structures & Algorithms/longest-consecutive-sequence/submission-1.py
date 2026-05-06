class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        highestC = 0

        seen = {}
        for i in nums:
            seen[i] = True
        
        for i in seen.keys():
            if i - 1 not in seen:
                count = 1
                while i + count in seen:
                    count += 1
                
                if count > highestC:
                    highestC = count
        
        return highestC
            


        