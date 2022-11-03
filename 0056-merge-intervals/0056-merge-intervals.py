class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not n:
            return []
        intervals.sort(key = lambda x:x[0])
        min_heap = []
        ans = []
        
        for point in intervals:
            if not min_heap :
                heappush(min_heap , point)
            elif point[0] <= min_heap[-1][1]:
                temp = heappop(min_heap)
                x = min(point[0] , temp[0])
                y = max(point[1] , temp[1])
                heappush(min_heap , [x , y])
            else:
                temp = heappop(min_heap)
                ans.append(temp)
                heappush(min_heap , point)
        if min_heap :
            ans.extend(min_heap)
            
        return ans
                
            