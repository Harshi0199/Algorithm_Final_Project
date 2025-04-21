# Problem 1217: Minimum Cost to Move Chips to The Same Position
# Difficulty: Easy
# Description:
# <p>We have <code>n</code> chips, where the position of the <code>i<sup>th</sup></code> chip is <code>position[i]</code>.</p>
# <p>We need to move all the chips to <strong>the same position</strong>. In one step, we can change the position of the <code>i<sup>th</sup></code> chip from <code>position[i]</code> to:</p>
# <ul>
# 	<li><code>position[i] + 2</code> or <code>position[i] - 2</code> with <code>cost = 0</code>.</li>
# 	<li><code>position[i] + 1</code> or <code>position[i] - 1</code> with <code>cost = 1</code>.</li>
# </ul>
# <p>Return <em>the minimum cost</em> needed to move all the chips to the same position.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1217.Minimum%20Cost%20to%20Move%20Chips%20to%20The%20Same%20Position/images/chips_e1.jpg" style="width: 750px; height: 217px;" />
# <pre>
# <strong>Input:</strong> position = [1,2,3]
# <strong>Output:</strong> 1
# <strong>Explanation:</strong> First step: Move the chip at position 3 to position 1 with cost = 0.
# Second step: Move the chip at position 2 to position 1 with cost = 1.
# Total cost is 1.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/1200-1299/1217.Minimum%20Cost%20to%20Move%20Chips%20to%20The%20Same%20Position/images/chip_e2.jpg" style="width: 750px; height: 306px;" />
# <pre>
# <strong>Input:</strong> position = [2,2,2,3,3]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> We can move the two chips at position  3 to position 2. Each move has cost = 1. The total cost = 2.
# </pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre>
# <strong>Input:</strong> position = [1,1000000000]
# <strong>Output:</strong> 1
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= position.length &lt;= 100</code></li>
# 	<li><code>1 &lt;= position[i] &lt;= 10^9</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

from typing import *

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(1 for p in position if p % 2 == 0)
        odd = len(position) - even
        return min(even, odd)


# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.minCostToMoveChips([36, 19]) == 1
assert solution.minCostToMoveChips([11, 61, 20]) == 1
assert solution.minCostToMoveChips([38, 53, 50, 31, 75, 22, 74, 25, 71]) == 4
assert solution.minCostToMoveChips([18, 70, 31, 78, 23, 13, 29, 7]) == 3
assert solution.minCostToMoveChips([5, 87, 39]) == 0
assert solution.minCostToMoveChips([92, 32, 66, 9, 18, 10, 62, 55, 3, 22]) == 3
assert solution.minCostToMoveChips([80]) == 0
assert solution.minCostToMoveChips([7, 40, 92, 86, 45]) == 2
assert solution.minCostToMoveChips([51, 1, 59, 90]) == 1
assert solution.minCostToMoveChips([69, 88, 68, 16, 78, 83, 12, 13, 96, 57]) == 4
assert solution.minCostToMoveChips([42, 41, 55, 59]) == 1
assert solution.minCostToMoveChips([56]) == 0
assert solution.minCostToMoveChips([48, 74, 70, 69]) == 1
assert solution.minCostToMoveChips([8, 22, 70, 68]) == 0
assert solution.minCostToMoveChips([4, 41, 88, 22]) == 1
assert solution.minCostToMoveChips([60, 81, 54, 65, 31, 16, 93, 32]) == 4
assert solution.minCostToMoveChips([26, 60, 75, 62, 89, 96, 78, 80, 54, 5]) == 3
assert solution.minCostToMoveChips([1]) == 0
assert solution.minCostToMoveChips([40, 91, 90, 17]) == 2
assert solution.minCostToMoveChips([5, 79, 3, 90, 29, 1, 72, 7, 31, 58]) == 3
assert solution.minCostToMoveChips([89, 2, 75]) == 1
assert solution.minCostToMoveChips([30, 62, 19, 83, 29, 17, 22]) == 3
assert solution.minCostToMoveChips([74, 47, 33, 8, 77, 87, 32]) == 3
assert solution.minCostToMoveChips([91, 92, 16, 89, 39, 52, 37, 82, 46, 41]) == 5
assert solution.minCostToMoveChips([79, 69, 31, 77, 38]) == 1
assert solution.minCostToMoveChips([7, 42, 35, 68, 37, 61, 19, 12]) == 3
assert solution.minCostToMoveChips([10, 75, 7, 26, 78, 80, 61]) == 3
assert solution.minCostToMoveChips([29, 26, 92, 20]) == 1
assert solution.minCostToMoveChips([59, 29, 73, 60, 8, 50, 14]) == 3
assert solution.minCostToMoveChips([24, 44, 70, 42]) == 0
assert solution.minCostToMoveChips([38, 83]) == 1
assert solution.minCostToMoveChips([21, 33, 50, 100, 94, 37, 99]) == 3
assert solution.minCostToMoveChips([77, 6, 98, 73, 33, 8, 20, 70, 9, 34]) == 4
assert solution.minCostToMoveChips([56, 4, 52, 21, 22, 91, 35, 75, 25]) == 4
assert solution.minCostToMoveChips([4, 89, 23, 5, 83]) == 1
assert solution.minCostToMoveChips([33, 97, 60, 10, 71]) == 2
assert solution.minCostToMoveChips([47, 73, 53, 54, 34, 65, 11, 92, 26, 28]) == 5
assert solution.minCostToMoveChips([55, 97, 70, 52, 14, 67, 54, 12, 10, 82]) == 3
assert solution.minCostToMoveChips([97, 9, 1, 86, 98]) == 2
assert solution.minCostToMoveChips([65]) == 0
assert solution.minCostToMoveChips([86, 26, 97, 95, 58, 84]) == 2
assert solution.minCostToMoveChips([9, 45, 47, 36, 8, 53, 72, 2, 31]) == 4
assert solution.minCostToMoveChips([93, 47, 36, 75]) == 1
assert solution.minCostToMoveChips([94, 61]) == 1
assert solution.minCostToMoveChips([18, 5, 82, 58, 37]) == 2
assert solution.minCostToMoveChips([98]) == 0
assert solution.minCostToMoveChips([58, 44, 88, 92, 18, 15, 80, 91]) == 2
assert solution.minCostToMoveChips([68, 30, 66, 44, 9]) == 1
assert solution.minCostToMoveChips([83, 2, 38]) == 1
assert solution.minCostToMoveChips([12, 9, 63, 34, 48, 86, 74, 72, 67]) == 3
assert solution.minCostToMoveChips([93, 62, 34]) == 1
assert solution.minCostToMoveChips([90, 95, 78, 49, 68, 96]) == 2
assert solution.minCostToMoveChips([44]) == 0
assert solution.minCostToMoveChips([25, 66, 79, 6, 49, 55, 31, 88, 91, 20]) == 4
assert solution.minCostToMoveChips([44, 72, 97]) == 1
assert solution.minCostToMoveChips([97, 35, 77, 39, 65, 41, 63, 29, 87, 20]) == 1
assert solution.minCostToMoveChips([23, 50, 46, 25, 32, 52, 98, 61, 4, 17]) == 4
assert solution.minCostToMoveChips([67, 48, 60, 13]) == 2
assert solution.minCostToMoveChips([62, 13, 29, 34]) == 2
assert solution.minCostToMoveChips([21, 79, 77, 57, 98, 82, 65, 86, 53]) == 3
assert solution.minCostToMoveChips([50, 47, 63]) == 1
assert solution.minCostToMoveChips([50, 69, 3, 100, 2]) == 2
assert solution.minCostToMoveChips([15, 95, 18, 13, 30, 61, 73, 91]) == 2
assert solution.minCostToMoveChips([57, 7, 91, 56]) == 1
assert solution.minCostToMoveChips([49, 14, 70, 35, 56, 59, 32, 3, 16, 34]) == 4
assert solution.minCostToMoveChips([57, 70]) == 1
assert solution.minCostToMoveChips([89, 74, 24, 12, 53]) == 2
assert solution.minCostToMoveChips([88, 35, 29, 16, 8, 76, 44]) == 2
assert solution.minCostToMoveChips([1, 37, 99, 10, 72, 4]) == 3
assert solution.minCostToMoveChips([50, 38, 24, 33, 100, 5]) == 2
assert solution.minCostToMoveChips([57, 23]) == 0
assert solution.minCostToMoveChips([58, 34, 23, 97]) == 2
assert solution.minCostToMoveChips([94, 73, 12, 64, 97, 42, 71, 63, 96, 58]) == 4
assert solution.minCostToMoveChips([1, 37, 92, 52, 34, 53, 41, 69, 59, 55]) == 3
assert solution.minCostToMoveChips([51]) == 0
assert solution.minCostToMoveChips([15, 46, 49, 96, 61, 57, 86, 12, 76, 83]) == 5
assert solution.minCostToMoveChips([100, 79, 83, 13]) == 1
assert solution.minCostToMoveChips([28, 87, 56, 62, 64, 69, 55]) == 3
assert solution.minCostToMoveChips([41, 11, 91, 6, 62]) == 2
assert solution.minCostToMoveChips([74, 56, 26, 75, 54, 31, 79, 60]) == 3
assert solution.minCostToMoveChips([83, 45, 6, 52]) == 2
assert solution.minCostToMoveChips([52, 89, 81]) == 1
assert solution.minCostToMoveChips([51, 40, 89, 15, 62]) == 2
assert solution.minCostToMoveChips([72]) == 0
assert solution.minCostToMoveChips([4, 89, 75, 79, 48, 77, 1, 100, 19, 3]) == 3
assert solution.minCostToMoveChips([86, 71, 84, 9, 5, 26]) == 3
assert solution.minCostToMoveChips([32]) == 0
assert solution.minCostToMoveChips([97]) == 0
assert solution.minCostToMoveChips([47, 28, 16, 12, 7, 56, 9, 15, 37, 20]) == 5
assert solution.minCostToMoveChips([22]) == 0
assert solution.minCostToMoveChips([36]) == 0
assert solution.minCostToMoveChips([55, 60, 78]) == 1
assert solution.minCostToMoveChips([56, 23, 34]) == 1
assert solution.minCostToMoveChips([78]) == 0
assert solution.minCostToMoveChips([87, 91]) == 0
assert solution.minCostToMoveChips([36, 43]) == 1
assert solution.minCostToMoveChips([33, 63, 34]) == 1
assert solution.minCostToMoveChips([83, 97, 85, 43]) == 0
assert solution.minCostToMoveChips([11, 23, 88, 36, 30]) == 2
assert solution.minCostToMoveChips([20, 13, 30]) == 1

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass