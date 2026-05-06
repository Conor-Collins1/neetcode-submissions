class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        topK = []

        
        for n in counts:
            if len(topK) < k or counts[n] > counts[topK[-1]]:
                
                inserted = False

                for i in range(len(topK)):
                    if counts[n] > counts[topK[i]]:
                        topK.insert(i, n)
                        inserted = True
                        break

                if not inserted:
                    topK.append(n)

                ##if len(topK) > k:
                 ##   topK.pop()

        return topK[0:k]