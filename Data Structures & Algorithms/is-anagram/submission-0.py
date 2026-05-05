class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChar: dict[str, int] = {}
        tChar: dict[str, int] = {}
        for i in s:
            sChar[i] = 1 + sChar.get(i, 0)
        
        for i in t:
            tChar[i] = 1 + tChar.get(i, 0)
            
            
        return sChar == tChar

        