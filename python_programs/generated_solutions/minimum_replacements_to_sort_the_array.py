# Problem 2366: Minimum Replacements to Sort the Array
# Difficulty: Hard
# Description:
# <p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>. In one operation you can replace any element of the array with <strong>any two</strong> elements that <strong>sum</strong> to it.</p>
# <ul>
# 	<li>For example, consider <code>nums = [5,6,7]</code>. In one operation, we can replace <code>nums[1]</code> with <code>2</code> and <code>4</code> and convert <code>nums</code> to <code>[5,2,4,7]</code>.</li>
# </ul>
# <p>Return <em>the minimum number of operations to make an array that is sorted in <strong>non-decreasing</strong> order</em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [3,9,3]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> Here are the steps to sort the array in non-decreasing order:
# - From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
# - From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
# There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [1,2,3,4,5]
# <strong>Output:</strong> 0
# <strong>Explanation:</strong> The array is already in non-decreasing order. Therefore, we return 0. 
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        mx = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= mx:
                mx = nums[i]
                continue
            k = (nums[i] + mx - 1) // mx
            ans += k - 1
            mx = nums[i] // k
        return ans

def generate_test_case():
    solution = Solution()
    test_case_generator_results = []
    for i in range(100):
        # Generate random numbers list
        nums = random.sample(range(1, 101), random.randint(2, 10))

        # Calculate the expected result using the provided Solution class
        expected_result = solution.minimumReplacement(nums)

        test_case_generator_results.append(f"assert solution.minimumReplacement({nums}) == {expected_result}")
    
    return test_case_generator_results

if __name__ == "__main__":
    test_case_generator_results = generate_test_case()

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.minimumReplacement([73, 81, 20, 65]) == 8
assert solution.minimumReplacement([100, 44, 45, 79, 96, 46, 49, 26, 2]) == 440
assert solution.minimumReplacement([1, 39, 96, 15]) == 8
assert solution.minimumReplacement([95, 89, 30, 62, 8, 85, 56, 16, 66]) == 52
assert solution.minimumReplacement([46, 53, 72, 81, 57, 26]) == 16
assert solution.minimumReplacement([13, 99, 62, 39]) == 4
assert solution.minimumReplacement([94, 8, 30, 87, 24, 44, 26]) == 22
assert solution.minimumReplacement([94, 1, 87]) == 93
assert solution.minimumReplacement([99, 56]) == 1
assert solution.minimumReplacement([74, 31, 9, 70, 37, 82]) == 14
assert solution.minimumReplacement([10, 1, 21, 13, 44, 89]) == 10
assert solution.minimumReplacement([83, 28, 94, 20, 82]) == 10
assert solution.minimumReplacement([98, 21, 23, 100]) == 4
assert solution.minimumReplacement([8, 26]) == 0
assert solution.minimumReplacement([69, 50, 59]) == 1
assert solution.minimumReplacement([7, 26]) == 0
assert solution.minimumReplacement([31, 46, 21, 61, 98, 66, 47, 33, 88]) == 18
assert solution.minimumReplacement([19, 68, 76, 92, 94, 66, 58, 70]) == 9
assert solution.minimumReplacement([88, 86, 42, 85, 82, 71, 43, 3]) == 427
assert solution.minimumReplacement([69, 29, 79]) == 2
assert solution.minimumReplacement([23, 47, 40, 7, 52, 44, 34, 31]) == 22
assert solution.minimumReplacement([86, 47, 71, 53, 83]) == 5
assert solution.minimumReplacement([17, 34, 43, 97, 9, 86, 80]) == 22
assert solution.minimumReplacement([64, 20, 38, 32]) == 8
assert solution.minimumReplacement([85, 24, 19, 5, 28, 10]) == 31
assert solution.minimumReplacement([87, 58, 71, 27, 22, 60, 13, 67, 59]) == 34
assert solution.minimumReplacement([41, 95, 15, 59, 76, 48, 10]) == 47
assert solution.minimumReplacement([56, 20, 82]) == 2
assert solution.minimumReplacement([1, 26, 59, 67, 96, 53, 47, 61, 39, 18]) == 39
assert solution.minimumReplacement([86, 11, 18, 94, 35]) == 9
assert solution.minimumReplacement([81, 40, 29, 39, 24, 91]) == 10
assert solution.minimumReplacement([37, 7, 90, 17, 55, 3]) == 157
assert solution.minimumReplacement([7, 55, 44, 28, 3]) == 63
assert solution.minimumReplacement([86, 63, 29, 14, 58, 66, 9]) == 52
assert solution.minimumReplacement([74, 10, 11, 58]) == 7
assert solution.minimumReplacement([97, 77, 45, 25, 50, 3, 5]) == 244
assert solution.minimumReplacement([75, 82, 83, 79, 15]) == 25
assert solution.minimumReplacement([100, 3]) == 33
assert solution.minimumReplacement([93, 7, 62, 51, 88, 21]) == 22
assert solution.minimumReplacement([48, 54, 45, 7, 70, 29, 37, 33, 100, 77]) == 28
assert solution.minimumReplacement([31, 13, 98, 65, 9, 48, 24, 78, 1]) == 358
assert solution.minimumReplacement([65, 83, 99, 59, 50, 16, 94, 55, 11]) == 75
assert solution.minimumReplacement([43, 58, 38, 1, 51, 14, 46, 17, 52]) == 141
assert solution.minimumReplacement([84, 14, 1, 13, 52, 56, 3]) == 145
assert solution.minimumReplacement([5, 89, 43, 61, 28, 41]) == 10
assert solution.minimumReplacement([76, 17, 93, 96, 47, 64, 7, 22, 54, 36]) == 101
assert solution.minimumReplacement([44, 89, 63]) == 1
assert solution.minimumReplacement([8, 48, 35]) == 1
assert solution.minimumReplacement([54, 60, 46, 8]) == 21
assert solution.minimumReplacement([35, 27, 48, 14, 96, 68, 44, 64, 24, 58]) == 32
assert solution.minimumReplacement([44, 88, 45, 89, 35, 50]) == 7
assert solution.minimumReplacement([61, 90, 3, 30, 5]) == 54
assert solution.minimumReplacement([15, 31, 51, 91, 33]) == 4
assert solution.minimumReplacement([52, 96, 10, 99, 97, 64, 20, 25]) == 30
assert solution.minimumReplacement([16, 54, 74, 82]) == 0
assert solution.minimumReplacement([80, 33, 13, 52]) == 9
assert solution.minimumReplacement([76, 54, 19, 78]) == 6
assert solution.minimumReplacement([49, 75, 63, 29]) == 7
assert solution.minimumReplacement([71, 7, 68, 16, 5, 64, 48, 88]) == 44
assert solution.minimumReplacement([30, 9, 18, 20, 10, 75, 21]) == 8
assert solution.minimumReplacement([36, 24]) == 1
assert solution.minimumReplacement([50, 79]) == 0
assert solution.minimumReplacement([78, 59, 73, 26]) == 8
assert solution.minimumReplacement([5, 2, 33, 27, 1, 49, 41, 72]) == 64
assert solution.minimumReplacement([43, 9, 80]) == 4
assert solution.minimumReplacement([75, 18, 26, 83, 28, 22, 82, 95]) == 16
assert solution.minimumReplacement([81, 72, 91, 13, 80]) == 17
assert solution.minimumReplacement([2, 31, 41, 32, 18, 27]) == 5
assert solution.minimumReplacement([20, 91, 16, 14, 41, 6, 1, 94]) == 182
assert solution.minimumReplacement([5, 91, 7, 74, 96]) == 12
assert solution.minimumReplacement([19, 42, 56, 24, 11, 60, 93, 55]) == 17
assert solution.minimumReplacement([38, 23, 86, 51, 95, 2, 91, 52]) == 242
assert solution.minimumReplacement([95, 49, 73, 40]) == 5
assert solution.minimumReplacement([40, 93, 12]) == 10
assert solution.minimumReplacement([9, 48, 2, 3, 90, 52, 78]) == 28
assert solution.minimumReplacement([36, 52]) == 0
assert solution.minimumReplacement([48, 2, 70, 96, 77, 65, 21]) == 41
assert solution.minimumReplacement([83, 24, 17, 59, 54]) == 8
assert solution.minimumReplacement([32, 41, 38, 51, 18, 58, 81, 2, 13]) == 272
assert solution.minimumReplacement([40, 6, 47, 29, 26, 99, 81, 54]) == 13
assert solution.minimumReplacement([77, 36]) == 2
assert solution.minimumReplacement([6, 71, 31, 75, 62]) == 3
assert solution.minimumReplacement([92, 64, 56, 31, 90]) == 7
assert solution.minimumReplacement([57, 74, 22, 24, 12]) == 13
assert solution.minimumReplacement([9, 95, 24, 14, 81, 53]) == 9
assert solution.minimumReplacement([27, 87, 50, 15, 68, 4, 18, 65]) == 104
assert solution.minimumReplacement([35, 38, 3]) == 29
assert solution.minimumReplacement([93, 64, 80, 1, 47]) == 234
assert solution.minimumReplacement([65, 28, 47, 49]) == 2
assert solution.minimumReplacement([24, 99, 92, 1, 75]) == 212
assert solution.minimumReplacement([48, 62]) == 0
assert solution.minimumReplacement([86, 80, 34, 84, 63, 18, 1]) == 359
assert solution.minimumReplacement([44, 23, 88, 49, 82, 22, 26]) == 14
assert solution.minimumReplacement([85, 83, 90, 14]) == 19
assert solution.minimumReplacement([85, 69]) == 1
assert solution.minimumReplacement([85, 1, 78, 100, 68]) == 86
assert solution.minimumReplacement([11, 70, 99, 28]) == 5
assert solution.minimumReplacement([26, 9, 67, 74, 2, 40, 61, 20, 92, 16]) == 118
assert solution.minimumReplacement([6, 79, 30]) == 2
assert solution.minimumReplacement([6, 23, 89, 25, 21]) == 10

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
