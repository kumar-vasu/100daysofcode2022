class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        for i in range(k):
            if queue != []:
                while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                    queue.pop(-1)
            queue.append(i)
        maximum = [nums[queue[0]]]
        left = 0
        
        for i in range(k, len(nums)):
            while len(queue) > 0 and queue[0] <= left:
                queue.pop(0)
            if queue != []:
                while len(queue) > 0 and nums[queue[-1]] < nums[i]:
                    queue.pop(-1)
            queue.append(i)
            left += 1
            maximum.append(nums[queue[0]])
            
        return maximum
        
        