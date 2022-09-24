class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        one = False
        zeroes = 0
        res = 0
        for i in flowerbed:
            if i == 0:
                zeroes += 1
            else:
                if one == True:
                    if zeroes % 2 == 0:
                        res -= 1
                else:
                    one = True
                res += zeroes // 2
                zeroes = 0
                    
        if one == False and zeroes%2 == 1 :
            res += 1
        res += zeroes //2
        if res >= n:
            return True
        else:
            return False