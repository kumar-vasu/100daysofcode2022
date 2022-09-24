class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poi = []
        for i in timeSeries:
            poi.append([i, i+duration -1])
            if len(poi) > 1:
                if poi[-2][1] >= poi[-1][0]:
                    if poi[-2][1] > poi[-1][1]:
                        poi.pop(-1)
                        
                    else:
                        poi[-2][1] = poi[-1][1]
                        poi.pop(-1)
        
        dur = 0
        for i in poi:
            dur += i[1] - i[0] + 1
            
        return dur