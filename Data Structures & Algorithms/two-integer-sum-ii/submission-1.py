class Solution:
       
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, n in enumerate(numbers):
            finding = target - n
            if finding <= numbers[-1]:
                left, right = 0, len(numbers) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if numbers[mid] == finding:
                        return [i+1, mid + 1]
                    elif numbers[mid] < finding:
                        left = mid + 1
                    else:
                        right = mid - 1
                

    
        