# Problem 2170: Minimum Operations to Make the Array Alternating
# Difficulty: Medium
# Description:
# <p>You are given a <strong>0-indexed</strong> array <code>nums</code> consisting of <code>n</code> positive integers.</p>
# <p>The array <code>nums</code> is called <strong>alternating</strong> if:</p>
# <ul>
# 	<li><code>nums[i - 2] == nums[i]</code>, where <code>2 &lt;= i &lt;= n - 1</code>.</li>
# 	<li><code>nums[i - 1] != nums[i]</code>, where <code>1 &lt;= i &lt;= n - 1</code>.</li>
# </ul>
# <p>In one <strong>operation</strong>, you can choose an index <code>i</code> and <strong>change</strong> <code>nums[i]</code> into <strong>any</strong> positive integer.</p>
# <p>Return <em>the <strong>minimum number of operations</strong> required to make the array alternating</em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [3,1,3,2,4,3]
# <strong>Output:</strong> 3
# <strong>Explanation:</strong>
# One way to make the array alternating is by converting it to [3,1,3,<u><strong>1</strong></u>,<u><strong>3</strong></u>,<u><strong>1</strong></u>].
# The number of operations required in this case is 3.
# It can be proven that it is not possible to make the array alternating in less than 3 operations. 
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [1,2,2,2,2]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong>
# One way to make the array alternating is by converting it to [1,2,<u><strong>1</strong></u>,2,<u><strong>1</strong></u>].
# The number of operations required in this case is 2.
# Note that the array cannot be converted to [<u><strong>2</strong></u>,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from collections import Counter

from collections import Counter


class Solution:
    def minimumOperations(self, nums):
        # Split the list into even and odd indexed numbers.
        even = nums[0::2]
        odd = nums[1::2]

        # Count the frequency of each number in even and odd indices.
        even_counter = Counter(even)
        odd_counter = Counter(odd)

        # Get the two most common numbers for both even and odd groups.
        even_common = even_counter.most_common(2)
        odd_common = odd_counter.most_common(2)

        # If there is only one candidate in either group, add a dummy candidate with frequency 0.
        if len(even_common) < 2:
            even_common.append((None, 0))
        if len(odd_common) < 2:
            odd_common.append((None, 0))

        # If the top candidates for even and odd groups differ, we can use them directly.
        if even_common[0][0] != odd_common[0][0]:
            changes = (len(even) - even_common[0][1]) + (len(odd) - odd_common[0][1])
        else:
            # If the top candidates are the same, try both alternatives by replacing one group
            changes_option1 = (len(even) - even_common[0][1]) + (len(odd) - odd_common[1][1])
            changes_option2 = (len(even) - even_common[1][1]) + (len(odd) - odd_common[0][1])
            changes = min(changes_option1, changes_option2)

        return changes


# Test Cases:
solution = Solution()
assert solution.minimumOperations([19, 61, 82]) == 1
assert solution.minimumOperations([84, 10, 52, 5, 21, 98, 59, 73]) == 6
assert solution.minimumOperations([44, 4, 41, 73]) == 2
assert solution.minimumOperations([63, 76, 31]) == 1
assert solution.minimumOperations([90, 98, 66, 69, 41, 100, 72]) == 5
assert solution.minimumOperations([50, 76, 93]) == 1
assert solution.minimumOperations([71, 94, 100, 84, 46, 51]) == 4
assert solution.minimumOperations([23, 12, 94, 49, 13, 55, 52, 87, 79]) == 7
assert solution.minimumOperations([14, 18, 90, 59, 73, 50, 21, 24, 54, 85]) == 8
assert solution.minimumOperations([46, 6, 52, 58, 53, 81]) == 4
assert solution.minimumOperations([55, 46, 11]) == 1
assert solution.minimumOperations([80, 27, 26, 57, 7, 14, 67, 20, 87, 77]) == 8
assert solution.minimumOperations([13, 45, 51]) == 1
assert solution.minimumOperations([95, 49, 81, 39, 42, 34, 23, 21, 65, 58]) == 8
assert solution.minimumOperations([30, 62, 94, 13, 10, 68, 63, 96, 23]) == 7
assert solution.minimumOperations([48, 51, 64, 40, 86, 62, 22]) == 5
assert solution.minimumOperations([68, 18, 11, 39, 61, 34]) == 4
assert solution.minimumOperations([79, 29, 9, 67, 72, 85]) == 4
assert solution.minimumOperations([91, 63]) == 0
assert solution.minimumOperations([43, 76, 100, 40, 87]) == 3
assert solution.minimumOperations([51, 70, 58, 57, 48]) == 3
assert solution.minimumOperations([78, 11, 49, 75]) == 2
assert solution.minimumOperations([97, 2]) == 0
assert solution.minimumOperations([6, 20, 88]) == 1
assert solution.minimumOperations([85, 64]) == 0
assert solution.minimumOperations([92, 88, 26, 87, 40]) == 3
assert solution.minimumOperations([1, 62, 83, 97, 44, 39]) == 4
assert solution.minimumOperations([27, 39, 35, 10, 85, 79, 61, 49]) == 6
assert solution.minimumOperations([54, 8, 93, 98, 47]) == 3
assert solution.minimumOperations([52, 75, 11, 57, 10, 93, 42, 43, 53, 21]) == 8
assert solution.minimumOperations([13, 29, 8, 91, 22, 6, 67, 58, 43]) == 7
assert solution.minimumOperations([84, 8, 13, 54, 43, 96, 46, 75, 9, 74]) == 8
assert solution.minimumOperations([16, 41, 35]) == 1
assert solution.minimumOperations([76, 15]) == 0
assert solution.minimumOperations([65, 55, 31, 50, 96, 24, 21, 14, 58, 40]) == 8
assert solution.minimumOperations([50, 45, 94, 38, 97, 99, 23, 39, 75, 20]) == 8
assert solution.minimumOperations([34, 22, 93, 37, 62, 51]) == 4
assert solution.minimumOperations([13, 52, 75, 17, 85, 54, 71, 60]) == 6
assert solution.minimumOperations([44, 58, 8, 46, 10, 41, 70, 78, 98]) == 7
assert solution.minimumOperations([77, 18, 36]) == 1
assert solution.minimumOperations([60, 44, 48]) == 1
assert solution.minimumOperations([18, 98, 47, 11, 60, 31]) == 4
assert solution.minimumOperations([9, 39, 26, 15]) == 2
assert solution.minimumOperations([32, 25, 82, 39, 68, 58, 21, 63]) == 6
assert solution.minimumOperations([73, 4]) == 0
assert solution.minimumOperations([42, 95, 21, 78, 68, 57, 11, 43]) == 6
assert solution.minimumOperations([79, 86, 71, 73, 34, 72, 85, 22]) == 6
assert solution.minimumOperations([23, 33, 63, 90, 36, 22, 16, 1, 53]) == 7
assert solution.minimumOperations([40, 97, 15, 14, 32, 87, 37, 7, 77, 45]) == 8
assert solution.minimumOperations([22, 69, 38, 81, 84]) == 3
assert solution.minimumOperations([63, 8, 10, 19]) == 2
assert solution.minimumOperations([18, 33]) == 0
assert solution.minimumOperations([34, 79, 84, 58, 29, 66, 40]) == 5
assert solution.minimumOperations([96, 46]) == 0
assert solution.minimumOperations([30, 80, 26, 51, 8, 66, 69, 53]) == 6
assert solution.minimumOperations([72, 70, 47, 100]) == 2
assert solution.minimumOperations([88, 98, 91]) == 1
assert solution.minimumOperations([33, 84, 3, 21, 80, 48, 52, 15, 29, 62]) == 8
assert solution.minimumOperations([10, 2, 6, 79, 95, 57, 34, 88]) == 6
assert solution.minimumOperations([95, 30, 100, 91, 34, 79, 63, 1, 50]) == 7
assert solution.minimumOperations([33, 13, 76, 41, 91, 6]) == 4
assert solution.minimumOperations([83, 35, 18, 72, 97, 99, 64, 71, 34, 70]) == 8
assert solution.minimumOperations([65, 29]) == 0
assert solution.minimumOperations([66, 23]) == 0
assert solution.minimumOperations([71, 80, 78, 40, 49, 90]) == 4
assert solution.minimumOperations([53, 52, 76, 8, 39, 6, 74, 99]) == 6
assert solution.minimumOperations([22, 4]) == 0
assert solution.minimumOperations([88, 83]) == 0
assert solution.minimumOperations([80, 60, 71, 26, 63, 28, 32, 8, 30, 37]) == 8
assert solution.minimumOperations([61, 36, 50, 38, 90]) == 3
assert solution.minimumOperations([83, 58]) == 0
assert solution.minimumOperations([8, 13]) == 0
assert solution.minimumOperations([8, 7]) == 0
assert solution.minimumOperations([61, 25, 44, 15, 43, 87]) == 4
assert solution.minimumOperations([73, 36, 4, 41, 46, 48]) == 4
assert solution.minimumOperations([83, 77, 71, 41, 5, 63, 74]) == 5
assert solution.minimumOperations([58, 82, 48, 99, 29, 59, 44, 1, 11]) == 7
assert solution.minimumOperations([3, 32]) == 0
assert solution.minimumOperations([24, 51, 15, 84, 49, 100, 73, 92, 45]) == 7
assert solution.minimumOperations([43, 86, 26, 7, 70, 29, 68, 27, 96, 73]) == 8
assert solution.minimumOperations([57, 49, 68, 47, 62]) == 3
assert solution.minimumOperations([39, 31, 11]) == 1
assert solution.minimumOperations([38, 22, 73, 36, 46]) == 3
assert solution.minimumOperations([14, 19, 44, 65, 1, 53, 63, 79, 58]) == 7
assert solution.minimumOperations([83, 99, 87]) == 1
assert solution.minimumOperations([30, 77, 83, 14, 67, 87]) == 4
assert solution.minimumOperations([41, 45, 90, 82, 29, 21]) == 4
assert solution.minimumOperations([79, 75, 54, 50, 27, 94, 68, 59, 7, 19]) == 8
assert solution.minimumOperations([94, 28, 31, 67, 15, 57, 32, 38]) == 6
assert solution.minimumOperations([26, 17, 71, 56, 89]) == 3
assert solution.minimumOperations([35, 19, 41, 49]) == 2
assert solution.minimumOperations([87, 64, 77, 70, 13, 52, 80, 38]) == 6
assert solution.minimumOperations([59, 16, 44, 64, 22, 28, 83, 75]) == 6
assert solution.minimumOperations([41, 1, 14, 78, 33]) == 3
assert solution.minimumOperations([68, 83, 40, 60, 3, 2, 51, 65]) == 6
assert solution.minimumOperations([65, 75]) == 0
assert solution.minimumOperations([65, 61, 99, 35]) == 2
assert solution.minimumOperations([80, 26, 38, 11, 86, 79, 55]) == 5
assert solution.minimumOperations([47, 44, 95, 93, 64, 82, 36]) == 5
assert solution.minimumOperations([12, 63, 22, 19, 25, 50, 74, 61, 68]) == 7

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
