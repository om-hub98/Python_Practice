import heapq

class Solution:
    def my_approach_countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
            intervals.sort()
            intersect = 0
            for i in range(len(intervals)-1):
                for j in range(i+1,len(intervals)):
                    diff = intervals[i][1] - intervals[j][0]
                    if diff >= 0:
                        intersect += 1
            return intersect
    
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intersect = 0
        for i in range(len(intervals)-1):
            for j in range(i+1,len(intervals)):
                if max(intervals[i][0], intervals[j][0]) <=  min(intervals[i][1], intervals[j][1]):
                    intersect += 1
        return intersect    

    def optimizedCountIntersectingIntervals(self, intervals: list[list[int]]) -> int:
            intervals.sort()
            active = []
            count = 0
            for start, end in intervals:
                while active and active[0] < start:
                    heapq.heappop(active)

                count += len(active)
                print(f"Count: {count}")
                heapq.heappush(active, end)

            return count

intervals = [
            [[97,100],[61,61]],
            [[86,87],[34,90]],
            [[1,5],[2,3],[3,4]]
        ]   
sol = Solution()
for arr in intervals:
    print(sol.my_approach_countIntersectingIntervals(arr))
    #print(sol.countIntersectingIntervals(arr))
    #print(sol.optimizedCountIntersectingIntervals(arr))
