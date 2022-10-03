class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        max_num = 0
        cur_sum = 0
        pre_color = ''
        ans = 0
        
        for color, num in zip(colors, neededTime):
            if color == pre_color:
                max_num = max(max_num, num)
                cur_sum += num
            
            else:
                ans += cur_sum - max_num
                max_num = num
                cur_sum = num
                pre_color = color
        
        ans += cur_sum - max_num
    
        return ans