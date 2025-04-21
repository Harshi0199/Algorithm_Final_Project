# Problem 2141: Maximum Running Time of N Computers
# Difficulty: Hard
# Description:
# <p>You have <code>n</code> computers. You are given the integer <code>n</code> and a <strong>0-indexed</strong> integer array <code>batteries</code> where the <code>i<sup>th</sup></code> battery can <strong>run</strong> a computer for <code>batteries[i]</code> minutes. You are interested in running <strong>all</strong> <code>n</code> computers <strong>simultaneously</strong> using the given batteries.</p>
# <p>Initially, you can insert <strong>at most one battery</strong> into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery <strong>any number of times</strong>. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.</p>
# <p>Note that the batteries cannot be recharged.</p>
# <p>Return <em>the <strong>maximum</strong> number of minutes you can run all the </em><code>n</code><em> computers simultaneously.</em></p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2141.Maximum%20Running%20Time%20of%20N%20Computers/images/example1-fit.png" style="width: 762px; height: 150px;" />
# <pre>
# <strong>Input:</strong> n = 2, batteries = [3,3,3]
# <strong>Output:</strong> 4
# <strong>Explanation:</strong> 
# Initially, insert battery 0 into the first computer and battery 1 into the second computer.
# After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
# At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
# By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
# We can run the two computers simultaneously for at most 4 minutes, so we return 4.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/2100-2199/2141.Maximum%20Running%20Time%20of%20N%20Computers/images/example2.png" style="width: 629px; height: 150px;" />
# <pre>
# <strong>Input:</strong> n = 2, batteries = [1,1,1,1]
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> 
# Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
# After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
# After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
# We can run the two computers simultaneously for at most 2 minutes, so we return 2.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= n &lt;= batteries.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= batteries[i] &lt;= 10<sup>9</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, r = 0, sum(batteries)
        while l < r:
            mid = (l + r + 1) >> 1
            if sum(min(x, mid) for x in batteries) >= n * mid:
                l = mid
            else:
                r = mid - 1
        return l


def generate_test_case():
    solution = Solution()
    
    # Generate a random number of computers
    n = random.randint(1, 11)
    
    # Generate a random list of batteries with length n
    batteries = random.sample(range(1, 101), n)
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.maxRunTime(n, batteries)

    return n, batteries, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        n, batteries, expected_result = generate_test_case()
        solution = Solution()
        assert solution.maxRunTime(n, batteries) == expected_result
        print(f"assert solution.maxRunTime({n}, {batteries}) == {expected_result}")
        test_case_generator_results.append(f"assert solution.maxRunTime({n}, {batteries}) == {expected_result}")
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.maxRunTime(5, [39, 3, 24, 2, 1]) == 1
assert solution.maxRunTime(4, [96, 36, 27, 100]) == 27
assert solution.maxRunTime(3, [5, 77, 37]) == 5
assert solution.maxRunTime(7, [34, 57, 77, 30, 62, 58, 26]) == 26
assert solution.maxRunTime(1, [16]) == 16
assert solution.maxRunTime(5, [31, 51, 100, 82, 36]) == 31
assert solution.maxRunTime(3, [4, 41, 10]) == 4
assert solution.maxRunTime(11, [58, 82, 6, 2, 14, 74, 100, 94, 73, 55, 95]) == 2
assert solution.maxRunTime(11, [21, 83, 51, 72, 55, 64, 63, 41, 100, 12, 22]) == 12
assert solution.maxRunTime(5, [21, 57, 43, 58, 24]) == 21
assert solution.maxRunTime(9, [89, 65, 74, 11, 13, 90, 27, 99, 14]) == 11
assert solution.maxRunTime(9, [46, 78, 58, 45, 95, 88, 12, 73, 29]) == 12
assert solution.maxRunTime(5, [30, 91, 68, 97, 8]) == 8
assert solution.maxRunTime(11, [23, 75, 5, 55, 60, 41, 4, 13, 84, 54, 67]) == 4
assert solution.maxRunTime(9, [84, 76, 95, 67, 24, 64, 91, 14, 16]) == 14
assert solution.maxRunTime(6, [70, 24, 2, 71, 84, 49]) == 2
assert solution.maxRunTime(4, [63, 31, 86, 20]) == 20
assert solution.maxRunTime(6, [39, 2, 20, 76, 99, 51]) == 2
assert solution.maxRunTime(1, [39]) == 39
assert solution.maxRunTime(1, [35]) == 35
assert solution.maxRunTime(6, [78, 99, 83, 3, 80, 49]) == 3
assert solution.maxRunTime(6, [82, 80, 85, 30, 40, 50]) == 30
assert solution.maxRunTime(6, [58, 24, 25, 43, 99, 33]) == 24
assert solution.maxRunTime(5, [29, 90, 100, 25, 51]) == 25
assert solution.maxRunTime(7, [64, 92, 16, 22, 35, 69, 8]) == 8
assert solution.maxRunTime(5, [97, 99, 50, 100, 46]) == 46
assert solution.maxRunTime(10, [90, 73, 17, 13, 3, 77, 38, 98, 2, 93]) == 2
assert solution.maxRunTime(11, [18, 86, 34, 88, 6, 77, 98, 12, 31, 24, 58]) == 6
assert solution.maxRunTime(3, [37, 88, 75]) == 37
assert solution.maxRunTime(5, [69, 82, 62, 88, 55]) == 55
assert solution.maxRunTime(11, [84, 43, 71, 81, 21, 31, 90, 30, 7, 26, 37]) == 7
assert solution.maxRunTime(7, [75, 10, 78, 81, 19, 45, 16]) == 10
assert solution.maxRunTime(5, [16, 96, 30, 15, 6]) == 6
assert solution.maxRunTime(6, [10, 43, 87, 39, 88, 19]) == 10
assert solution.maxRunTime(8, [90, 79, 56, 4, 37, 97, 46, 21]) == 4
assert solution.maxRunTime(9, [22, 20, 7, 93, 98, 30, 76, 27, 44]) == 7
assert solution.maxRunTime(1, [11]) == 11
assert solution.maxRunTime(3, [100, 10, 20]) == 10
assert solution.maxRunTime(8, [60, 39, 57, 9, 41, 54, 72, 42]) == 9
assert solution.maxRunTime(7, [5, 55, 86, 63, 68, 27, 79]) == 5
assert solution.maxRunTime(8, [79, 45, 51, 36, 85, 42, 21, 69]) == 21
assert solution.maxRunTime(10, [79, 29, 30, 64, 15, 35, 89, 19, 60, 92]) == 15
assert solution.maxRunTime(7, [90, 95, 48, 3, 12, 9, 70]) == 3
assert solution.maxRunTime(8, [82, 45, 44, 67, 73, 98, 1, 40]) == 1
assert solution.maxRunTime(8, [35, 93, 78, 3, 92, 57, 13, 97]) == 3
assert solution.maxRunTime(4, [47, 63, 2, 41]) == 2
assert solution.maxRunTime(3, [28, 76, 13]) == 13
assert solution.maxRunTime(11, [77, 61, 95, 42, 45, 17, 88, 70, 11, 87, 82]) == 11
assert solution.maxRunTime(10, [7, 2, 11, 89, 20, 17, 58, 75, 14, 59]) == 2
assert solution.maxRunTime(3, [24, 30, 87]) == 24
assert solution.maxRunTime(5, [42, 38, 19, 43, 14]) == 14
assert solution.maxRunTime(1, [52]) == 52
assert solution.maxRunTime(9, [81, 46, 53, 58, 44, 3, 52, 37, 65]) == 3
assert solution.maxRunTime(9, [72, 97, 50, 49, 23, 21, 10, 59, 60]) == 10
assert solution.maxRunTime(5, [80, 90, 47, 77, 62]) == 47
assert solution.maxRunTime(9, [19, 92, 95, 11, 29, 88, 74, 16, 15]) == 11
assert solution.maxRunTime(6, [4, 84, 45, 19, 14, 79]) == 4
assert solution.maxRunTime(11, [6, 22, 71, 94, 16, 91, 76, 34, 46, 53, 39]) == 6
assert solution.maxRunTime(11, [69, 78, 59, 56, 86, 28, 88, 34, 13, 55, 1]) == 1
assert solution.maxRunTime(8, [63, 21, 65, 42, 25, 40, 7, 56]) == 7
assert solution.maxRunTime(1, [70]) == 70
assert solution.maxRunTime(8, [15, 33, 78, 98, 71, 29, 22, 52]) == 15
assert solution.maxRunTime(2, [13, 56]) == 13
assert solution.maxRunTime(1, [6]) == 6
assert solution.maxRunTime(7, [45, 86, 60, 39, 93, 9, 46]) == 9
assert solution.maxRunTime(5, [31, 54, 9, 45, 63]) == 9
assert solution.maxRunTime(11, [32, 20, 78, 13, 69, 15, 14, 52, 61, 39, 84]) == 13
assert solution.maxRunTime(8, [8, 66, 15, 88, 23, 63, 40, 17]) == 8
assert solution.maxRunTime(3, [22, 36, 41]) == 22
assert solution.maxRunTime(5, [94, 84, 10, 32, 1]) == 1
assert solution.maxRunTime(11, [66, 92, 28, 58, 63, 62, 95, 25, 7, 20, 77]) == 7
assert solution.maxRunTime(2, [70, 97]) == 70
assert solution.maxRunTime(1, [86]) == 86
assert solution.maxRunTime(10, [72, 88, 71, 11, 38, 36, 57, 60, 45, 100]) == 11
assert solution.maxRunTime(1, [80]) == 80
assert solution.maxRunTime(8, [97, 84, 55, 62, 73, 80, 79, 51]) == 51
assert solution.maxRunTime(8, [34, 98, 76, 96, 22, 23, 89, 79]) == 22
assert solution.maxRunTime(7, [15, 49, 59, 69, 26, 2, 65]) == 2
assert solution.maxRunTime(10, [44, 37, 96, 91, 98, 48, 1, 36, 9, 3]) == 1
assert solution.maxRunTime(6, [10, 91, 54, 42, 87, 89]) == 10
assert solution.maxRunTime(6, [90, 86, 7, 18, 73, 21]) == 7
assert solution.maxRunTime(1, [55]) == 55
assert solution.maxRunTime(1, [85]) == 85
assert solution.maxRunTime(9, [21, 47, 99, 87, 39, 55, 68, 5, 4]) == 4
assert solution.maxRunTime(4, [99, 83, 37, 92]) == 37
assert solution.maxRunTime(5, [81, 19, 25, 93, 54]) == 19
assert solution.maxRunTime(6, [17, 97, 60, 33, 72, 13]) == 13
assert solution.maxRunTime(3, [64, 72, 60]) == 60
assert solution.maxRunTime(6, [77, 54, 42, 95, 85, 75]) == 42
assert solution.maxRunTime(8, [90, 23, 37, 42, 27, 61, 4, 99]) == 4
assert solution.maxRunTime(3, [80, 3, 54]) == 3
assert solution.maxRunTime(2, [57, 32]) == 32
assert solution.maxRunTime(8, [7, 70, 96, 92, 20, 13, 2, 43]) == 2
assert solution.maxRunTime(6, [86, 31, 12, 52, 43, 45]) == 12
assert solution.maxRunTime(1, [83]) == 83
assert solution.maxRunTime(8, [58, 63, 27, 76, 69, 34, 45, 25]) == 25
assert solution.maxRunTime(8, [31, 78, 63, 59, 41, 3, 30, 55]) == 3
assert solution.maxRunTime(8, [42, 61, 70, 66, 57, 17, 81, 22]) == 17
assert solution.maxRunTime(5, [99, 6, 35, 50, 95]) == 6
assert solution.maxRunTime(4, [25, 42, 87, 40]) == 25

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
