class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 0

        time = 0
        prev = [points[0],0]
        nxt = [points[1],1]
        
        while nxt[1] < len(points):
            if nxt[0] == prev[0]:
                prev[0] = points[nxt[1]]
                prev[1] = nxt[1]
                if nxt[1] + 1 < len(points):
                    nxt[0] = points[nxt[1] + 1]
                nxt[1] = nxt[1] + 1
                continue
            if nxt[0][0] > prev[0][0]:
                prev[0][0] += 1
            elif nxt[0][0] < prev[0][0]:
                prev[0][0] -= 1
            if nxt[0][1] > prev[0][1]:
                prev[0][1] += 1
            elif nxt[0][1] < prev[0][1]:
                prev[0][1] -= 1
            time += 1
            
        return time