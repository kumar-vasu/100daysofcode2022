class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff =  target - sum(nums[:3])
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                sums = nums[i] + nums[left] + nums[right]
                if abs(target - sums) < abs(diff):
                    diff = target - sums
                elif sums < target:
                    left += 1
                elif sums > target:
                    right -= 1
                else:
                    return sums
        return target - diff