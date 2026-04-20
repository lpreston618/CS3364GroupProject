def knapsack(weights, values, W):
    n = len(weights)
    
    # Build DP table (n+1 rows, W+1 columns), initialized to 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill the table row by row
    for i in range(1, n + 1):
        wi = weights[i - 1]  # current item's weight
        vi = values[i - 1]   # current item's score
        for w in range(W + 1):
            if wi > w:
                # Item doesn't fit — skip it
                dp[i][w] = dp[i - 1][w]
            else:
                # Take the better of skipping or including
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - wi] + vi)
    
    # Backtrack to find which items were selected
    selected = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)  # item i was included
            w -= weights[i - 1]
    
    selected.reverse()
    return dp[n][W], selected

# Problem data
weights = [6, 4, 5, 3, 7]
values  = [1600, 1000, 1800, 1200, 2000]
W = 18

max_score, items = knapsack(weights, values, W)
print(f"Maximum Biodiversity Score: {max_score}")
print(f"Selected Items: {items}")