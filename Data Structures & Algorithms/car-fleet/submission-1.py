class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed))
        fleets = 0
        arrivals = []
        
        for D, S in cars:
            arrival = (target - D) / S
            arrivals.append(arrival)
       

        while len(arrivals) > 0:
            fleets += 1

            while len(arrivals) > 1 and arrivals[-2] <= arrivals [-1]:
                arrivals[-2] = arrivals[-1]
                arrivals.pop()
            arrivals.pop()


        return fleets
        
        
        