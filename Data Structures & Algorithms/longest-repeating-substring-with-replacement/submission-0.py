class Solution:
  
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}

        L = 0
        longest = 0
        maxf = 0

        for R in range(len(s)):

            c = s[R]
            count[c] = count.get(c, 0) + 1

            if count[c] > maxf:
                maxf = count[c]

            while (R - L + 1) - maxf > k:

                left_c = s[L]
                count[left_c] -= 1
                L += 1

            if R - L + 1 > longest:
                longest = R - L + 1

        return longest

        