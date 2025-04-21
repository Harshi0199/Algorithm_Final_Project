class Solution(object):
    def possibleToStamp(self, grid, stampHeight, stampWidth):
        """
        :type grid: List[List[int]]
        :type stampHeight: int
        :type stampWidth: int
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        # Step 1: Calculate prefix sum of the grid
        # This helps us quickly determine if a region has any obstacles
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                prefix_sum[i + 1][j + 1] = prefix_sum[i + 1][j] + prefix_sum[i][j + 1] - prefix_sum[i][j] + grid[i][j]
        
        # Step 2: Mark cells where we can place a stamp
        can_place = [[0] * n for _ in range(m)]
        for i in range(m - stampHeight + 1):
            for j in range(n - stampWidth + 1):
                # Calculate the sum of grid cells in the current stamp region
                region_sum = prefix_sum[i + stampHeight][j + stampWidth] - prefix_sum[i + stampHeight][j] - prefix_sum[i][j + stampWidth] + prefix_sum[i][j]
                
                # If region_sum is 0, it means there are no occupied cells in this region
                if region_sum == 0:
                    can_place[i][j] = 1
        
        # Step 3: Use another 2D prefix sum to track which cells can be covered
        coverage_prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                coverage_prefix[i + 1][j + 1] = coverage_prefix[i + 1][j] + coverage_prefix[i][j + 1] - coverage_prefix[i][j] + can_place[i][j]
        
        # Step 4: Check if all empty cells can be covered
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # If this is an empty cell
                    # Check if this cell can be covered by at least one stamp
                    # We check the region that ends at (i,j) and starts at (i-stampHeight+1, j-stampWidth+1), bounded by grid limits
                    start_i = max(0, i - stampHeight + 1)
                    start_j = max(0, j - stampWidth + 1)
                    
                    # Calculate how many stamps cover this cell
                    coverage = coverage_prefix[i + 1][j + 1] - coverage_prefix[i + 1][start_j] - coverage_prefix[start_i][j + 1] + coverage_prefix[start_i][start_j]
                    
                    # If coverage is 0, this empty cell cannot be covered
                    if coverage == 0:
                        return False
        
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