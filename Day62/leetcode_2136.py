class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        acc_plant = 0   # accumulated plant time on each step
        min_time = 0
        for grow, cur_plant in reversed(sorted(zip(growTime, plantTime))):
		    # print accumulated plant time and plant/growth time for current plant
            log_str = " " * acc_plant + "." * cur_plant + "^" * grow
			print(log_str)
            acc_plant += cur_plant
            min_time = max(min_time, len(log_str))

	    return min_time