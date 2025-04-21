# Problem 1713: Minimum Operations to Make a Subsequence
# Difficulty: Hard
# Description:
# <p>You are given an array <code>target</code> that consists of <strong>distinct</strong> integers and another integer array <code>arr</code> that <strong>can</strong> have duplicates.</p>
# <p>In one operation, you can insert any integer at any position in <code>arr</code>. For example, if <code>arr = [1,4,1,2]</code>, you can add <code>3</code> in the middle and make it <code>[1,4,<u>3</u>,1,2]</code>. Note that you can insert the integer at the very beginning or end of the array.</p>
# <p>Return <em>the <strong>minimum</strong> number of operations needed to make </em><code>target</code><em> a <strong>subsequence</strong> of </em><code>arr</code><em>.</em></p>
# <p>A <strong>subsequence</strong> of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements&#39; relative order. For example, <code>[2,7,4]</code> is a subsequence of <code>[4,<u>2</u>,3,<u>7</u>,2,1,<u>4</u>]</code> (the underlined elements), while <code>[2,4,2]</code> is not.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> target = [5,1,3], <code>arr</code> = [9,4,2,3,4]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> You can add 5 and 1 in such a way that makes <code>arr</code> = [<u>5</u>,9,4,<u>1</u>,2,3,4], then target will be a subsequence of <code>arr</code>.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> target = [6,4,8,1,3,2], <code>arr</code> = [4,7,6,2,3,8,6,1]
# <strong>Output:</strong> 3
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= target.length, arr.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= target[i], arr[i] &lt;= 10<sup>9</sup></code></li>
# 	<li><code>target</code> contains no duplicates.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from typing import List

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, x, val):
        while x <= self.n:
            self.c[x] = max(self.c[x], val)
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x):
        s = 0
        while x:
            s = max(s, self.c[x])
            x -= BinaryIndexedTree.lowbit(x)
        return s


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {v: i for i, v in enumerate(target)}
        nums = [d[v] for v in arr if v in d]
        return len(target) - self.lengthOfLIS(nums)

    def lengthOfLIS(self, nums):
        s = sorted(set(nums))
        m = {v: i for i, v in enumerate(s, 1)}
        tree = BinaryIndexedTree(len(m))
        ans = 0
        for v in nums:
            x = m[v]
            t = tree.query(x - 1) + 1
            ans = max(ans, t)
            tree.update(x, t)
        return ans

def generate_test_case():
    solution = Solution()

    # Generate target list
    target = random.sample(range(1, 101), random.randint(2, 10))

    # Generate arr list
    arr = random.choices(target + random.sample(range(1, 101), random.randint(1, 10)), k=random.randint(1, 20))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minOperations(target, arr)

    return target, arr, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        target, arr, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minOperations(target, arr) == expected_result
        print(f"assert solution.minOperations({target}, {arr}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.minOperations({target}, {arr}) == {expected_result}") 
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.minOperations([44, 79, 89, 49, 3, 55], [79, 49, 44, 79, 79, 89, 96, 44, 44, 89, 89]) == 3
assert solution.minOperations([8, 70, 96, 12, 27, 37], [49, 27, 70, 96, 68, 27, 37, 70, 68, 8, 96, 31]) == 2
assert solution.minOperations([83, 38], [65]) == 2
assert solution.minOperations([88, 29, 64, 30, 69, 50], [64, 50, 64]) == 4
assert solution.minOperations([82, 30, 52, 10, 1, 49], [72, 72, 30, 52, 22, 39, 53, 82, 39, 30, 91]) == 4
assert solution.minOperations([56, 10, 94, 86, 78, 24], [56, 78, 42, 94, 56, 23, 24, 78, 94, 56, 86, 57, 22, 78, 42, 22, 23]) == 2
assert solution.minOperations([66, 16, 86, 7, 19, 45, 99], [72, 19, 66]) == 6
assert solution.minOperations([30, 38, 45], [45, 45]) == 2
assert solution.minOperations([49, 87, 46, 69, 9, 95, 93, 27, 31], [27, 46, 27, 27, 46, 18, 93, 46, 69, 18]) == 7
assert solution.minOperations([17, 86, 52, 48, 60, 22, 77, 43, 89, 41], [89, 19, 48, 7, 9, 9, 43, 89, 22, 60]) == 7
assert solution.minOperations([81, 24, 15, 22, 78], [37, 37, 15, 37, 24, 15, 22, 24, 78, 81, 22, 38, 22, 24, 78, 22, 38, 24, 22, 22]) == 1
assert solution.minOperations([66, 93, 76, 3, 1, 89, 70], [66, 89]) == 5
assert solution.minOperations([66, 20], [20, 26, 20, 26, 66]) == 1
assert solution.minOperations([76, 94, 48], [92, 76, 76, 48, 21, 76, 92, 48, 92, 21, 48, 94, 76, 48, 81]) == 0
assert solution.minOperations([80, 25, 58, 6, 47, 60, 30], [6, 22, 6, 6, 80, 6, 47, 47, 22, 47, 25, 30, 30, 58, 47, 80]) == 3
assert solution.minOperations([87, 86, 45, 40, 97, 81], [45, 45, 20]) == 5
assert solution.minOperations([56, 71, 87], [71, 71, 71, 87, 34, 71, 56, 71]) == 1
assert solution.minOperations([60, 35, 17, 28, 44, 48, 6, 84, 85], [48, 79, 28, 85, 30, 6, 96, 28]) == 7
assert solution.minOperations([48, 59, 61, 99, 49, 54, 11, 57], [59, 25, 61, 48, 99, 91, 26]) == 5
assert solution.minOperations([36, 70, 26, 94, 34, 77, 35, 64, 28, 79], [34, 24, 64, 67, 79, 19]) == 7
assert solution.minOperations([35, 59, 5, 53, 15, 28, 32], [76, 15, 41, 83, 35, 80, 53, 100, 35, 53, 15]) == 4
assert solution.minOperations([83, 3, 35, 12, 52, 31], [60, 31, 76, 51, 60, 23, 3, 60, 99, 60, 51, 51, 60]) == 5
assert solution.minOperations([76, 3, 39, 33, 21], [76, 24, 29, 24, 15, 18, 21, 3, 29, 21, 76, 29, 39, 33, 39, 24, 75, 3, 76, 75]) == 1
assert solution.minOperations([54, 85, 32, 68, 91, 27, 95], [3, 85, 54, 53, 85, 95, 53, 54, 54, 48, 15, 48, 48, 27, 15, 66, 53]) == 4
assert solution.minOperations([18, 12, 92, 61], [79, 92, 10, 10, 25, 18, 25, 61, 79, 68, 18, 25, 39, 12, 79, 79, 1, 39, 10]) == 2
assert solution.minOperations([48, 37, 1, 16, 27, 45, 99, 12, 58], [12, 95, 45, 9]) == 8
assert solution.minOperations([86, 37, 92, 14, 70, 59, 97, 64, 55], [92, 13, 55, 40, 92, 84, 30, 14, 30]) == 7
assert solution.minOperations([53, 46], [53, 12, 1, 80, 12, 80, 23, 80]) == 1
assert solution.minOperations([78, 58, 20, 28, 53], [81, 53, 20, 13]) == 4
assert solution.minOperations([78, 83, 85, 77, 84, 43, 89, 39], [32, 78, 33, 85, 38, 43, 78]) == 5
assert solution.minOperations([26, 55, 28, 84, 63, 96, 48, 17, 93, 46], [96, 22, 49, 5, 84]) == 9
assert solution.minOperations([20, 50, 89, 80, 73, 78, 6, 38, 37, 26], [37, 58, 26, 20, 99, 78, 6, 25, 25, 38]) == 6
assert solution.minOperations([26, 99, 87, 42], [68, 66, 66, 26, 99]) == 2
assert solution.minOperations([66, 62], [84, 84, 11, 66, 11, 62, 62, 62, 62, 11, 62, 62, 62, 84, 84, 66, 62]) == 0
assert solution.minOperations([41, 3], [94, 62, 62]) == 2
assert solution.minOperations([33, 52, 28, 32, 18, 96, 78, 79, 46], [27]) == 9
assert solution.minOperations([58, 32, 27, 48], [27, 23, 27, 97, 97, 97, 97, 23, 58, 97, 97, 27, 58, 48, 27]) == 1
assert solution.minOperations([81, 48, 40, 78, 29], [27, 40, 81, 90, 81, 44, 27, 48, 78, 47]) == 2
assert solution.minOperations([80, 62, 34], [34, 62, 59, 8, 8, 62, 80, 34, 59, 62, 34, 62, 43, 34, 8, 34, 34, 43, 59, 8]) == 0
assert solution.minOperations([87, 78, 48, 28], [87, 76, 78, 19, 11, 48, 19, 48, 78, 87, 87, 87, 28, 28, 78, 87, 78, 48, 28, 87]) == 0
assert solution.minOperations([38, 92, 9, 64, 75, 50, 44, 82], [44, 64, 92, 44, 92, 82, 9]) == 5
assert solution.minOperations([97, 80], [80, 80, 97, 35, 35, 97, 80, 8, 1, 35, 71, 97, 63, 71, 80, 8]) == 0
assert solution.minOperations([6, 2, 88, 20, 30, 85, 13, 5], [26, 31, 26, 6, 73, 88, 5, 20, 27, 26, 13, 13, 2, 6, 30]) == 4
assert solution.minOperations([4, 62, 53, 68, 61, 7, 69, 82, 2, 44], [96, 39]) == 10
assert solution.minOperations([36, 25, 100, 24, 97, 37, 35, 5], [27, 51, 87, 27, 47, 27, 51]) == 8
assert solution.minOperations([41, 35, 29], [78, 20, 29, 23, 30, 55, 90, 90, 23, 67, 30, 30, 29]) == 2
assert solution.minOperations([72, 88, 7, 64, 3, 19, 23, 53], [88, 53, 72, 72, 53, 7]) == 6
assert solution.minOperations([20, 49, 7, 40, 50, 32, 65, 99, 92, 87], [7, 87, 32, 80, 49, 99, 87, 20, 50, 92, 7, 20, 7, 80, 87, 32, 65, 20, 40, 40]) == 5
assert solution.minOperations([64, 49, 85], [20, 95, 21, 85]) == 2
assert solution.minOperations([35, 71, 97, 62, 40, 42, 2], [62, 42, 97, 97, 27, 35, 29, 62, 6, 62, 27, 39]) == 5
assert solution.minOperations([11, 37, 8], [35, 90, 8, 17, 37, 32, 90, 32, 37, 35, 11, 37, 35, 8, 35, 37]) == 0
assert solution.minOperations([50, 92, 100, 79, 84, 25, 51, 61, 37], [18, 87, 37, 85, 73, 74, 76, 18, 100, 53, 76, 73, 73, 76, 37]) == 7
assert solution.minOperations([15, 72, 92, 28, 63, 76, 78, 97, 2, 5], [63, 97, 2, 79, 72, 78, 2, 2, 79, 78, 92, 72, 72, 79, 5, 63, 5, 15, 28, 78]) == 6
assert solution.minOperations([46, 96, 10, 83, 75, 34, 9, 91, 29, 15], [83, 46, 42, 42, 15, 91, 86, 34, 2, 75, 57, 2, 34, 29, 9, 83, 64]) == 6
assert solution.minOperations([76, 18], [76, 100, 18, 97, 100, 18, 97, 97, 100, 100, 97, 97, 18, 24, 100, 18, 97]) == 0
assert solution.minOperations([57, 4, 47, 34, 96, 8, 62, 84], [35]) == 8
assert solution.minOperations([68, 89, 44, 30, 21, 76, 99, 35, 95, 38], [21, 95, 30, 77, 38, 46, 21, 44, 68, 26, 68, 30]) == 7
assert solution.minOperations([45, 69], [69, 69, 82, 45, 69]) == 0
assert solution.minOperations([67, 7, 49, 92, 35, 89, 57, 81, 63, 56], [7, 56, 49, 92, 41, 41, 7, 81, 7, 56, 81, 41, 67]) == 5
assert solution.minOperations([94, 2], [2, 29, 29, 94, 94, 91, 2, 29, 91, 92]) == 0
assert solution.minOperations([38, 19, 75, 80], [75, 59, 58, 93, 75, 38, 42, 80, 80, 75]) == 2
assert solution.minOperations([17, 54, 28], [31, 69, 28, 17, 80, 28, 31, 28, 31, 17, 80, 5, 54]) == 1
assert solution.minOperations([7, 79, 19, 9, 14, 23, 96, 69, 52], [96, 52, 2, 23, 52, 14, 23, 68, 79, 70, 69, 52, 51, 70, 96, 52, 23, 7, 19]) == 5
assert solution.minOperations([55, 79], [75, 79, 75, 1, 32, 98, 55, 32, 1, 79, 58, 1, 75]) == 0
assert solution.minOperations([78, 21, 9, 23, 96], [21, 23, 44, 44, 23, 44, 96]) == 2
assert solution.minOperations([57, 11, 12, 63, 75], [58, 58, 41, 73, 41, 76, 29, 73]) == 5
assert solution.minOperations([100, 25, 51, 57, 28, 71, 99, 65, 75], [65]) == 8
assert solution.minOperations([53, 65, 66, 43, 7, 98, 12, 28, 74], [98, 65, 12, 98]) == 7
assert solution.minOperations([76, 36, 61, 9, 4, 84, 83, 66, 35], [87, 97, 86, 86, 19, 97, 4]) == 8
assert solution.minOperations([45, 97, 96, 72], [45, 97, 51]) == 2
assert solution.minOperations([83, 78], [78, 6, 98, 43, 78, 6, 43, 45, 76, 98]) == 1
assert solution.minOperations([12, 9], [43, 9]) == 1
assert solution.minOperations([47, 71, 4, 32, 55, 72], [79, 32, 79, 55, 28, 71, 31, 6, 32, 79, 79, 6, 30]) == 4
assert solution.minOperations([20, 7, 33, 64, 36, 54, 31], [84, 31]) == 6
assert solution.minOperations([2, 87, 44, 65, 47, 99, 91], [94, 87, 99, 2, 47, 99, 99, 94, 75, 44, 91, 66, 91, 2, 2]) == 3
assert solution.minOperations([56, 70, 22, 30, 28, 99, 63], [99, 56, 95, 22, 26, 65]) == 5
assert solution.minOperations([57, 61, 12, 72, 58, 96, 21, 91, 51], [57, 100, 65]) == 8
assert solution.minOperations([39, 61, 68, 12, 22, 51, 14, 77, 6], [95, 59, 68, 59, 85, 6, 22, 14]) == 6
assert solution.minOperations([53, 72, 30, 50, 23], [30, 53, 72, 30, 52, 30, 89, 52, 89, 8, 89]) == 2
assert solution.minOperations([72, 45, 84, 13, 15, 97, 30], [84, 13, 15, 84, 97, 45, 15, 84, 13, 45, 45, 35, 84, 72, 45, 45, 72, 72, 15, 13]) == 3
assert solution.minOperations([22, 66, 35, 95, 67, 57, 11, 60], [90, 66, 60, 66, 11, 47, 11, 90, 44, 57, 95, 44, 67, 22, 95]) == 5
assert solution.minOperations([4, 62, 6, 2, 100, 99, 64, 72, 10, 14], [71, 97, 99, 54, 99, 54, 99, 20, 71, 6, 85, 20, 62]) == 9
assert solution.minOperations([85, 37, 11, 53, 94, 93, 10, 56, 68], [68, 17, 94]) == 8
assert solution.minOperations([25, 70, 98, 35, 18, 99, 31, 19, 44], [56, 46, 79, 67, 46, 99, 46, 76, 99]) == 8
assert solution.minOperations([36, 100, 21], [27, 21, 36]) == 2
assert solution.minOperations([8, 56, 46, 24], [46, 4, 24, 20, 8, 20, 24, 24, 46, 46, 56, 97, 4, 20, 92]) == 2
assert solution.minOperations([32, 97, 50, 65, 46, 7, 47, 63], [94, 47, 66, 22, 63, 63, 32, 70, 32, 25, 47, 76, 25, 92, 65, 92, 97, 63, 63]) == 5
assert solution.minOperations([98, 3, 9, 42, 75, 38, 65], [9, 42, 75, 38, 42, 20, 50, 50]) == 3
assert solution.minOperations([5, 58, 93, 83], [77, 86, 86, 84, 71, 28, 83]) == 3
assert solution.minOperations([45, 83, 61], [28, 83, 19, 61, 28, 45, 19, 81, 28]) == 1
assert solution.minOperations([58, 34, 50, 31, 11, 59, 38, 89, 36, 17], [58, 58, 38, 18, 11, 89, 17, 11, 74, 48, 11, 55, 50, 14, 11, 50, 55, 31, 38, 38]) == 6
assert solution.minOperations([44, 85, 5, 45, 46, 58, 52, 91, 35, 51], [87, 82, 87, 63, 47, 44, 16, 69, 72, 69, 82]) == 9
assert solution.minOperations([38, 89, 31, 99, 4, 13, 16], [6, 99, 13, 6, 16, 6, 31, 89, 100]) == 4
assert solution.minOperations([66, 55], [13, 55, 13, 96, 28, 49, 22, 85, 72]) == 1
assert solution.minOperations([7, 92, 86, 4], [86, 75, 86, 16, 86, 4, 7]) == 2
assert solution.minOperations([78, 35, 63], [63, 48, 48, 78, 78, 78, 39, 35, 35, 81, 35, 81, 78, 81, 78, 48]) == 1
assert solution.minOperations([71, 68, 7, 31, 40, 82, 23], [7, 54, 75, 40, 82, 71, 7, 75, 82, 40, 23, 75, 54, 7]) == 3
assert solution.minOperations([60, 6, 95, 42, 77, 44, 48, 45, 78], [42, 78, 77, 60, 95, 95, 48, 6, 95, 78, 95, 48, 42, 42, 78, 60]) == 4
assert solution.minOperations([96, 31, 18, 51, 20, 58], [20, 69, 51, 11, 30, 18, 18, 31, 51, 69, 96, 50, 38, 38]) == 4
assert solution.minOperations([47, 23, 79, 33, 44, 75, 94, 5, 14], [44, 14, 63, 75, 5, 47, 14, 44, 47, 14, 63, 63, 79, 23, 5, 47, 44, 79, 33, 75]) == 4

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
