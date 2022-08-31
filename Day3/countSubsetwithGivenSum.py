def count_subset():
    nums = [1,2,1]
    sum = 3

    dp = [[0 if i !=0 else 1 for i in range(sum + 1)] for j in range(len(nums) + 1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if j == 0 or i == 0:
                continue
            exclude = dp[i-1][j]
            if nums[i-1] > j:
                include = 0
            else:
                include = dp[i-1][j-nums[i-1]]
            dp[i][j] = exclude + include

    return(dp[-1][-1])

print(count_subset())
