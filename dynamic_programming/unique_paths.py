"""
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
https://leetcode.com/problems/unique-paths/
"""


class UniquePaths:

    def getUniquePaths(self, m, n) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = row[j] + newRow[j + 1]
            row = newRow

        return row[0]
