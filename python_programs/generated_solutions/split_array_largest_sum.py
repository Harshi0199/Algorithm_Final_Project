# Problem 410: Split Array Largest Sum
# Difficulty: Hard
# Description:
# <p>Given an integer array <code>nums</code> and an integer <code>k</code>, split <code>nums</code> into <code>k</code> non-empty subarrays such that the largest sum of any subarray is <strong>minimized</strong>.</p>
# <p>Return <em>the minimized largest sum of the split</em>.</p>
# <p>A <strong>subarray</strong> is a contiguous part of the array.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [7,2,5,10,8], k = 2
# <strong>Output:</strong> 18
# <strong>Explanation:</strong> There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> nums = [1,2,3,4,5], k = 2
# <strong>Output:</strong> 9
# <strong>Explanation:</strong> There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
# 	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
# 	<li><code>1 &lt;= k &lt;= min(50, nums.length)</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
from bisect import bisect_left
import random

class Solution:
    def splitArray(self, nums, k):
        def check(mx):
            s, cnt = float('inf'), 0
            for x in nums:
                s += x
                if s > mx:
                    s = x
                    cnt += 1
            return cnt <= k

        left, right = max(nums), sum(nums)
        return left + bisect_left(range(left, right + 1), True, key=check)


def generate_test_case():
    solution = Solution()

    # Generate random numbers list
    nums = random.sample(range(1, 1001), random.randint(1, 10))

    # Generate a random value of k
    k = random.randint(1, min(50, len(nums)))

    # Calculate the expected result using the provided Solution class
    expected_result = solution.splitArray(nums, k)

    return nums, k, expected_result


def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        nums, k, expected_result = generate_test_case()
        solution = Solution()
        assert solution.splitArray(nums, k) == expected_result
        print(f"assert solution.splitArray({nums}, {k}) == {expected_result}")
        test_case_generator_results.append(
            f"assert solution.splitArray({nums}, {k}) == {expected_result}")  # You can find that we construct the test case in the same format as the example
    return test_case_generator_results


if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.splitArray([681, 630, 94, 58, 88, 835, 727, 989], 5) == 989
assert solution.splitArray([313, 711, 755, 856, 593], 1) == 3228
assert solution.splitArray([893, 865, 255, 469, 370, 566], 2) == 1758
assert solution.splitArray([934, 53, 66, 283, 149, 401], 6) == 934
assert solution.splitArray([21, 469, 787, 734, 19, 401, 639, 484], 8) == 787
assert solution.splitArray([892, 492, 306, 699, 16, 43, 602, 42, 925, 861], 7) == 925
assert solution.splitArray([181], 1) == 181
assert solution.splitArray([763, 487, 674, 284, 566, 807, 371, 68], 1) == 4020
assert solution.splitArray([242, 329, 439, 127, 42, 331, 816], 1) == 2326
assert solution.splitArray([711, 681, 355, 37, 476, 753], 1) == 3013
assert solution.splitArray([74, 781, 694, 549, 232, 384, 55, 461, 189, 139], 1) == 3558
assert solution.splitArray([33, 956, 894, 814, 696, 786, 506, 912, 817], 6) == 1482
assert solution.splitArray([585, 300, 220, 295, 96, 115, 954, 734], 8) == 954
assert solution.splitArray([936, 595, 567, 594], 3) == 1161
assert solution.splitArray([127, 359, 879, 440, 805, 498, 484, 576], 7) == 879
assert solution.splitArray([870, 821, 984], 3) == 984
assert solution.splitArray([28, 17], 2) == 28
assert solution.splitArray([864], 1) == 864
assert solution.splitArray([671, 845, 761, 324, 57, 215], 1) == 2873
assert solution.splitArray([27, 486, 900, 26], 1) == 1439
assert solution.splitArray([214, 571, 682, 425, 414, 343, 34, 216, 928], 3) == 1467
assert solution.splitArray([534, 41, 435, 940, 514], 4) == 940
assert solution.splitArray([10, 545, 486, 107, 115, 538, 858, 627, 523, 790], 4) == 1396
assert solution.splitArray([524, 556, 404], 2) == 960
assert solution.splitArray([753, 97, 552, 417, 324, 104], 5) == 753
assert solution.splitArray([313], 1) == 313
assert solution.splitArray([41, 278], 2) == 278
assert solution.splitArray([415, 545, 463], 2) == 960
assert solution.splitArray([457, 200], 2) == 457
assert solution.splitArray([48, 156], 1) == 204
assert solution.splitArray([687, 972, 79, 30, 945, 462], 1) == 3175
assert solution.splitArray([628, 721, 66, 676, 409], 2) == 1349
assert solution.splitArray([80, 225, 268, 747], 1) == 1320
assert solution.splitArray([490, 907, 457, 688, 713, 666, 397], 6) == 1063
assert solution.splitArray([756, 759, 125, 597, 769, 961, 58, 929, 376], 7) == 987
assert solution.splitArray([670, 247, 82, 195, 341, 179, 416, 418, 625, 938], 1) == 4111
assert solution.splitArray([570, 89, 524, 919, 526, 69, 299], 4) == 919
assert solution.splitArray([233, 178, 482, 236, 87], 3) == 482
assert solution.splitArray([642], 1) == 642
assert solution.splitArray([303, 480, 260, 478, 672, 875, 477, 652, 628], 2) == 2632
assert solution.splitArray([918, 624, 450, 345, 794, 123, 640, 983], 6) == 983
assert solution.splitArray([553, 809, 811, 736, 706, 261, 762, 596], 6) == 1358
assert solution.splitArray([296], 1) == 296
assert solution.splitArray([855, 891, 958, 315, 120, 772], 3) == 1746
assert solution.splitArray([170, 192], 1) == 362
assert solution.splitArray([168, 414, 138, 557], 1) == 1277
assert solution.splitArray([187, 622, 871, 29, 54, 330, 865], 3) == 1195
assert solution.splitArray([307, 382], 2) == 382
assert solution.splitArray([184, 875, 97, 616, 785], 2) == 1401
assert solution.splitArray([364, 118, 164, 657, 730, 461, 168, 193], 1) == 2855
assert solution.splitArray([703, 729, 770, 644, 817, 432], 2) == 2202
assert solution.splitArray([52, 782, 178], 3) == 782
assert solution.splitArray([101, 669, 887], 1) == 1657
assert solution.splitArray([969, 22, 911, 340], 2) == 1251
assert solution.splitArray([203, 652, 635, 799, 259, 746, 312, 650], 3) == 1708
assert solution.splitArray([322, 531, 232], 1) == 1085
assert solution.splitArray([359, 793], 1) == 1152
assert solution.splitArray([307, 457, 540, 276, 732, 929], 2) == 1661
assert solution.splitArray([221, 666, 638, 663], 1) == 2188
assert solution.splitArray([81, 404, 268], 2) == 485
assert solution.splitArray([920, 692], 2) == 920
assert solution.splitArray([821, 564, 585, 392, 260, 374, 235, 299], 2) == 1970
assert solution.splitArray([947, 568, 397, 510], 3) == 947
assert solution.splitArray([780, 634, 385, 4, 326, 360, 706], 3) == 1349
assert solution.splitArray([388, 56, 875, 408, 482, 728, 635, 613, 946, 151], 5) == 1283
assert solution.splitArray([206, 294, 887, 967, 194, 551, 41, 442, 144, 721], 3) == 1712
assert solution.splitArray([649, 331, 678, 436, 954, 187, 354, 593, 60], 7) == 954
assert solution.splitArray([501], 1) == 501
assert solution.splitArray([408, 25, 635, 200, 292, 566, 212, 341], 4) == 858
assert solution.splitArray([117, 570, 182, 338], 2) == 687
assert solution.splitArray([834, 506, 155, 186, 36, 887, 191, 592], 2) == 1706
assert solution.splitArray([514, 225, 193, 366, 333, 559, 934, 722], 3) == 1631
assert solution.splitArray([928, 562, 221, 540, 276, 978], 4) == 978
assert solution.splitArray([667, 732, 917, 730, 54, 109, 28, 334], 5) == 917
assert solution.splitArray([295, 792, 708, 31, 509, 64, 803, 57, 834], 3) == 1694
assert solution.splitArray([98, 174, 850, 27, 397, 943, 956, 401, 94, 433], 4) == 1340
assert solution.splitArray([726, 39, 560, 16, 613, 76, 494, 554, 43, 921], 3) == 1518
assert solution.splitArray([880, 51, 584, 717, 369], 1) == 2601
assert solution.splitArray([2], 1) == 2
assert solution.splitArray([168, 615, 553, 325, 557, 538], 5) == 783
assert solution.splitArray([662, 971, 341], 1) == 1974
assert solution.splitArray([235, 844], 2) == 844
assert solution.splitArray([919, 461, 253, 664, 495, 621, 700], 3) == 1412
assert solution.splitArray([324, 380, 179], 2) == 559
assert solution.splitArray([60, 395, 381, 127, 812, 129, 802, 587, 942], 8) == 942
assert solution.splitArray([669, 6, 499], 1) == 1174
assert solution.splitArray([100, 651, 727, 632, 106, 361, 182, 941, 547], 8) == 941
assert solution.splitArray([370, 367, 616, 178, 550, 954, 338, 252, 21, 250], 6) == 954
assert solution.splitArray([628, 295, 913, 987, 82], 2) == 1836
assert solution.splitArray([712, 440, 551, 87, 974, 826, 308, 858], 4) == 1612
assert solution.splitArray([527, 866, 323], 1) == 1716
assert solution.splitArray([480, 603, 201], 3) == 603
assert solution.splitArray([436, 338, 326, 968], 1) == 2068
assert solution.splitArray([690, 189, 272, 678], 1) == 1829
assert solution.splitArray([697, 947, 617, 391, 687, 430, 49, 352, 596, 318], 3) == 1745
assert solution.splitArray([916, 751, 132, 19, 562], 4) == 916
assert solution.splitArray([418, 588], 1) == 1006
assert solution.splitArray([319, 819, 350, 834, 782, 242, 349, 637, 956, 519], 2) == 3104
assert solution.splitArray([511, 902], 2) == 902
assert solution.splitArray([441, 439, 67, 584, 163, 522], 3) == 880

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
