# Problem 2708: Maximum Strength of a Group
# Difficulty: Medium
# Description:
# <p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> representing the score of students in an exam. The teacher would like to form one <strong>non-empty</strong> group of students with maximal <strong>strength</strong>, where the strength of a group of students of indices <code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, <code>i<sub>2</sub></code>, ... , <code>i<sub>k</sub></code> is defined as <code>nums[i<sub>0</sub>] * nums[i<sub>1</sub>] * nums[i<sub>2</sub>] * ... * nums[i<sub>k</sub>​]</code>.</p>
# <p>Return <em>the maximum strength of a group the teacher can create</em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [3,-1,-5,2,5,-9]
# <strong>Output:</strong> 1350
# <strong>Explanation:</strong> One way to form a group of maximal strength is to group the students at indices [0,2,3,4,5]. Their strength is 3 * (-5) * 2 * 5 * (-9) = 1350, which we can show is optimal.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [-4,-5,-4]
# <strong>Output:</strong> 20
# <strong>Explanation:</strong> Group the students at indices [0, 1] . Then, we&rsquo;ll have a resulting strength of 20. We cannot achieve greater strength.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= nums.length &lt;= 13</code></li>
# 	<li><code>-9 &lt;= nums[i] &lt;= 9</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from typing import List


class Solution:
    def maxStrength(self, nums):
        negatives = []
        positives = []
        zeros = 0

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zeros += 1

        negatives.sort()
        product = 1

        if len(positives) == 0 and len(negatives) == 0:
            return 0

        if len(positives) == 0 and len(negatives) == 1 and zeros > 0:
            return 0

        if len(negatives) % 2 == 0:
            for num in negatives:
                product *= num
        else:
            if len(negatives) > 1:
                for i in range(len(negatives) - 1):
                    product *= negatives[i]
            else:
                if len(positives) == 0 and zeros > 0:
                    return 0
                else:
                    product = negatives[0]

        for num in positives:
            product *= num

        return product

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = random.choices(range(-9, 10), k=random.randint(1, 13))
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.maxStrength(nums)

    return nums, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, expected_result = generate_test_case()
        solution = Solution()
        assert solution.maxStrength(nums) == expected_result
        test_case_generator_results.append(f"assert solution.maxStrength({nums}) == {expected_result}") 
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  
    test_case_generator_results = test_generated_test_cases(num_tests)

# --------------------------------------
# Test Cases:
solution = Solution()
#assert solution.maxStrength([-3, 4]) == 4
assert solution.maxStrength([-8, -6, -2, -1, -1, 2, 3, 4, 6, 7]) == 96768
assert solution.maxStrength([-7, -5, -5, 3, 3, 7, 9, 9]) == 178605
assert solution.maxStrength([-9, -9, -6, -5, -1, 2, 2, 3, 9]) == 262440
assert solution.maxStrength([-9, -9, -6, -4, -2, 0, 0, 1, 4, 5, 6, 8]) == 1866240
#assert solution.maxStrength([-1, 3, 6, 8]) == 144
assert solution.maxStrength([-9, -5, -3, -2, 0, 1, 2, 6]) == 3240
assert solution.maxStrength([-5, -4, -3, -2, -1, 3, 3, 4, 6, 6, 7]) == 1088640
#assert solution.maxStrength([-8, 2, 5]) == 10
assert solution.maxStrength([-7, -5, -4, 1, 2, 2, 4, 4, 7, 8]) == 125440
assert solution.maxStrength([-8, -6, -3, -1, 1, 3, 4, 5, 7, 8]) == 483840
assert solution.maxStrength([-8, -7, -5, -2, 0, 1, 3, 5, 5, 7]) == 294000
#assert solution.maxStrength([-6, 0, 1, 2, 3, 3, 6, 6, 9]) == 5832
assert solution.maxStrength([-9, -9, -8, 0, 1, 1, 4, 4, 7, 8]) == 72576
assert solution.maxStrength([-4]) == -4
assert solution.maxStrength([-8]) == -8
assert solution.maxStrength([2]) == 2
assert solution.maxStrength([-9, -8, -8, -8, -6, -5, 3, 4, 4, 7, 8, 8, 9]) == 26754416640
assert solution.maxStrength([-9, -8, -5, -3, -2, -2, -1, 2, 4, 7, 9]) == 2177280
assert solution.maxStrength([0, 2, 6]) == 12
assert solution.maxStrength([-9, -8, -6, -5, -5, -2, -1, 0, 3, 7, 8]) == 3628800
assert solution.maxStrength([-9, -8, -5, -4, -4, -2, 1, 2, 5]) == 115200
assert solution.maxStrength([-9, -7, -5, -5, -3, -3, -3, -2, -2, 2, 5, 6, 9]) == 45927000
assert solution.maxStrength([-9, -8, -1, 0, 2, 2, 4, 6]) == 6912
assert solution.maxStrength([-8, -1, 5, 5, 6, 9]) == 10800
assert solution.maxStrength([-8, -6, -5, -4, -3, -2, 0, 1, 3, 7, 8, 8, 8]) == 61931520
assert solution.maxStrength([-8, -6, -5, -4, 4, 7, 7]) == 188160
assert solution.maxStrength([-9, -8, -6, 2, 3, 4, 5, 7]) == 60480
assert solution.maxStrength([-8, -7, -4, 1, 5, 9]) == 2520
assert solution.maxStrength([-5, -1, 1, 1, 1, 2, 2]) == 20
assert solution.maxStrength([-9, -8, -1, 3, 3, 8]) == 5184
assert solution.maxStrength([-9, -7, -6, -4, -2, -2, -1, 1, 2, 7, 9]) == 762048
assert solution.maxStrength([-7, -6, -5, 1, 2, 3, 5, 7, 8, 9]) == 635040
#assert solution.maxStrength([-9, 0, 3]) == 3
assert solution.maxStrength([-9, -8, -7, -3, 1, 1, 3, 5, 6]) == 136080
assert solution.maxStrength([-8, -7, 9]) == 504
assert solution.maxStrength([-7, -6, 5, 8]) == 1680
assert solution.maxStrength([-7, -7, -5, -4, -3, 0, 1, 2, 2, 3, 8, 9]) == 846720
assert solution.maxStrength([-7, -6, 4, 7]) == 1176
assert solution.maxStrength([-9, -6, -5, -2, 0, 6, 7, 8, 9, 9]) == 14696640
assert solution.maxStrength([-9, -3, -3, 0, 2, 4, 5, 6, 6, 6, 7, 8]) == 13063680
assert solution.maxStrength([-9, -4, -2, -1, 1, 1, 4, 4, 5, 5, 5, 7, 9]) == 9072000
assert solution.maxStrength([-7, -4, -2, -1]) == 56
assert solution.maxStrength([-9, -8, -8, -7, -5, -4, -4, -2, 0, 1, 5, 6, 7]) == 135475200
assert solution.maxStrength([-6, -4, 4, 7, 7]) == 4704
assert solution.maxStrength([-9, -7, -6, -1, 1, 3, 5, 7]) == 39690
assert solution.maxStrength([-9, -8, -5, -4, -4, -1, 1, 1, 2, 4, 4]) == 184320
assert solution.maxStrength([-8, -2, 0, 1, 3, 5, 9]) == 2160
assert solution.maxStrength([-8, -3, 0, 1, 5, 6, 8]) == 5760
assert solution.maxStrength([-7, -5, -4, 0, 2]) == 70
assert solution.maxStrength([-8, -4, 3]) == 96
assert solution.maxStrength([-8, -2, -2, 0, 0, 1, 3, 4, 5]) == 960
assert solution.maxStrength([-8, -8, -7, -2, -2, -2, -1, 2]) == 7168
assert solution.maxStrength([-7, -4, -3, 0, 3]) == 84
assert solution.maxStrength([-8, -5]) == 40
assert solution.maxStrength([-9, -5, -4, -3, -2, 2, 2, 3, 7, 7, 8, 8, 8]) == 162570240
assert solution.maxStrength([-8, -4, -3, -2, -1, 1, 2, 5, 8, 9]) == 138240
assert solution.maxStrength([-9, -3, -3, 9]) == 243
assert solution.maxStrength([-8, -6, -5, -4, 1, 9, 9]) == 77760
assert solution.maxStrength([5]) == 5
assert solution.maxStrength([-3]) == -3
assert solution.maxStrength([6]) == 6
assert solution.maxStrength([-4, -4, -4, -3, 3, 3, 4, 6, 6, 7, 7, 9, 9]) == 987614208
assert solution.maxStrength([-7, -5, -5, -4, -3, 2, 3, 5, 8]) == 168000
assert solution.maxStrength([-7, -5, 0, 0, 0, 3, 4, 9, 9, 9]) == 306180
assert solution.maxStrength([-4, -3, -1, 0, 0, 1, 5, 8]) == 480
assert solution.maxStrength([-9, -4, -4, -3, 3, 3, 4, 5, 7, 7]) == 3810240
assert solution.maxStrength([-5, -3, -2, -1, 4, 9]) == 1080
assert solution.maxStrength([-7, -7, -6, -5, -4, -4, -3, -2, -1, -1, 2, 5, 6]) == 8467200
assert solution.maxStrength([0, 0, 5, 5, 6, 6, 7, 9]) == 56700
assert solution.maxStrength([-9, -7, -6, -4, -3, 2, 6, 6, 9]) == 979776
assert solution.maxStrength([-8, -4, -1, 0, 1, 6, 9, 9, 9]) == 139968
assert solution.maxStrength([-6, -2, -1, 6]) == 72
assert solution.maxStrength([-9, -8, -5, -5, -1, 3, 4, 6]) == 129600
assert solution.maxStrength([-4, -3, 0, 2, 8]) == 192
assert solution.maxStrength([-9, -9, -8, -8, -8, -7, -7, -1, 3, 4, 7, 7, 9]) == 10754021376
assert solution.maxStrength([-5]) == -5
assert solution.maxStrength([-8, -5, -1, 0, 7]) == 280
assert solution.maxStrength([-9, -8, -8, -3, -3, -2, -1, 1, 1, 2, 6]) == 124416
assert solution.maxStrength([-9, -6, -4, -3, 0, 6]) == 3888
assert solution.maxStrength([-9, -7, -4, -2, -1, -1, 2, 6, 6, 7]) == 254016
assert solution.maxStrength([-6, -6, -5, -3, -2, 2, 6, 8, 9]) == 466560
#assert solution.maxStrength([-6, 0, 3, 7, 8, 8]) == 1344
assert solution.maxStrength([-9, -9, -9, -5, -5, -1, 2, 3, 3]) == 328050
assert solution.maxStrength([-7]) == -7
assert solution.maxStrength([-7, -6, -4, -4, -1, 3, 8]) == 16128
assert solution.maxStrength([0, 2, 5, 9]) == 90
assert solution.maxStrength([-7, -6, -5, -4, 5, 8]) == 33600
assert solution.maxStrength([2]) == 2
assert solution.maxStrength([-8, -5, -3, -3, 5, 9]) == 16200
assert solution.maxStrength([-7, -7, -6, -5, -1, 1, 2, 3]) == 8820
assert solution.maxStrength([-9, -8, -5, -3, 0, 4, 5, 5, 7, 7, 8, 8, 9]) == 3048192000
assert solution.maxStrength([-6, -4, -2, 2, 3, 3, 7, 9]) == 27216
assert solution.maxStrength([-8, -8, -4, -3, -3, -2, -2, 2, 5, 6, 8, 9]) == 19906560
assert solution.maxStrength([-7, -5, -3, -2, 1, 5]) == 1050
assert solution.maxStrength([-9, -3, -2, -1, 1, 1, 1, 2, 2, 3, 3, 4, 8]) == 62208
assert solution.maxStrength([-9, -6, -6, -6, -5, -4, 0, 0, 2, 3, 5, 7]) == 8164800
assert solution.maxStrength([-9]) == -9
assert solution.maxStrength([-6, -3, -1, 2, 6, 7]) == 1512
#assert solution.maxStrength([-1, 0, 0, 4]) == 4

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
