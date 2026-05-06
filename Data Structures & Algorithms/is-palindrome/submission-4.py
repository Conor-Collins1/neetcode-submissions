class Solution:
    def isPalindrome(self, s: str) -> bool:

        right = len(s) -1
        left = 0
        while left < right:
            while ord(s[left]) > 122  or ord(s[left]) < 48  or 58 <= ord(s[left]) <= 64 or 91 <= ord(s[left]) <= 96:
                left += 1
                if left > right:
                    return True
            
            while ord(s[right]) > 122  or ord(s[right]) < 48  or 58 <= ord(s[right]) <= 64 or 91 <= ord(s[right]) <= 96:
                right -= 1
                if left > right:
                    return True

            
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True
            
        