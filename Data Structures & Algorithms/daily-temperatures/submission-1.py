class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        carrying = []
        answer = [0] * len(temperatures)
        i = 0
        for temp in temperatures:

            if not carrying:
                carrying.append(i)
            else:
                
                while carrying and temperatures[carrying[-1]] < temp:
                    answer[carrying[-1]] =(i - carrying[-1])
                    carrying.pop()
                carrying.append(i)
            
            i += 1
        
        return answer
        