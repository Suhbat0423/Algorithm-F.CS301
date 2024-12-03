import unittest

def coinChange(coins, amount):
    memo = {}

    def dp(x):
        if x in memo:
            return memo[x]
        if x == 0:
            return 0
        if x < 0:
            return float('inf')

        res = float('inf')
        for coin in coins:
            res = min(res, dp(x - coin) + 1)

        memo[x] = res
        return res

    result = dp(amount)
    return result if result != float('inf') else -1

class TestCoinChange(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)

    def test_case_2(self):
        self.assertEqual(coinChange([2], 3), -1)

if __name__ == '__main__':
    unittest.main()
