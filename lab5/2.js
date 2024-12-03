function knapsack(weights, values, W) {
  const n = weights.length;
  let dp = Array(W + 1).fill(0);

  for (let i = 0; i < n; i++) {
    for (let w = W; w >= weights[i]; w--) {
      dp[w] = Math.max(dp[w], dp[w - weights[i]] + values[i]);
    }
  }

  return dp[W];
}

// Test with sample data
let weights = [2, 3, 4, 5];
let values = [3, 4, 5, 6];
let capacity = 5;
console.log("Maximum value in Knapsack:", knapsack(weights, values, capacity)); // Output: 7
