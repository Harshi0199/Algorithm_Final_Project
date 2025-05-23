# Problem 2448: Minimum Cost to Make Array Equal
# Difficulty: Hard
# Description:
# <p>You are given two <strong>0-indexed</strong> arrays <code>nums</code> and <code>cost</code> consisting each of <code>n</code> <strong>positive</strong> integers.</p>
# <p>You can do the following operation <strong>any</strong> number of times:</p>
# <ul>
# 	<li>Increase or decrease <strong>any</strong> element of the array <code>nums</code> by <code>1</code>.</li>
# </ul>
# <p>The cost of doing one operation on the <code>i<sup>th</sup></code> element is <code>cost[i]</code>.</p>
# <p>Return <em>the <strong>minimum</strong> total cost such that all the elements of the array </em><code>nums</code><em> become <strong>equal</strong></em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [1,3,5,2], cost = [2,3,1,14]
# <strong>Output:</strong> 8
# <strong>Explanation:</strong> We can make all the elements equal to 2 in the following way:
# - Increase the 0<sup>th</sup> element one time. The cost is 2.
# - Decrease the 1<sup><span style="font-size: 10.8333px;">st</span></sup> element one time. The cost is 3.
# - Decrease the 2<sup>nd</sup> element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# <strong>Output:</strong> 0
# <strong>Explanation:</strong> All the elements are already equal, so no operations are needed.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>n == nums.length == cost.length</code></li>
# 	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
# 	<li><code>1 &lt;= nums[i], cost[i] &lt;= 10<sup>6</sup></code></li>
# 	<li>Test cases are generated in a way that the output doesn&#39;t exceed&nbsp;2<sup>53</sup>-1</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def minCost(self, nums, cost):
        arr = sorted(zip(nums, cost))
        n = len(arr)
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i in range(1, n + 1):
            a, b = arr[i - 1]
            f[i] = f[i - 1] + a * b
            g[i] = g[i - 1] + b
        ans = float('inf')
        for i in range(1, n + 1):
            a = arr[i - 1][0]
            l = a * g[i - 1] - f[i - 1]
            r = f[n] - f[i] - a * (g[n] - g[i])
            ans = min(ans, l + r)
        return ans

def generate_test_case():
    solution = Solution()
    
    # Generate random numbers list
    nums = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
    
    # Generate random cost list
    cost = [random.randint(1, 100) for _ in range(len(nums))]

    # Calculate the expected result using the provided Solution class
    expected_result = solution.minCost(nums, cost)

    return nums, cost, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, cost, expected_result = generate_test_case()
        solution = Solution()
        assert solution.minCost(nums, cost) == expected_result
        print(f"assert solution.minCost({nums}, {cost}) == {expected_result}")
        test_case_generator_results.append("assert solution.minCost({}, {}) == {}".format(nums, cost, expected_result))
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.minCost([99, 12, 78, 54, 58, 7, 99, 3], [53, 42, 30, 45, 4, 34, 54, 48]) == 11361
assert solution.minCost([53, 54, 99, 78, 19, 75], [6, 36, 31, 57, 84, 93]) == 6507
assert solution.minCost([12, 58, 1, 83], [24, 37, 86, 11]) == 3275
assert solution.minCost([45], [21]) == 0
assert solution.minCost([100], [76]) == 0
assert solution.minCost([85, 30, 18, 79, 55], [70, 70, 15, 63, 81]) == 5917
assert solution.minCost([42], [13]) == 0
assert solution.minCost([35, 10, 48, 48], [4, 39, 1, 69]) == 1534
assert solution.minCost([43, 9, 86, 60, 44, 98, 5, 4, 27, 66], [79, 90, 25, 72, 25, 4, 22, 75, 29, 13]) == 10128
assert solution.minCost([46, 34, 55, 49, 64, 26], [63, 43, 22, 26, 100, 42]) == 3432
assert solution.minCost([64, 3, 58, 23, 20, 16, 57, 35], [76, 76, 75, 64, 58, 55, 99, 74]) == 11222
assert solution.minCost([70], [59]) == 0
assert solution.minCost([91, 65, 88, 41, 40, 64, 35, 37, 32], [56, 37, 54, 65, 56, 9, 16, 14, 20]) == 6821
assert solution.minCost([63, 100, 24, 96, 55, 39, 100], [3, 91, 43, 68, 16, 3, 21]) == 4470
assert solution.minCost([49, 64, 97, 46, 87, 38, 87, 9, 73, 6], [78, 23, 61, 98, 51, 1, 93, 82, 43, 62]) == 16028
assert solution.minCost([28, 54, 95], [90, 72, 94]) == 6194
assert solution.minCost([46, 89, 81, 82, 54, 23, 7], [47, 84, 1, 12, 96, 33, 6]) == 4984
assert solution.minCost([39, 50, 94, 83, 58, 15], [65, 10, 61, 69, 51, 90]) == 9106
assert solution.minCost([91, 67, 66], [8, 68, 10]) == 202
assert solution.minCost([69, 54, 61, 22, 98, 49, 35, 63, 32], [22, 20, 10, 76, 71, 43, 89, 4, 48]) == 7707
assert solution.minCost([80, 44, 14, 20, 45, 19, 16, 46], [56, 23, 21, 19, 63, 67, 41, 2]) == 5896
assert solution.minCost([78, 89, 9, 84, 16, 89], [15, 77, 68, 56, 45, 98]) == 9125
assert solution.minCost([23, 67, 95], [62, 6, 19]) == 1632
assert solution.minCost([73, 54, 53, 94, 67, 31, 28, 27, 22], [44, 59, 76, 27, 24, 25, 92, 84, 60]) == 8594
assert solution.minCost([93, 57, 95, 71, 39, 46, 83], [33, 28, 5, 51, 27, 95, 77]) == 5401
assert solution.minCost([7, 53, 32], [45, 24, 39]) == 1629
assert solution.minCost([52], [58]) == 0
assert solution.minCost([68, 53, 86, 77, 10, 22, 37, 7], [100, 43, 24, 57, 23, 13, 66, 45]) == 8178
assert solution.minCost([45, 13, 70, 100], [37, 77, 1, 12]) == 2285
assert solution.minCost([35, 43, 36, 58, 88, 51, 15], [42, 30, 74, 19, 86, 22, 27]) == 5941
assert solution.minCost([100, 96, 74, 39], [4, 35, 39, 66]) == 3184
assert solution.minCost([19, 77, 29, 28, 48], [4, 8, 38, 59, 22]) == 901
assert solution.minCost([27, 78], [32, 61]) == 1632
assert solution.minCost([5, 63, 4], [66, 10, 81]) == 656
assert solution.minCost([32, 28, 32, 2, 49, 9, 26, 73], [65, 83, 22, 71, 27, 24, 26, 96]) == 7565
assert solution.minCost([94, 65, 52, 16, 17], [35, 63, 45, 35, 42]) == 5019
assert solution.minCost([27, 80, 60, 4, 2], [96, 44, 13, 59, 63]) == 5693
assert solution.minCost([24, 61, 59, 5, 28, 66, 77, 63, 10, 63], [84, 19, 16, 2, 12, 55, 82, 84, 75, 41]) == 9202
assert solution.minCost([27, 34, 51], [61, 90, 80]) == 1787
assert solution.minCost([11, 64, 20, 32, 27, 2, 96, 25], [46, 52, 72, 19, 59, 85, 11, 55]) == 5984
assert solution.minCost([53], [23]) == 0
assert solution.minCost([79, 21], [1, 32]) == 58
assert solution.minCost([38], [9]) == 0
assert solution.minCost([25, 26, 39, 57, 4, 94], [70, 67, 17, 91, 72, 69]) == 9388
assert solution.minCost([46], [85]) == 0
assert solution.minCost([3, 13, 90, 12, 98, 62, 6, 48, 5, 70], [72, 54, 78, 25, 44, 66, 65, 43, 33, 1]) == 16006
assert solution.minCost([58, 76, 35], [98, 11, 1]) == 221
assert solution.minCost([32, 23, 83, 82, 8, 18], [59, 46, 65, 87, 97, 25]) == 10757
assert solution.minCost([28], [8]) == 0
assert solution.minCost([24, 42, 29], [48, 94, 80]) == 1462
assert solution.minCost([83, 26], [75, 4]) == 228
assert solution.minCost([99, 5, 31, 21], [55, 16, 35, 97]) == 4896
assert solution.minCost([76, 87, 76, 16, 63, 79], [90, 29, 63, 1, 53, 75]) == 1293
assert solution.minCost([49, 46, 85, 70, 86, 64, 16, 90], [34, 98, 47, 13, 37, 37, 9, 77]) == 6587
assert solution.minCost([19, 85, 81, 87, 31, 87], [73, 67, 59, 6, 95, 16]) == 8676
assert solution.minCost([62], [55]) == 0
assert solution.minCost([26, 68, 49, 94], [48, 69, 6, 33]) == 2988
assert solution.minCost([63, 78, 24, 65, 11, 10], [3, 56, 79, 56, 48, 97]) == 7419
assert solution.minCost([1, 13, 64], [60, 53, 38]) == 2658
assert solution.minCost([76, 48, 34, 44, 55], [29, 99, 31, 53, 17]) == 1577
assert solution.minCost([84, 7], [92, 67]) == 5159
assert solution.minCost([77, 28, 92, 49, 41], [70, 47, 17, 88, 3]) == 3702
assert solution.minCost([58, 65, 76, 10, 44, 29, 43, 70], [60, 19, 43, 87, 42, 38, 46, 82]) == 8321
assert solution.minCost([39, 10], [50, 47]) == 1363
assert solution.minCost([27], [28]) == 0
assert solution.minCost([48, 76, 64, 81, 7, 43, 72, 62], [42, 70, 13, 22, 74, 14, 16, 7]) == 6480
assert solution.minCost([19, 59, 52, 47, 16], [86, 1, 6, 72, 64]) == 2446
assert solution.minCost([18, 94, 43, 4, 52, 52, 92, 46, 5, 46], [24, 96, 73, 55, 92, 51, 66, 15, 94, 19]) == 15407
assert solution.minCost([50, 67, 2, 4, 8, 41], [55, 100, 95, 75, 28, 78]) == 10499
assert solution.minCost([67, 31, 12, 49, 78, 40], [98, 93, 90, 79, 84, 16]) == 9348
assert solution.minCost([64, 25, 51, 43, 82, 48, 51], [85, 39, 11, 50, 26, 5, 72]) == 3340
assert solution.minCost([53, 16, 25, 13, 85, 96, 1, 75, 52, 37], [100, 43, 96, 28, 64, 19, 54, 28, 58, 91]) == 12398
assert solution.minCost([95, 97], [34, 80]) == 68
assert solution.minCost([41], [12]) == 0
assert solution.minCost([16, 27, 37, 14], [1, 55, 89, 5]) == 686
assert solution.minCost([16, 68, 55, 52, 38, 57, 30, 40], [45, 96, 29, 78, 60, 70, 66, 86]) == 6917
assert solution.minCost([20, 55, 66, 17, 34, 79, 93, 21, 48], [11, 42, 18, 97, 85, 85, 10, 27, 95]) == 8937
assert solution.minCost([65, 39, 43], [71, 68, 10]) == 1834
assert solution.minCost([37], [20]) == 0
assert solution.minCost([17, 3, 13, 4, 15, 19, 32], [20, 12, 95, 96, 39, 63, 53]) == 2527
assert solution.minCost([77, 51, 52, 76], [36, 90, 100, 92]) == 3198
assert solution.minCost([76, 34, 37, 74, 68], [89, 62, 67, 47, 4]) == 5161
assert solution.minCost([42, 89, 85], [9, 75, 100]) == 687
assert solution.minCost([18, 19, 83, 45, 37], [35, 64, 48, 19, 84]) == 4177
assert solution.minCost([70, 2, 9, 39, 68, 62], [21, 93, 2, 64, 92, 95]) == 7878
assert solution.minCost([40, 85, 36, 7, 51, 15, 45, 50, 4, 51], [49, 44, 73, 92, 45, 76, 100, 83, 61, 68]) == 11977
assert solution.minCost([96, 2, 72, 88, 58, 23, 45, 9, 2], [46, 9, 43, 85, 79, 32, 97, 100, 7]) == 13077
assert solution.minCost([39, 78, 89, 72, 65], [57, 83, 50, 12, 13]) == 3014
assert solution.minCost([31], [33]) == 0
assert solution.minCost([1, 29], [31, 47]) == 868
assert solution.minCost([44, 93, 51, 29, 69, 43], [26, 46, 6, 77, 76, 5]) == 5072
assert solution.minCost([29, 17, 40], [43, 69, 53]) == 1411
assert solution.minCost([17, 56], [83, 81]) == 3159
assert solution.minCost([84, 96, 18], [20, 99, 49]) == 4062
assert solution.minCost([22], [36]) == 0
assert solution.minCost([22, 52, 5], [58, 3, 69]) == 1127
assert solution.minCost([26, 38, 19, 39], [47, 96, 89, 4]) == 1827
assert solution.minCost([13, 11, 78, 79, 78], [10, 73, 95, 74, 46]) == 5615
assert solution.minCost([48, 54, 43, 88, 95], [27, 16, 63, 45, 20]) == 3151
assert solution.minCost([95, 95, 54], [11, 84, 75]) == 3075

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
