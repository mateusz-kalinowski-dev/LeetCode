class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time = 1
        max_time = max(ranks)*cars*cars
        n = len(ranks)

        while min_time < max_time:
            mid = (min_time + max_time)//2
            repaired = 0
            x = 0
            while x < n:
                cars_sqrt = mid // ranks[x]
                repaired += int(math.sqrt(cars_sqrt))
                x += 1
            if repaired >= cars:
                max_time = mid
            else:
                min_time = mid+1
        return min_time 
