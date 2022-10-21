class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        stack = []
        map_ = {}
        for i in nums:
            if len(stack) == k+1:
                map_[stack[0]] -= 1
                if map_[stack[0]] == 0:
                    map_.pop(stack[0])
                stack.pop(0)
            
            if i in map_:
                return True
            else:
                stack.append(i)
                if i in map_:
                    map_[i] += 1
                else:
                    map_[i] = 1
        return False