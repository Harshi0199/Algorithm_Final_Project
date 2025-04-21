# Problem 2600: K Items With the Maximum Sum
# Difficulty: Easy
# Description:
# <p>There is a bag that consists of items, each item&nbsp;has a number <code>1</code>, <code>0</code>, or <code>-1</code> written on it.</p>
# <p>You are given four <strong>non-negative </strong>integers <code>numOnes</code>, <code>numZeros</code>, <code>numNegOnes</code>, and <code>k</code>.</p>
# <p>The bag initially contains:</p>
# <ul>
# 	<li><code>numOnes</code> items with <code>1</code>s written on them.</li>
# 	<li><code>numZeroes</code> items with <code>0</code>s written on them.</li>
# 	<li><code>numNegOnes</code> items with <code>-1</code>s written on them.</li>
# </ul>
# <p>We want to pick exactly <code>k</code> items among the available items. Return <em>the <strong>maximum</strong> possible sum of numbers written on the items</em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 2 items with 1 written on them and get a sum in a total of 2.
# It can be proven that 2 is the maximum possible sum.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
# <strong>Output:</strong> 3
# <strong>Explanation:</strong> We have a bag of items with numbers written on them {1, 1, 1, 0, 0}. We take 3 items with 1 written on them, and 1 item with 0 written on it, and get a sum in a total of 3.
# It can be proven that 3 is the maximum possible sum.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>0 &lt;= numOnes, numZeros, numNegOnes &lt;= 50</code></li>
# 	<li><code>0 &lt;= k &lt;= numOnes + numZeros + numNegOnes</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # First pick as many 1s as possible
        pickOnes = min(numOnes, k)
        k -= pickOnes

        # Then pick 0s (they don't affect the sum)
        pickZeros = min(numZeros, k)
        k -= pickZeros

        # Then if any picks are left, they have to be -1s, which reduce the sum
        pickNegOnes = k  # only -1s left to pick

        return pickOnes - pickNegOnes

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.kItemsWithMaximumSum(8, 10, 8, 10) == 8
assert solution.kItemsWithMaximumSum(6, 3, 9, 15) == 0
assert solution.kItemsWithMaximumSum(3, 4, 5, 11) == -1
assert solution.kItemsWithMaximumSum(1, 4, 7, 3) == 1
assert solution.kItemsWithMaximumSum(9, 2, 6, 11) == 9
assert solution.kItemsWithMaximumSum(1, 3, 10, 3) == 1
assert solution.kItemsWithMaximumSum(6, 3, 3, 2) == 2
assert solution.kItemsWithMaximumSum(6, 10, 5, 2) == 2
assert solution.kItemsWithMaximumSum(7, 0, 5, 12) == 2
assert solution.kItemsWithMaximumSum(3, 6, 1, 3) == 3
assert solution.kItemsWithMaximumSum(8, 6, 5, 10) == 8
assert solution.kItemsWithMaximumSum(8, 1, 3, 4) == 4
assert solution.kItemsWithMaximumSum(5, 10, 7, 21) == -1
assert solution.kItemsWithMaximumSum(6, 3, 10, 15) == 0
assert solution.kItemsWithMaximumSum(8, 2, 5, 11) == 7
assert solution.kItemsWithMaximumSum(4, 10, 6, 19) == -1
assert solution.kItemsWithMaximumSum(9, 3, 8, 5) == 5
assert solution.kItemsWithMaximumSum(5, 2, 4, 9) == 3
assert solution.kItemsWithMaximumSum(10, 5, 5, 15) == 10
assert solution.kItemsWithMaximumSum(7, 3, 0, 8) == 7
assert solution.kItemsWithMaximumSum(7, 10, 10, 24) == 0
assert solution.kItemsWithMaximumSum(1, 0, 2, 0) == 0
assert solution.kItemsWithMaximumSum(9, 6, 5, 8) == 8
assert solution.kItemsWithMaximumSum(8, 10, 10, 8) == 8
assert solution.kItemsWithMaximumSum(0, 4, 6, 10) == -6
assert solution.kItemsWithMaximumSum(6, 0, 10, 5) == 5
assert solution.kItemsWithMaximumSum(2, 7, 6, 3) == 2
assert solution.kItemsWithMaximumSum(2, 1, 10, 3) == 2
assert solution.kItemsWithMaximumSum(4, 2, 6, 11) == -1
assert solution.kItemsWithMaximumSum(9, 5, 4, 10) == 9
assert solution.kItemsWithMaximumSum(10, 1, 3, 5) == 5
assert solution.kItemsWithMaximumSum(5, 3, 4, 2) == 2
assert solution.kItemsWithMaximumSum(9, 0, 3, 0) == 0
assert solution.kItemsWithMaximumSum(5, 3, 1, 3) == 3
assert solution.kItemsWithMaximumSum(4, 1, 7, 0) == 0
assert solution.kItemsWithMaximumSum(9, 6, 4, 7) == 7
assert solution.kItemsWithMaximumSum(1, 5, 10, 0) == 0
assert solution.kItemsWithMaximumSum(6, 4, 5, 14) == 2
assert solution.kItemsWithMaximumSum(10, 2, 1, 12) == 10
assert solution.kItemsWithMaximumSum(1, 8, 7, 11) == -1
assert solution.kItemsWithMaximumSum(2, 1, 5, 2) == 2
assert solution.kItemsWithMaximumSum(4, 4, 6, 3) == 3
assert solution.kItemsWithMaximumSum(5, 0, 2, 7) == 3
assert solution.kItemsWithMaximumSum(8, 9, 7, 13) == 8
assert solution.kItemsWithMaximumSum(2, 2, 7, 1) == 1
assert solution.kItemsWithMaximumSum(6, 8, 1, 4) == 4
assert solution.kItemsWithMaximumSum(0, 6, 0, 6) == 0
assert solution.kItemsWithMaximumSum(5, 5, 5, 4) == 4
assert solution.kItemsWithMaximumSum(5, 3, 5, 12) == 1
assert solution.kItemsWithMaximumSum(4, 2, 3, 8) == 2
assert solution.kItemsWithMaximumSum(9, 2, 4, 6) == 6
assert solution.kItemsWithMaximumSum(4, 5, 7, 5) == 4
assert solution.kItemsWithMaximumSum(1, 5, 7, 8) == -1
assert solution.kItemsWithMaximumSum(0, 4, 9, 6) == -2
assert solution.kItemsWithMaximumSum(0, 2, 7, 4) == -2
assert solution.kItemsWithMaximumSum(7, 2, 3, 8) == 7
assert solution.kItemsWithMaximumSum(4, 3, 7, 12) == -1
assert solution.kItemsWithMaximumSum(6, 1, 6, 5) == 5
assert solution.kItemsWithMaximumSum(9, 10, 1, 8) == 8
assert solution.kItemsWithMaximumSum(1, 4, 3, 7) == -1
assert solution.kItemsWithMaximumSum(8, 7, 3, 5) == 5
assert solution.kItemsWithMaximumSum(8, 10, 8, 15) == 8
assert solution.kItemsWithMaximumSum(5, 6, 5, 12) == 4
assert solution.kItemsWithMaximumSum(10, 4, 1, 5) == 5
assert solution.kItemsWithMaximumSum(10, 6, 2, 3) == 3
assert solution.kItemsWithMaximumSum(7, 0, 3, 8) == 6
assert solution.kItemsWithMaximumSum(1, 3, 7, 2) == 1
assert solution.kItemsWithMaximumSum(9, 9, 6, 13) == 9
assert solution.kItemsWithMaximumSum(3, 0, 7, 9) == -3
assert solution.kItemsWithMaximumSum(4, 0, 0, 3) == 3
assert solution.kItemsWithMaximumSum(9, 4, 8, 16) == 6
assert solution.kItemsWithMaximumSum(10, 5, 5, 13) == 10
assert solution.kItemsWithMaximumSum(9, 10, 10, 22) == 6
assert solution.kItemsWithMaximumSum(8, 0, 0, 0) == 0
assert solution.kItemsWithMaximumSum(5, 5, 4, 10) == 5
assert solution.kItemsWithMaximumSum(10, 8, 0, 9) == 9
assert solution.kItemsWithMaximumSum(7, 0, 6, 7) == 7
assert solution.kItemsWithMaximumSum(2, 6, 6, 5) == 2
assert solution.kItemsWithMaximumSum(3, 3, 4, 10) == -1
assert solution.kItemsWithMaximumSum(2, 10, 4, 6) == 2
assert solution.kItemsWithMaximumSum(5, 6, 3, 2) == 2
assert solution.kItemsWithMaximumSum(4, 10, 6, 5) == 4
assert solution.kItemsWithMaximumSum(10, 7, 2, 16) == 10
assert solution.kItemsWithMaximumSum(6, 9, 8, 0) == 0
assert solution.kItemsWithMaximumSum(6, 4, 4, 2) == 2
assert solution.kItemsWithMaximumSum(7, 3, 8, 11) == 6
assert solution.kItemsWithMaximumSum(2, 5, 5, 7) == 2
assert solution.kItemsWithMaximumSum(10, 3, 4, 13) == 10
assert solution.kItemsWithMaximumSum(7, 8, 6, 2) == 2
assert solution.kItemsWithMaximumSum(9, 1, 5, 5) == 5
assert solution.kItemsWithMaximumSum(1, 4, 5, 6) == 0
assert solution.kItemsWithMaximumSum(8, 1, 0, 5) == 5
assert solution.kItemsWithMaximumSum(9, 3, 9, 18) == 3
assert solution.kItemsWithMaximumSum(7, 9, 2, 5) == 5
assert solution.kItemsWithMaximumSum(0, 9, 8, 16) == -7
assert solution.kItemsWithMaximumSum(10, 3, 2, 2) == 2
assert solution.kItemsWithMaximumSum(7, 5, 10, 21) == -2
assert solution.kItemsWithMaximumSum(4, 6, 7, 10) == 4
assert solution.kItemsWithMaximumSum(4, 4, 6, 12) == 0
assert solution.kItemsWithMaximumSum(3, 0, 6, 5) == 1

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass