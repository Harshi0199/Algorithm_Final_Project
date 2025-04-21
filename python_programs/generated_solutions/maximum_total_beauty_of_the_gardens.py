# Problem 2234: Maximum Total Beauty of the Gardens
# Difficulty: Hard
# Description:
# <p>Alice is a caretaker of <code>n</code> gardens and she wants to plant flowers to maximize the total beauty of all her gardens.</p>
# <p>You are given a <strong>0-indexed</strong> integer array <code>flowers</code> of size <code>n</code>, where <code>flowers[i]</code> is the number of flowers already planted in the <code>i<sup>th</sup></code> garden. Flowers that are already planted <strong>cannot</strong> be removed. You are then given another integer <code>newFlowers</code>, which is the <strong>maximum</strong> number of flowers that Alice can additionally plant. You are also given the integers <code>target</code>, <code>full</code>, and <code>partial</code>.</p>
# <p>A garden is considered <strong>complete</strong> if it has <strong>at least</strong> <code>target</code> flowers. The <strong>total beauty</strong> of the gardens is then determined as the <strong>sum</strong> of the following:</p>
# <ul>
# 	<li>The number of <strong>complete</strong> gardens multiplied by <code>full</code>.</li>
# 	<li>The <strong>minimum</strong> number of flowers in any of the <strong>incomplete</strong> gardens multiplied by <code>partial</code>. If there are no incomplete gardens, then this value will be <code>0</code>.</li>
# </ul>
# <p>Return <em>the <strong>maximum</strong> total beauty that Alice can obtain after planting at most </em><code>newFlowers</code><em> flowers.</em></p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
# <strong>Output:</strong> 14
# <strong>Explanation:</strong> Alice can plant
# - 2 flowers in the 0<sup>th</sup> garden
# - 3 flowers in the 1<sup>st</sup> garden
# - 1 flower in the 2<sup>nd</sup> garden
# - 1 flower in the 3<sup>rd</sup> garden
# The gardens will then be [3,6,2,2]. She planted a total of 2 + 3 + 1 + 1 = 7 flowers.
# There is 1 garden that is complete.
# The minimum number of flowers in the incomplete gardens is 2.
# Thus, the total beauty is 1 * 12 + 2 * 1 = 12 + 2 = 14.
# No other way of planting flowers can obtain a total beauty higher than 14.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
# <strong>Output:</strong> 30
# <strong>Explanation:</strong> Alice can plant
# - 3 flowers in the 0<sup>th</sup> garden
# - 0 flowers in the 1<sup>st</sup> garden
# - 0 flowers in the 2<sup>nd</sup> garden
# - 2 flowers in the 3<sup>rd</sup> garden
# The gardens will then be [5,4,5,5]. She planted a total of 3 + 0 + 0 + 2 = 5 flowers.
# There are 3 gardens that are complete.
# The minimum number of flowers in the incomplete gardens is 4.
# Thus, the total beauty is 3 * 2 + 4 * 6 = 6 + 24 = 30.
# No other way of planting flowers can obtain a total beauty higher than 30.
# Note that Alice could make all the gardens complete but in this case, she would obtain a lower total beauty.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= flowers.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= flowers[i], target &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= newFlowers &lt;= 10<sup>10</sup></code></li>
# 	<li><code>1 &lt;= full, partial &lt;= 10<sup>5</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from itertools import accumulate
from bisect import bisect_left
from typing import List

# Task solution class
class Solution:
    def maximumBeauty(
        self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int
    ) -> int:
        flowers.sort()
        n = len(flowers)
        s = list(accumulate(flowers, initial=0))
        ans, i = 0, n - bisect_left(flowers, target)
        for x in range(i, n + 1):
            newFlowers -= 0 if x == 0 else max(target - flowers[n - x], 0)
            if newFlowers < 0:
                break
            l, r = 0, n - x - 1
            while l < r:
                mid = (l + r + 1) >> 1
                if flowers[mid] * (mid + 1) - s[mid + 1] <= newFlowers:
                    l = mid
                else:
                    r = mid - 1
            y = 0
            if r != -1:
                cost = flowers[l] * (l + 1) - s[l + 1]
                y = min(flowers[l] + (newFlowers - cost) // (l + 1), target - 1)
            ans = max(ans, x * full + y * partial)
        return ans

# Test case generator
class TestCaseGenerator:
    def __init__(self):
        self.solution = Solution()

    def generate_test_case(self):
        # Generate random numbers list
        flowers = random.sample(range(1, 101), random.randint(2, 10))

        # Generate the maximum number of new flowers that Alice can plant
        newFlowers = random.randint(1, 101)

        # Generate the target number of flowers for completeness
        target = random.randint(1, 101)

        # Generate random values for full and partial beauty
        full = random.randint(1, 101)
        partial = random.randint(1, 101)

        # Calculate the expected result using the provided Solution class
        expected_result = self.solution.maximumBeauty(flowers, newFlowers, target, full, partial)

        return flowers, newFlowers, target, full, partial, expected_result

    def test_generated_test_cases(self, num_tests):
        test_case_generator_results = []
        for i in range(num_tests):
            flowers, newFlowers, target, full, partial, expected_result = self.generate_test_case()
            solution = Solution()
            assert solution.maximumBeauty(flowers, newFlowers, target, full, partial) == expected_result
            print(f"assert solution.maximumBeauty({flowers}, {newFlowers}, {target}, {full}, {partial}) == {expected_result}")
            test_case_generator_results.append(f"assert solution.maximumBeauty({flowers}, {newFlowers}, {target}, {full}, {partial}) == {expected_result}")
        return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator = TestCaseGenerator()
    test_case_generator_results = test_case_generator.test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.maximumBeauty([1, 6, 29, 53, 54, 85, 91, 93, 96, 100], 3, 56, 22, 46) == 294
assert solution.maximumBeauty([20, 50, 60, 68], 6, 31, 39, 94) == 2561
assert solution.maximumBeauty([13, 44, 54, 74, 77, 79, 91], 43, 73, 88, 57) == 3202
assert solution.maximumBeauty([2, 6, 41, 51, 80], 72, 1, 30, 38) == 150
assert solution.maximumBeauty([5, 26, 34, 51, 77, 87, 88], 91, 73, 48, 67) == 3561
assert solution.maximumBeauty([9, 14, 19, 41, 66, 73, 80, 81, 90], 39, 79, 39, 59) == 1710
assert solution.maximumBeauty([10, 28, 29, 37, 42, 50, 57, 91, 92], 12, 20, 62, 61) == 1655
assert solution.maximumBeauty([13, 18, 68], 73, 20, 98, 25) == 671
assert solution.maximumBeauty([4, 35, 38, 69], 81, 86, 82, 63) == 3276
assert solution.maximumBeauty([2, 5, 24, 37, 41, 48, 50, 69, 78], 96, 20, 9, 46) == 946
assert solution.maximumBeauty([2, 9, 16, 17, 23, 37, 39, 77, 82, 95], 47, 28, 34, 78) == 1886
assert solution.maximumBeauty([3, 74], 97, 56, 35, 65) == 3610
assert solution.maximumBeauty([3, 5, 7, 36, 72, 87, 100], 75, 51, 10, 82) == 2490
assert solution.maximumBeauty([79, 100], 54, 92, 63, 62) == 5705
assert solution.maximumBeauty([9, 19, 50, 58, 69, 71, 75, 78, 84, 93], 31, 53, 60, 41) == 1628
assert solution.maximumBeauty([9, 17, 28, 52, 57, 65, 89, 96, 98], 3, 58, 87, 94) == 1476
assert solution.maximumBeauty([1, 9, 26, 27, 29, 56, 61, 77, 92, 98], 67, 5, 83, 76) == 1051
assert solution.maximumBeauty([4, 32, 53, 59, 61, 65, 75, 76, 81, 88], 96, 77, 96, 15) == 1326
assert solution.maximumBeauty([38, 44, 46, 60], 91, 15, 79, 3) == 316
assert solution.maximumBeauty([31, 37, 65, 72, 73, 94], 33, 27, 33, 23) == 198
assert solution.maximumBeauty([32, 48, 50, 57, 68, 72, 78], 57, 101, 8, 4) == 244
assert solution.maximumBeauty([24, 36, 76], 35, 30, 37, 92) == 2742
assert solution.maximumBeauty([69, 99], 52, 101, 7, 15) == 1507
assert solution.maximumBeauty([14, 23, 25, 53, 72], 47, 19, 101, 65) == 1574
assert solution.maximumBeauty([12, 32, 47, 58, 69], 78, 13, 61, 20) == 484
assert solution.maximumBeauty([61, 74], 92, 96, 16, 53) == 5051
assert solution.maximumBeauty([6, 13, 19, 30, 36, 89, 91, 95, 96], 93, 72, 67, 28) == 1360
assert solution.maximumBeauty([1, 16, 41, 66, 72], 55, 32, 36, 86) == 2810
assert solution.maximumBeauty([21, 54, 74, 78], 4, 77, 24, 100) == 2524
assert solution.maximumBeauty([67, 89], 30, 83, 33, 11) == 935
assert solution.maximumBeauty([15, 23, 38, 45, 49, 56, 57, 73, 82], 47, 9, 84, 17) == 756
assert solution.maximumBeauty([15, 21, 34, 44, 54, 96], 82, 60, 81, 9) == 639
assert solution.maximumBeauty([62, 68], 55, 99, 45, 54) == 4968
assert solution.maximumBeauty([24, 42, 45, 52, 57, 98], 80, 34, 8, 76) == 2548
assert solution.maximumBeauty([37, 92], 34, 84, 30, 98) == 6988
assert solution.maximumBeauty([37, 54, 78, 80, 89, 96], 12, 41, 12, 21) == 900
assert solution.maximumBeauty([21, 38, 56, 58, 73, 82, 91, 99, 100], 63, 50, 84, 88) == 4984
assert solution.maximumBeauty([12, 15, 19, 39, 44, 76, 98], 40, 80, 11, 78) == 2195
assert solution.maximumBeauty([8, 19, 33, 50, 66, 70, 76, 82, 89, 96], 77, 90, 72, 75) == 3519
assert solution.maximumBeauty([1, 5, 10, 13, 23, 29, 31, 32, 53, 72], 37, 19, 9, 2) == 100
assert solution.maximumBeauty([14, 42, 53], 1, 7, 82, 95) == 246
assert solution.maximumBeauty([6, 18, 25, 43, 47, 67], 83, 74, 96, 93) == 3999
assert solution.maximumBeauty([3, 40, 73, 89, 97], 73, 59, 54, 97) == 5788
assert solution.maximumBeauty([2, 21, 25, 46, 53, 57, 62], 46, 67, 43, 64) == 1984
assert solution.maximumBeauty([29, 44, 59, 61, 83, 86, 92], 77, 58, 45, 29) == 1923
assert solution.maximumBeauty([26, 92, 100], 39, 33, 57, 6) == 306
assert solution.maximumBeauty([1, 10, 12, 36, 44, 52, 63, 95], 29, 62, 92, 36) == 796
assert solution.maximumBeauty([14, 51, 65, 99], 80, 3, 38, 25) == 152
assert solution.maximumBeauty([25, 46], 86, 51, 88, 73) == 3738
assert solution.maximumBeauty([17, 74, 93], 94, 91, 63, 88) == 8046
assert solution.maximumBeauty([12, 26, 34, 36, 39, 50, 51, 61, 72, 99], 53, 41, 76, 17) == 1296
assert solution.maximumBeauty([24, 27, 43, 54, 69, 89, 90, 97, 98], 31, 52, 85, 25) == 1535
assert solution.maximumBeauty([41, 46, 48, 55, 60, 71, 98], 59, 21, 18, 37) == 126
assert solution.maximumBeauty([9, 43], 85, 23, 37, 94) == 2105
assert solution.maximumBeauty([6, 14, 30, 37, 38, 43, 95], 41, 35, 44, 67) == 2186
assert solution.maximumBeauty([6, 56, 86, 88], 76, 40, 6, 83) == 3255
assert solution.maximumBeauty([21, 37, 86, 92, 96], 7, 75, 97, 80) == 2531
assert solution.maximumBeauty([5, 28, 39, 46, 50, 62, 68, 71, 96], 101, 77, 71, 64) == 3470
assert solution.maximumBeauty([22, 35, 36, 50, 100], 68, 96, 92, 6) == 412
assert solution.maximumBeauty([4, 9, 32, 42, 66, 72, 73, 82], 9, 75, 72, 93) == 1095
assert solution.maximumBeauty([2, 10, 11, 32, 46, 48, 64, 74, 79, 93], 12, 83, 94, 23) == 418
assert solution.maximumBeauty([3, 22, 26, 31, 33, 37, 79, 86, 87], 7, 75, 62, 54) == 726
assert solution.maximumBeauty([4, 14, 29, 41, 48, 50, 64, 67, 69], 52, 15, 49, 90) == 1652
assert solution.maximumBeauty([65, 94], 88, 65, 34, 35) == 68
assert solution.maximumBeauty([1, 4, 48, 55, 74, 94], 36, 65, 51, 10) == 303
assert solution.maximumBeauty([20, 65], 90, 98, 73, 23) == 2001
assert solution.maximumBeauty([10, 56], 100, 64, 22, 68) == 4306
assert solution.maximumBeauty([32, 67], 2, 96, 17, 3) == 102
assert solution.maximumBeauty([1, 17, 60, 69, 76], 10, 45, 19, 62) == 739
assert solution.maximumBeauty([10, 19, 55, 59, 60, 64, 67], 90, 21, 64, 99) == 2364
assert solution.maximumBeauty([11, 14, 32, 39, 66, 85], 85, 84, 64, 95) == 4339
assert solution.maximumBeauty([28, 32, 36, 37, 44, 68, 72, 97, 99], 58, 87, 72, 49) == 2447
assert solution.maximumBeauty([37, 52, 54, 61, 63, 65, 84, 86, 89, 100], 34, 60, 14, 6) == 468
assert solution.maximumBeauty([13, 32, 48, 67, 72, 73, 99], 20, 12, 39, 81) == 273
assert solution.maximumBeauty([11, 25, 48, 57, 63, 64, 70, 76, 95], 1, 93, 24, 97) == 1188
assert solution.maximumBeauty([70, 75, 78], 73, 97, 65, 14) == 1474
assert solution.maximumBeauty([32, 98], 13, 8, 55, 34) == 110
assert solution.maximumBeauty([3, 15, 29, 37, 58, 69, 74, 76, 99], 13, 9, 87, 25) == 896
assert solution.maximumBeauty([4, 25, 45, 60, 67, 79, 91, 92], 28, 65, 70, 63) == 2044
assert solution.maximumBeauty([9, 36, 39, 44, 64, 67, 78, 85], 51, 61, 49, 35) == 1736
assert solution.maximumBeauty([16, 28, 31, 38, 41, 71, 80], 12, 86, 61, 69) == 1932
assert solution.maximumBeauty([32, 87], 45, 66, 25, 57) == 3730
assert solution.maximumBeauty([7, 18, 35, 37, 47, 51, 59, 82, 90, 92], 78, 62, 89, 58) == 2850
assert solution.maximumBeauty([35, 36, 49, 60, 63, 87, 92, 99], 96, 75, 38, 74) == 5072
assert solution.maximumBeauty([11, 21, 22, 53, 83], 36, 98, 26, 13) == 390
assert solution.maximumBeauty([2, 28, 30, 40, 47, 49, 50, 58, 72], 82, 97, 9, 35) == 1575
assert solution.maximumBeauty([86, 94], 68, 49, 71, 89) == 142
assert solution.maximumBeauty([14, 22, 23, 35, 46, 49, 54, 57, 85, 93], 62, 37, 75, 11) == 1071
assert solution.maximumBeauty([8, 27, 34, 46, 56], 50, 61, 56, 49) == 1918
assert solution.maximumBeauty([7, 23, 75], 15, 73, 11, 28) == 627
assert solution.maximumBeauty([3, 15, 31, 49, 55, 56, 64, 68, 97], 19, 57, 75, 7) == 527
assert solution.maximumBeauty([63, 65, 74], 56, 7, 77, 18) == 231
assert solution.maximumBeauty([9, 12, 20, 30, 68, 73, 82], 81, 89, 78, 92) == 3496
assert solution.maximumBeauty([74, 86], 5, 66, 26, 96) == 52
assert solution.maximumBeauty([12, 19, 26, 31, 38, 44, 57, 62, 70], 49, 31, 7, 60) == 1856
assert solution.maximumBeauty([1, 58, 69, 74, 76], 61, 31, 77, 11) == 638
assert solution.maximumBeauty([9, 81], 52, 60, 87, 81) == 4866
assert solution.maximumBeauty([61, 71, 79], 37, 70, 2, 67) == 4627
assert solution.maximumBeauty([65, 71], 8, 67, 12, 41) == 2718
assert solution.maximumBeauty([1, 32, 38, 61, 81, 83], 11, 73, 26, 5) == 112

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
