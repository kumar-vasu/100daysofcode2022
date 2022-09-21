class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = []
        
        sum_even = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                sum_even += nums[i] 
                
        for i in range(len(queries)):
            #print(nums, sum_even)
            if queries[i][0] % 2 == 0:
                if nums[queries[i][1]] % 2 == 0:
                    nums[queries[i][1]] += queries[i][0] 
                    sum_even += queries[i][0]
                    answer.append(sum_even)
                else:
                    nums[queries[i][1]] += queries[i][0] 
                    answer.append(sum_even)
            else:
                if nums[queries[i][1]] % 2 != 0:
                    nums[queries[i][1]] += queries[i][0] 
                    sum_even += nums[queries[i][1]]
                    answer.append(sum_even)
                else:
                    sum_even -= nums[queries[i][1]]
                    nums[queries[i][1]] += queries[i][0] 
                    answer.append(sum_even)
            #print(nums, sum_even)
        return answer