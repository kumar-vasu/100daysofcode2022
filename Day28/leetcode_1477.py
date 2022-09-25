class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        stack = deque([])
        tot = 0
        n = len(arr)
        dp = [math.inf]*(n+1)
        ans = math.inf
        for i in range(n):
            stack.append(arr[i])
            tot += arr[i]
            while tot > target:
                tot -= stack.popleft()
            if tot == target:
                l = len(stack)
                dp[i+1] = min(l,dp[i])
                ans = min(ans,l+dp[i-l+1])
            else:
                dp[i+1] = dp[i]




        return ans if ans!= math.inf else -1