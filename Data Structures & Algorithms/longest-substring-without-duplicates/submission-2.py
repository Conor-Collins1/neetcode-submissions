class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max = 0
        tail = 0
        count = 0
        current = [0]*100
        for i, n in enumerate(s):
            while current[ord(n) - 32] != 0:
                current[ord(s[tail]) - 32] = 0
                tail += 1
                count -= 1
            else:
                count += 1
                if count > max:
                    max = count
                
            
            current[ord(n) - 32] = 1
        return max









                
            



        
    
    # 142534251435124351243512351423542532415