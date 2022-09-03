class Solution:
    def maxHeight(self, cuboids) -> int:
        for i in range(len(cuboids)):
            cuboids[i].sort()
        cuboids.sort()
        maxLis = 0
        Lis = [x[2] for x in cuboids]
        for i in range(len(cuboids)):
            for j in range(i):
                if(cuboids[i][0]>=cuboids[j][0] and cuboids[i][1]>=cuboids[j][1] and cuboids[i][2]>=cuboids[j][2] and Lis[i]<=Lis[j]+cuboids[i][2]):
                    Lis[i]=Lis[j]+cuboids[i][2]
            maxLis = max(maxLis,Lis[i])
        return maxLis