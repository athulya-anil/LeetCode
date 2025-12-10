# Last updated: 10/12/2025, 07:39:45
class Solution(object):
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            if c2 + 1 < n:
                diff[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                diff[r2 + 1][c2 + 1] += 1

        # prefix row
        for r in range(n):
            for c in range(1, n):
                diff[r][c] += diff[r][c - 1]

        # prefix col
        for c in range(n):
            for r in range(1, n):
                diff[r][c] += diff[r - 1][c]

        # build final n×n matrix
        return [row[:n] for row in diff[:n]]
