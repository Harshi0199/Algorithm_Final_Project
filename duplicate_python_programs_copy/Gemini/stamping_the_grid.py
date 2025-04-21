import itertools

class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool

        Determines if it's possible to cover all empty cells (0) in the grid
        with stamps of given dimensions without covering occupied cells (1).
        """
        m = len(grid)
        n = len(grid[0])

        # 1. Calculate Prefix Sums of the Grid
        # prefix_sum[r+1][c+1] will store the sum of grid[0..r][0..c]
        # This allows O(1) query for the sum of any rectangle.
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                prefix_sum[r + 1][c + 1] = grid[r][c] + prefix_sum[r][c + 1] + prefix_sum[r + 1][c] - prefix_sum[r][c]

        # Helper function to get the sum of a rectangle using prefix sums
        def get_rect_sum(r1, c1, r2, c2):
            # Calculates sum of grid[r1..r2][c1..c2] (inclusive)
            if r1 > r2 or c1 > c2:
                return 0 # Or handle appropriately if needed, though shouldn't happen with valid checks
            return prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]

        # 2. Determine where stamps *can* be placed
        # possible_stamps[r][c] = 1 if a stamp can start with top-left at (r, c), else 0
        possible_stamps = [[0] * n for _ in range(m)]
        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                # Check if the stamp area contains any occupied cells (1s)
                if get_rect_sum(r, c, r + stampHeight - 1, c + stampWidth - 1) == 0:
                    possible_stamps[r][c] = 1

        # 3. Calculate Coverage using 2D Difference Array / Prefix Sum technique
        # This efficiently determines which cells are covered by *at least one* possible stamp.
        # diff[r][c] helps compute the final coverage count.
        diff = [[0] * (n + 1) for _ in range(m + 1)] # Use m+1, n+1 for boundary handling

        for r in range(m - stampHeight + 1):
            for c in range(n - stampWidth + 1):
                if possible_stamps[r][c] == 1:
                    # Increment the top-left corner of the stamp area
                    diff[r][c] += 1
                    # Decrement the corner just outside the stamp area (right)
                    diff[r][c + stampWidth] -= 1
                    # Decrement the corner just outside the stamp area (bottom)
                    diff[r + stampHeight][c] -= 1
                    # Increment the corner diagonally outside (bottom-right) to correct double decrement
                    diff[r + stampHeight][c + stampWidth] += 1

        # Calculate the actual coverage count for each cell by computing prefix sums on the diff array
        # coverage[r][c] will store how many valid stamps cover cell (r,c)
        coverage = [[0] * n for _ in range(m)]
        current_row_sum = [[0] * (n + 1) for _ in range(m + 1)] # Temporary store for row prefix sums
        for r in range(m):
             for c in range(n):
                # Update based on diff array value and values from top and left
                current_row_sum[r+1][c+1] = diff[r][c] + current_row_sum[r+1][c]

        for c in range(n):
            for r in range(m):
                 # final prefix sum for coverage count
                 coverage[r][c] = current_row_sum[r+1][c+1] + (coverage[r-1][c] if r > 0 else 0)


        # 4. Final Check: Verify all empty cells are covered
        for r in range(m):
            for c in range(n):
                # If a cell is empty (0) but is not covered by any possible stamp
                if grid[r][c] == 0 and coverage[r][c] == 0:
                    return False # This empty cell cannot be stamped

        # If we reach here, all empty cells are coverable
        return True

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.possibleToStamp([[1, 1, 1, 0, 0, 1], [0, 1, 0, 1, 1, 1]], 2, 1) == False
assert solution.possibleToStamp([[0, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [1, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 1], [0, 0, 1, 1], [0, 1, 0, 1]], 4, 1) == False
assert solution.possibleToStamp([[1, 1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 1, 0, 1, 1, 0]], 3, 5) == False
assert solution.possibleToStamp([[1, 0, 1, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1, 0, 0]], 8, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 0, 1, 1, 1]], 5, 2) == False
assert solution.possibleToStamp([[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]], 2, 4) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 1, 0, 0, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0, 0, 0]], 1, 6) == False
assert solution.possibleToStamp([[1, 0, 1, 0, 1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1]], 1, 10) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 1, 0, 1, 0, 1], [1, 1, 0, 0, 1, 1, 0, 1, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 0, 1]], 2, 5) == False
assert solution.possibleToStamp([[0, 0, 0, 0], [1, 0, 1, 0]], 2, 1) == False
assert solution.possibleToStamp([[1, 1, 0], [0, 0, 0], [1, 0, 1], [0, 0, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1], [1, 0, 0]], 8, 2) == False
assert solution.possibleToStamp([[0, 0, 1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 1, 0, 1, 1]], 1, 3) == False
assert solution.possibleToStamp([[0, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 1, 0, 0, 0]], 2, 1) == False
assert solution.possibleToStamp([[0, 1, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 0, 1, 0, 0]], 4, 3) == False
assert solution.possibleToStamp([[1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 1, 0]], 6, 1) == False
assert solution.possibleToStamp([[0, 0], [0, 0], [0, 0], [0, 0], [0, 1]], 5, 1) == False
assert solution.possibleToStamp([[0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 1, 1], [1, 1, 1], [0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 1]], 5, 2) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1]], 1, 4) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 1, 1, 0, 1, 0, 0], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 1, 1, 0, 0, 1], [0, 1, 1, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1, 0, 1], [0, 1, 1, 1, 1, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0, 0, 1, 0, 1]], 7, 1) == False
assert solution.possibleToStamp([[0, 1, 1, 0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1], [0, 1, 1, 1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1, 1]], 8, 1) == False
assert solution.possibleToStamp([[0, 0, 1, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 1, 0]], 4, 9) == False
assert solution.possibleToStamp([[0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 1, 1]], 4, 7) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 1], [1, 0, 1, 1, 1], [0, 0, 1, 0, 0]], 1, 5) == False
assert solution.possibleToStamp([[0, 1, 0], [0, 0, 0]], 1, 1) == True
assert solution.possibleToStamp([[1, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1]], 1, 2) == False
assert solution.possibleToStamp([[0, 0, 1], [1, 0, 1], [1, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0], [0, 1, 1], [1, 0, 0], [0, 1, 1]], 2, 1) == False
assert solution.possibleToStamp([[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 2, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 1, 1, 1, 0, 1, 1, 0], [0, 0, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]], 7, 9) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1]], 3, 2) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 0, 1, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 1], [1, 0, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 0, 0]], 5, 2) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0]], 2, 4) == False
assert solution.possibleToStamp([[1, 1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 1]], 3, 5) == False
assert solution.possibleToStamp([[0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1, 0]], 2, 7) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1, 1], [0, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 1, 0], [0, 1, 1, 1, 0, 1, 1]], 4, 6) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1, 0, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]], 2, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 1, 0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0]], 9, 3) == False
assert solution.possibleToStamp([[0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1, 1, 0]], 1, 8) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 1, 0, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0, 0], [1, 1, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 1, 0, 0, 1, 1, 0, 0]], 1, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1], [0, 1, 1, 1, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [0, 0, 0, 1, 0]], 4, 5) == False
assert solution.possibleToStamp([[0, 1, 1], [1, 0, 1], [1, 0, 0], [0, 0, 0], [0, 1, 1]], 5, 3) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 1, 1], [1, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1], [0, 1, 0, 0, 1, 1]], 3, 4) == False
assert solution.possibleToStamp([[1, 0, 0, 1, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1, 0, 0, 1]], 6, 8) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 1]], 4, 2) == False
assert solution.possibleToStamp([[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1]], 2, 7) == False
assert solution.possibleToStamp([[0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1]], 4, 2) == False
assert solution.possibleToStamp([[1, 0], [1, 0]], 1, 2) == False
assert solution.possibleToStamp([[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [1, 0, 1, 1, 0], [0, 0, 1, 1, 0], [0, 1, 0, 1, 0], [0, 1, 1, 0, 0], [1, 1, 0, 1, 0], [0, 0, 1, 1, 0], [0, 0, 1, 1, 0], [1, 1, 1, 0, 1]], 10, 5) == False
assert solution.possibleToStamp([[1, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 1], [1, 0, 0, 1], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]], 1, 1) == True
assert solution.possibleToStamp([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 1]], 1, 2) == False
assert solution.possibleToStamp([[1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0], [0, 1, 0, 1]], 5, 2) == False
assert solution.possibleToStamp([[1, 1, 0], [0, 1, 0], [1, 0, 1], [1, 1, 0], [1, 1, 0], [0, 1, 0], [1, 1, 1]], 2, 2) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1, 1, 1]], 1, 8) == False
assert solution.possibleToStamp([[1, 0, 1, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0, 0]], 5, 5) == False
assert solution.possibleToStamp([[1, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 1, 1, 0, 1], [1, 1, 1, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0, 1]], 1, 4) == False
assert solution.possibleToStamp([[0, 0, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0]], 3, 2) == False
assert solution.possibleToStamp([[0, 0, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0]], 1, 4) == False
assert solution.possibleToStamp([[1, 1], [1, 0], [1, 0], [1, 0], [1, 0]], 4, 2) == False
assert solution.possibleToStamp([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1]], 3, 8) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0, 1, 1]], 2, 4) == False
assert solution.possibleToStamp([[0, 1, 0, 1, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1, 1]], 3, 9) == False
assert solution.possibleToStamp([[1, 0, 0, 1, 0], [1, 1, 0, 1, 0]], 1, 1) == True
assert solution.possibleToStamp([[0, 0, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0, 1]], 8, 5) == False
assert solution.possibleToStamp([[0, 0, 0, 1, 0, 1, 1, 1, 0, 0], [1, 1, 1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0, 1, 1, 0, 0], [1, 1, 0, 1, 1, 1, 1, 0, 0, 0]], 4, 5) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0, 1], [0, 0, 0, 1, 1, 0, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 1, 0, 0, 1]], 1, 10) == False
assert solution.possibleToStamp([[0, 1, 1, 0, 1], [0, 1, 1, 1, 1], [1, 1, 0, 0, 0]], 2, 2) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1]], 2, 3) == False
assert solution.possibleToStamp([[1, 0, 0, 1, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1]], 2, 7) == False
assert solution.possibleToStamp([[1, 1, 1], [1, 0, 0], [0, 1, 1]], 1, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 1, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 1, 0, 0, 0], [1, 0, 1, 1, 0, 1, 1, 0, 0, 1], [0, 0, 0, 1, 0, 1, 1, 0, 0, 1]], 2, 4) == False
assert solution.possibleToStamp([[1, 1], [1, 0], [1, 1], [1, 0], [1, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0]], 9, 2) == False
assert solution.possibleToStamp([[1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 1, 0], [0, 1, 1, 0, 1]], 2, 4) == False
assert solution.possibleToStamp([[1, 1], [0, 1], [0, 1], [0, 0]], 1, 1) == True
assert solution.possibleToStamp([[1, 0, 1, 0, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 0, 1], [1, 0, 1, 1, 0], [1, 0, 1, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [1, 1, 0, 0, 0]], 8, 4) == False
assert solution.possibleToStamp([[0, 1, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0], [1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0]], 2, 5) == False
assert solution.possibleToStamp([[1, 1], [1, 0], [0, 0], [0, 1], [0, 1], [0, 0], [0, 0], [1, 1], [1, 1], [0, 0]], 7, 2) == False
assert solution.possibleToStamp([[1, 1, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1]], 4, 4) == False
assert solution.possibleToStamp([[0, 1, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1]], 3, 3) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1]], 1, 5) == False
assert solution.possibleToStamp([[0, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 0]], 1, 5) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 1, 0, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 1, 1, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 0]], 1, 2) == False
assert solution.possibleToStamp([[0, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0], [0, 1, 1, 0, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0]], 1, 7) == False
assert solution.possibleToStamp([[0, 1, 0, 1, 1], [1, 0, 0, 1, 1], [0, 1, 0, 1, 1]], 2, 3) == False
assert solution.possibleToStamp([[0, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [1, 0, 0], [1, 0, 0]], 3, 1) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0]], 3, 7) == False
assert solution.possibleToStamp([[1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 1, 0, 1, 0], [1, 0, 0, 1, 0], [1, 1, 0, 0, 0], [1, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 1, 1, 1, 0]], 4, 3) == False
assert solution.possibleToStamp([[1, 1, 0, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0], [1, 0, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 0, 1, 0]], 7, 2) == False
assert solution.possibleToStamp([[0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0]], 5, 2) == False
assert solution.possibleToStamp([[1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 0, 1]], 7, 6) == False
assert solution.possibleToStamp([[1, 0], [1, 1], [0, 0], [1, 1], [1, 1], [0, 0], [1, 1], [0, 1], [1, 1]], 2, 2) == False
assert solution.possibleToStamp([[0, 0, 0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 1, 1, 1, 0]], 1, 7) == False
assert solution.possibleToStamp([[1, 0, 0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1]], 3, 8) == False
assert solution.possibleToStamp([[0, 0, 1, 0, 0, 0, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 1]], 5, 2) == False
assert solution.possibleToStamp([[0, 1, 0, 1, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 0, 1], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1, 0, 0]], 9, 7) == False
assert solution.possibleToStamp([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0]], 2, 3) == False
assert solution.possibleToStamp([[0, 1, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1]], 2, 7) == False
assert solution.possibleToStamp([[0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 1, 0, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 0]], 2, 3) == False
assert solution.possibleToStamp([[0, 1, 1, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 0, 0]], 2, 6) == False
assert solution.possibleToStamp([[0, 1, 1, 1], [0, 0, 1, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 1, 2) == False
assert solution.possibleToStamp([[0, 1, 1], [0, 0, 1], [0, 0, 1], [1, 1, 1], [1, 0, 1]], 5, 3) == False
assert solution.possibleToStamp([[1, 1, 0], [1, 0, 1], [0, 0, 0]], 3, 1) == False
