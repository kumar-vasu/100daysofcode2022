from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_ = 0
        for pnt1, pnt2, pnt3 in combinations(points, 3):
            x1, y1 = pnt1
            x2, y2 = pnt2
            x3, y3 = pnt3
            Area =(1/2) * abs(x1*(y2 - y3) + x2*(y3 - y1)+ x3*(y1 - y2))
            max_ = max(max_, Area)
        return max_