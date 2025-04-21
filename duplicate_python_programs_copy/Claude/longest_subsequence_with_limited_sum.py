# Problem 2389: Longest Subsequence With Limited Sum
# Difficulty: Easy
# Description:
# <p>You are given an integer array <code>nums</code> of length <code>n</code>, and an integer array <code>queries</code> of length <code>m</code>.</p>
# <p>Return <em>an array </em><code>answer</code><em> of length </em><code>m</code><em> where </em><code>answer[i]</code><em> is the <strong>maximum</strong> size of a <strong>subsequence</strong> that you can take from </em><code>nums</code><em> such that the <strong>sum</strong> of its elements is less than or equal to </em><code>queries[i]</code>.</p>
# <p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [4,5,2,1], queries = [3,10,21]
# <strong>Output:</strong> [2,3,4]
# <strong>Explanation:</strong> We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [2,3,4,5], queries = [1]
# <strong>Output:</strong> [0]
# <strong>Explanation:</strong> The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.</pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>n == nums.length</code></li>
# 	<li><code>m == queries.length</code></li>
# 	<li><code>1 &lt;= n, m &lt;= 1000</code></li>
# 	<li><code>1 &lt;= nums[i], queries[i] &lt;= 10<sup>6</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Sort nums in ascending order
        nums.sort()
        
        # Calculate prefix sum array
        prefix_sums = []
        current_sum = 0
        for num in nums:
            current_sum += num
            prefix_sums.append(current_sum)
        
        # Process each query
        result = []
        for query in queries:
            # Binary search to find the largest index where prefix_sum <= query
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] <= query:
                    index = mid
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Add one to the index to get the length of the subsequence
            # If index is -1, no elements can be included
            result.append(index + 1)
        
        return result

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.answerQueries([9, 12, 13, 23, 23, 24, 42, 47, 54, 91], [26, 90, 87, 47]) == [2, 5, 5, 3]
assert solution.answerQueries([43, 54, 69], [98, 90, 72, 57]) == [2, 1, 1, 1]
assert solution.answerQueries([32, 37, 40, 86], [82]) == [2]
assert solution.answerQueries([11, 12, 24, 26, 27, 60, 76, 76, 96, 96], [40, 57]) == [2, 3]
assert solution.answerQueries([9, 9, 21, 64, 69, 74, 90, 95, 97], [52, 58]) == [3, 3]
assert solution.answerQueries([5, 7, 7, 14, 27, 28, 36, 39, 90, 96], [64, 2, 18, 4, 73]) == [5, 0, 2, 0, 5]
assert solution.answerQueries([10, 17, 24, 33, 40, 67, 71, 88, 98], [79, 53, 7]) == [3, 3, 0]
assert solution.answerQueries([36, 59, 91], [92, 98, 1]) == [1, 2, 0]
assert solution.answerQueries([25, 46, 46, 49, 78], [75, 58, 99, 97]) == [2, 1, 2, 2]
assert solution.answerQueries([51, 90], [39, 95, 17]) == [0, 1, 0]
assert solution.answerQueries([2, 10, 33, 47, 75, 79, 85, 85], [10, 71, 87, 41]) == [1, 3, 3, 2]
assert solution.answerQueries([1, 4, 9, 17, 86, 92, 99], [20, 18]) == [3, 3]
assert solution.answerQueries([16, 17, 22, 25, 35, 45], [91]) == [4]
assert solution.answerQueries([1, 6, 50, 72, 74, 84, 89, 95, 98], [37]) == [2]
assert solution.answerQueries([4, 14, 24, 27, 31, 70, 70, 71, 85, 85], [34, 98]) == [2, 4]
assert solution.answerQueries([1, 15, 37, 57, 86, 87, 92], [97, 29]) == [3, 2]
assert solution.answerQueries([7, 20, 26, 33, 51, 52, 56, 61, 63, 90], [36]) == [2]
assert solution.answerQueries([1, 1, 7, 26, 33, 80, 91], [75, 13]) == [5, 3]
assert solution.answerQueries([25, 82, 87, 92], [80]) == [1]
assert solution.answerQueries([8, 8, 20, 40, 62, 70, 71, 83], [12, 19]) == [1, 2]
assert solution.answerQueries([31, 51, 55, 56, 83, 86, 88, 97], [31, 56]) == [1, 1]
assert solution.answerQueries([4, 31, 50, 60], [91, 73, 99, 35, 49]) == [3, 2, 3, 2, 2]
assert solution.answerQueries([5, 16, 34, 50, 69, 70, 79, 82, 86], [16, 72, 30, 58]) == [1, 3, 2, 3]
assert solution.answerQueries([18, 37, 51, 97], [11, 59]) == [0, 2]
assert solution.answerQueries([78, 89, 96], [38, 58, 53, 25, 26]) == [0, 0, 0, 0, 0]
assert solution.answerQueries([1, 6, 17, 33, 35, 55, 57, 57, 74], [55, 1, 11, 16]) == [3, 1, 2, 2]
assert solution.answerQueries([2, 10, 20, 21, 34, 57, 72, 82, 97], [31]) == [2]
assert solution.answerQueries([49, 53, 54], [59]) == [1]
assert solution.answerQueries([15, 16, 18, 37, 55, 58, 65, 88], [92, 1, 87]) == [4, 0, 4]
assert solution.answerQueries([14, 17, 31, 36, 54, 84, 87, 89, 91], [71, 30]) == [3, 1]
assert solution.answerQueries([5, 13, 14, 17, 49, 55, 76, 79], [79, 12]) == [4, 1]
assert solution.answerQueries([7, 72], [42, 72, 71, 88, 6]) == [1, 1, 1, 2, 0]
assert solution.answerQueries([30, 40, 60, 62, 91], [11]) == [0]
assert solution.answerQueries([55, 69], [78, 48, 70, 87]) == [1, 0, 1, 1]
assert solution.answerQueries([3, 43, 67, 77, 80], [94, 70, 95, 57, 70]) == [2, 2, 2, 2, 2]
assert solution.answerQueries([8, 24, 32, 88], [59, 10, 2, 54]) == [2, 1, 0, 2]
assert solution.answerQueries([3, 26, 44, 60, 68, 75], [94]) == [3]
assert solution.answerQueries([7, 8, 28, 45, 48, 71], [89, 75, 70, 93]) == [4, 3, 3, 4]
assert solution.answerQueries([1, 9, 49, 62, 79, 96], [71, 50, 64, 50]) == [3, 2, 3, 2]
assert solution.answerQueries([4, 13, 17, 35, 53, 76, 86, 95, 96, 98], [48, 9, 64, 56]) == [3, 1, 3, 3]
assert solution.answerQueries([13, 13, 46, 52], [79]) == [3]
assert solution.answerQueries([2, 4, 30, 53, 55, 68, 71, 94, 99], [2, 23, 63]) == [1, 2, 3]
assert solution.answerQueries([5, 13, 27, 28, 32, 57, 80, 86, 94, 99], [50, 74, 23, 85, 33]) == [3, 4, 2, 4, 2]
assert solution.answerQueries([5, 19, 36, 79, 82, 87], [42, 60, 89, 7]) == [2, 3, 3, 1]
assert solution.answerQueries([17, 22, 61, 67, 97], [69, 86, 82, 91, 5]) == [2, 2, 2, 2, 0]
assert solution.answerQueries([17, 54, 58, 73, 87], [85, 67, 35, 15]) == [2, 1, 1, 0]
assert solution.answerQueries([25, 39, 46, 61, 64, 86, 94], [93, 57, 99, 69]) == [2, 1, 2, 2]
assert solution.answerQueries([17, 20, 32, 32, 52, 82, 87], [47, 60, 46, 63]) == [2, 2, 2, 2]
assert solution.answerQueries([68, 72, 80, 85], [64, 14, 24, 4]) == [0, 0, 0, 0]
assert solution.answerQueries([11, 73], [44, 56, 52, 77, 35]) == [1, 1, 1, 1, 1]
assert solution.answerQueries([5, 10, 17, 39, 53, 75, 81, 93], [98]) == [4]
assert solution.answerQueries([6, 26, 30, 36, 38, 71, 75, 97], [11, 73, 82, 96, 33]) == [1, 3, 3, 3, 2]
assert solution.answerQueries([7, 17, 95], [61, 67, 7, 38]) == [2, 2, 1, 2]
assert solution.answerQueries([31, 64], [8, 28, 35, 55]) == [0, 0, 1, 1]
assert solution.answerQueries([4, 8, 47, 54], [99, 16]) == [3, 2]
assert solution.answerQueries([14, 14, 19, 29, 35, 64, 65, 79, 79, 81], [79, 78, 4]) == [4, 4, 0]
assert solution.answerQueries([6, 22, 23, 27, 34, 36, 43, 53, 70], [10, 99, 78]) == [1, 4, 4]
assert solution.answerQueries([16, 23, 26, 26, 38, 51, 54, 60], [46, 11, 77, 43]) == [2, 0, 3, 2]
assert solution.answerQueries([3, 8, 16, 46, 71], [52]) == [3]
assert solution.answerQueries([4, 7, 39, 47, 50, 63, 69], [34, 79, 31]) == [2, 3, 2]
assert solution.answerQueries([24, 49], [41, 56, 53, 20]) == [1, 1, 1, 0]
assert solution.answerQueries([2, 4, 32, 51, 54, 78, 88, 95], [34]) == [2]
assert solution.answerQueries([9, 35, 53, 63, 77, 79, 86, 88], [52, 67]) == [2, 2]
assert solution.answerQueries([13, 30, 40, 52, 53, 54, 67, 81], [23, 51, 21, 50]) == [1, 2, 1, 2]
assert solution.answerQueries([36, 40, 67, 68, 71], [97, 63, 40, 20]) == [2, 1, 1, 0]
assert solution.answerQueries([7, 26, 30, 43, 46, 53, 79, 87, 87, 89], [24, 12, 61, 70]) == [1, 1, 2, 3]
assert solution.answerQueries([10, 24, 28, 52, 59, 59, 71, 87], [70]) == [3]
assert solution.answerQueries([42, 59, 78], [37]) == [0]
assert solution.answerQueries([10, 38, 41, 42, 54, 68, 81, 84], [12, 84, 73]) == [1, 2, 2]
assert solution.answerQueries([7, 23, 53, 87, 94], [33, 85]) == [2, 3]
assert solution.answerQueries([25, 45, 69, 79, 81, 91], [72, 55]) == [2, 1]
assert solution.answerQueries([13, 35, 69], [33, 4]) == [1, 0]
assert solution.answerQueries([7, 14, 25, 40, 42, 59, 61, 80], [14, 28, 15]) == [1, 2, 1]
assert solution.answerQueries([49, 54, 55, 63, 96], [49]) == [1]
assert solution.answerQueries([8, 11, 24, 60, 67, 89, 89, 97, 99, 99], [23, 21, 71]) == [2, 2, 3]
assert solution.answerQueries([11, 11, 14, 45, 48, 91], [38, 1]) == [3, 0]
assert solution.answerQueries([63, 70, 73, 79, 80, 88, 99], [89, 92, 55]) == [1, 1, 0]
assert solution.answerQueries([10, 15, 35, 36, 62, 87, 98], [62, 83, 60]) == [3, 3, 3]
assert solution.answerQueries([19, 20, 32, 41, 41, 59], [32, 93, 19, 25]) == [1, 3, 1, 1]
assert solution.answerQueries([25, 97], [26, 3, 38, 60]) == [1, 0, 1, 1]
assert solution.answerQueries([11, 15, 16, 26, 55, 97], [77, 99]) == [4, 4]
assert solution.answerQueries([11, 50, 62, 67, 77, 96], [73, 89, 82, 72]) == [2, 2, 2, 2]
assert solution.answerQueries([9, 38, 71, 77, 86], [56]) == [2]
assert solution.answerQueries([20, 28, 30, 37, 52, 60], [52]) == [2]
assert solution.answerQueries([6, 55, 69], [55, 64]) == [1, 2]
assert solution.answerQueries([9, 39, 40, 50, 63, 64, 71, 73], [67]) == [2]
assert solution.answerQueries([16, 43, 56, 76, 91, 95, 96], [72, 94, 30, 63]) == [2, 2, 1, 2]
assert solution.answerQueries([18, 32, 36, 55, 58, 74, 86], [39, 21]) == [1, 1]
assert solution.answerQueries([7, 13, 31, 32, 39, 72, 75, 83], [2]) == [0]
assert solution.answerQueries([8, 17, 56, 93], [9, 29]) == [1, 2]
assert solution.answerQueries([3, 25, 82], [46]) == [2]
assert solution.answerQueries([5, 13, 47, 56, 79], [6, 9]) == [1, 1]
assert solution.answerQueries([21, 23, 25, 46, 52, 55, 61, 69], [66, 76, 28, 34, 85]) == [2, 3, 1, 1, 3]
assert solution.answerQueries([2, 7, 15, 30, 40, 43, 54, 83, 83], [8, 65, 87]) == [1, 4, 4]
assert solution.answerQueries([21, 37, 38, 66, 72, 76, 90], [69, 62]) == [2, 2]
assert solution.answerQueries([34, 44, 55, 56, 57, 58, 65, 68, 85, 93], [79, 45]) == [2, 1]
assert solution.answerQueries([18, 30, 73, 80, 88, 89, 98], [91]) == [2]
assert solution.answerQueries([6, 24, 27, 45, 50, 57, 97], [80, 96]) == [3, 3]
assert solution.answerQueries([3, 17, 35, 56, 85, 99], [58, 56, 51, 16]) == [3, 3, 2, 1]
assert solution.answerQueries([22, 55, 74, 90], [77, 56]) == [2, 1]

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass