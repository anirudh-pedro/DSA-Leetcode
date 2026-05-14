class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for i in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = matrix[i][j] + min(
                    dp[i+1][j],
                    dp[i+1][j+1] if j+1 <= n - 1 else float('inf'),
                    dp[i+1][j-1] if j-1 >= 0 else float('inf')
                )
        return min(dp[0])

