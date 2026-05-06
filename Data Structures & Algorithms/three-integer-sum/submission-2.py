class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        map = {}
        double = {}
        


        for i, n in enumerate(nums):
            if n in map:
                double[n] = i
            else:
                map[n] = i
        
        for i, n in enumerate(nums):

            for j, x in enumerate(nums):

                if j != i:
                    need = 0 - n - x
                    if need in map:
                        if (map[need] == i or map[need] == j):
                            if need in double:
                                if (double[need] != i and double[need] != j):
                                    if sorted([n, x, need]) not in answer:
                                        answer.append(sorted([n, x, need]))
                        else:
                            if sorted([n, x, need]) not in answer:
                                answer.append(sorted([n, x, need]))
        return answer





        