class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1
        answer = []
        found_0 = 0
        for n in nums:
            if n == 0:
                found_0 += 1
            else:
                total *= n
        
        if found_0 == 1:
            for n in nums:
                if n == 0:
                    answer.append(int(total))
                else:
                    answer.append(0)
            return answer

        if found_0 > 1:
            for n in nums:
                answer.append(0)
            return answer
        
        for n in nums:
            answer.append(int(total / n))
        
        return answer
        