def optimal_bst_cost(keys, freqs, n):

    dp = [[0 for _ in range(n)] for _ in range(n)]


    sum_freq = [[0 for _ in range(n)] for _ in range(n)]
    

    for i in range(n):
        sum_freq[i][i] = freqs[i]
        for j in range(i+1, n):
            sum_freq[i][j] = sum_freq[i][j-1] + freqs[j]


    for i in range(n):
        dp[i][i] = freqs[i]

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for r in range(i, j+1):
                cost = dp[i][r-1] + dp[r+1][j] if r > i and r < j else 0
                dp[i][j] = min(dp[i][j], cost + sum_freq[i][j])


    return dp[0][n-1]


keys = [5, 6]
freqs = [17, 25]
n = len(keys)

min_cost = optimal_bst_cost(keys, freqs, n)
print(f"Minimum cost of the optimal BST: {min_cost}")