class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        queue = []
        for i in range(1,10):
            if i + k < 10 or i - k >= 0:
                queue.append([str(i)])
                
        curr_len = 1
        
        while curr_len < n:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr = queue.pop(0)
                
                if int(curr[-1]) + k < 10:
                    queue.append(curr+[str(int(curr[-1]) + k)])
                if int(curr[-1]) - k >= 0:
                    queue.append(curr+[str(int(curr[-1]) - k)])
            curr_len += 1
            
        result = list(set([int("".join(i)) for i in queue]))
        
        return result