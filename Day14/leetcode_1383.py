class Solution:
    
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        engineers = [[speed[i], efficiency[i]] for i in range(n)]
        
        engineers = sorted(engineers, key = lambda x : [-x[1],-x[0]])
        
        speed_queue = []
        speed_sum = 0
        curr_performance = 0
        
        for i in range(n):
            speed_queue = sorted(speed_queue)
            
            speed_queue.append(engineers[i][0])
            if len(speed_queue) > k:
                sub = speed_queue.pop(0)
                speed_sum -= sub
            speed_sum += engineers[i][0]
            
            curr_performance = max(curr_performance, speed_sum*engineers[i][1])
        return curr_performance % 1000000007