class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmaps = []
        answer = []
        listCount = 0
        for i, string in enumerate(strs):

            iDict = {}
            for char in string:
                iDict[char] = 1 + iDict.get(char, 0)

            found = False
            for i, s in enumerate(hashmaps):
                
                if iDict == s:

                    answer[i].append(string)
                    found = True

            if not found:
                answer.append([string])
                hashmaps.append(iDict)
                listCount += 1

        return answer


            
        



        