class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height)<=2:
            return 0
        
        left = 0
        water = 0
        right = len(height) - 1
        leftmost = height[0]
        rightmost = height[len(height) - 1]
        
        while left < right:
            
            if leftmost <= rightmost:
                
                water += leftmost - height[left]
                left += 1
                leftmost = max(leftmost, height[left])
                
            else:
                
                water += rightmost - height[right]
                right -= 1
                rightmost = max(rightmost, height[right])
                
        return water