rod_len = 4
length = [1,2,3,4]
price = [1,5,8,9]

dp = [[0 for i in range(rod_len + 1)] for j in range(len(length) + 1)]

for i in range(len(dp)):
    for j in range(len(dp[0])):

        if i == 0 or j == 0:
            continue

        exclude = dp[i-1][j]

        if length[i-1] > j:
            include = 0
        else:
            include = dp[i][j-length[i-1]] + price[i-1]

        dp[i][j] = max(include, exclude)

print(dp[-1][-1])