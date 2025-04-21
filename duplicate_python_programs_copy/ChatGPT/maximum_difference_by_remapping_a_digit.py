# Problem 2566: Maximum Difference by Remapping a Digit
# Difficulty: Easy
# Description:
# <p>You are given an integer <code>num</code>. You know that Danny Mittal will sneakily <strong>remap</strong> one of the <code>10</code> possible digits (<code>0</code> to <code>9</code>) to another digit.</p>
# <p>Return <em>the difference between the maximum and minimum</em><em>&nbsp;values Danny can make by remapping&nbsp;<strong>exactly</strong> <strong>one</strong> digit</em><em> in </em><code>num</code>.</p>
# <p><strong>Notes:</strong></p>
# <ul>
# 	<li>When Danny remaps a digit <font face="monospace">d1</font>&nbsp;to another digit <font face="monospace">d2</font>, Danny replaces all occurrences of <code>d1</code>&nbsp;in <code>num</code>&nbsp;with <code>d2</code>.</li>
# 	<li>Danny can remap a digit to itself, in which case <code>num</code>&nbsp;does not change.</li>
# 	<li>Danny can remap different digits for obtaining minimum and maximum values respectively.</li>
# 	<li>The resulting number after remapping can contain leading zeroes.</li>
# 	<li>We mentioned &quot;Danny Mittal&quot; to congratulate him on being in the top 10 in Weekly Contest 326.</li>
# </ul>
# <p>&nbsp;</p>
# <p><strong>Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> num = 11891
# <strong>Output:</strong> 99009
# <strong>Explanation:</strong> 
# To achieve the maximum value, Danny can remap the digit 1 to the digit 9 to yield 99899.
# To achieve the minimum value, Danny can remap the digit 1 to the digit 0, yielding 890.
# The difference between these two numbers is 99009.
# </pre>
# <p><strong>Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> num = 90
# <strong>Output:</strong> 99
# <strong>Explanation:</strong>
# The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
# Thus, we return 99.</pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= num &lt;= 10<sup>8</sup></code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        # Generate max by replacing the first non-9 digit with '9'
        for d in num_str:
            if d != '9':
                max_str = num_str.replace(d, '9')
                break
        else:
            max_str = num_str  # All digits are 9

        # Generate min by replacing the first non-0 digit with '0'
        for d in num_str:
            if d != '0':
                min_str = num_str.replace(d, '0')
                break
        else:
            min_str = num_str  # All digits are 0

        return int(max_str) - int(min_str)


# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.minMaxDifference(20804427) == 90000090
assert solution.minMaxDifference(71943470) == 90000090
assert solution.minMaxDifference(44195743) == 99000090
assert solution.minMaxDifference(63771733) == 90000000
assert solution.minMaxDifference(97443755) == 92000200
assert solution.minMaxDifference(1935418) == 9000090
assert solution.minMaxDifference(42232558) == 90000000
assert solution.minMaxDifference(94718233) == 95000000
assert solution.minMaxDifference(3264502) == 9000000
assert solution.minMaxDifference(37111090) == 90000000
assert solution.minMaxDifference(3452111) == 9000000
assert solution.minMaxDifference(61130406) == 90000009
assert solution.minMaxDifference(47717263) == 90000000
assert solution.minMaxDifference(83276107) == 90000000
assert solution.minMaxDifference(2097301) == 9000000
assert solution.minMaxDifference(52502225) == 90900009
assert solution.minMaxDifference(89318773) == 90009000
assert solution.minMaxDifference(52942446) == 90000000
assert solution.minMaxDifference(7746777) == 9900999
assert solution.minMaxDifference(90031158) == 99900000
assert solution.minMaxDifference(67855487) == 90000000
assert solution.minMaxDifference(60356983) == 90009000
assert solution.minMaxDifference(94187474) == 95000505
assert solution.minMaxDifference(24961039) == 90000000
assert solution.minMaxDifference(36235036) == 90090090
assert solution.minMaxDifference(28196649) == 90000000
assert solution.minMaxDifference(59210070) == 90000000
assert solution.minMaxDifference(86155230) == 90000000
assert solution.minMaxDifference(41513932) == 90000000
assert solution.minMaxDifference(13428890) == 90000000
assert solution.minMaxDifference(82877343) == 90900000
assert solution.minMaxDifference(86275053) == 90000000
assert solution.minMaxDifference(57141709) == 90000000
assert solution.minMaxDifference(99175778) == 99800000
assert solution.minMaxDifference(85608131) == 90009000
assert solution.minMaxDifference(74070688) == 90090000
assert solution.minMaxDifference(38271470) == 90000000
assert solution.minMaxDifference(19800693) == 90000000
assert solution.minMaxDifference(28526131) == 90090000
assert solution.minMaxDifference(17301478) == 90009000
assert solution.minMaxDifference(96444719) == 93000009
assert solution.minMaxDifference(31243197) == 90009000
assert solution.minMaxDifference(9506618) == 9400000
assert solution.minMaxDifference(66196252) == 99009000
assert solution.minMaxDifference(95731684) == 94000000
assert solution.minMaxDifference(76983464) == 90000000
assert solution.minMaxDifference(95966349) == 94900009
assert solution.minMaxDifference(38473886) == 90009000
assert solution.minMaxDifference(79692184) == 90000000
assert solution.minMaxDifference(32924341) == 90000900
assert solution.minMaxDifference(58805888) == 90009000
assert solution.minMaxDifference(7746688) == 9900000
assert solution.minMaxDifference(7702221) == 9900000
assert solution.minMaxDifference(2317397) == 9000000
assert solution.minMaxDifference(73212521) == 90000000
assert solution.minMaxDifference(92869831) == 97009000
assert solution.minMaxDifference(20680606) == 90000000
assert solution.minMaxDifference(65826409) == 90009000
assert solution.minMaxDifference(14061429) == 90009000
assert solution.minMaxDifference(36607692) == 90000000
assert solution.minMaxDifference(37597458) == 90000000
assert solution.minMaxDifference(51959121) == 90090000
assert solution.minMaxDifference(86350250) == 90000000
assert solution.minMaxDifference(49153748) == 90000090
assert solution.minMaxDifference(47540347) == 90090090
assert solution.minMaxDifference(62733476) == 90000009
assert solution.minMaxDifference(8946573) == 9000000
assert solution.minMaxDifference(39821746) == 90000000
assert solution.minMaxDifference(94153068) == 95000000
assert solution.minMaxDifference(46109089) == 90000000
assert solution.minMaxDifference(2116238) == 9000900
assert solution.minMaxDifference(7872609) == 9090000
assert solution.minMaxDifference(26681665) == 90000000
assert solution.minMaxDifference(83139345) == 90000000
assert solution.minMaxDifference(30044894) == 90000000
assert solution.minMaxDifference(42392409) == 90000900
assert solution.minMaxDifference(90363210) == 99000009
assert solution.minMaxDifference(45168081) == 90000000
assert solution.minMaxDifference(87450497) == 90000000
assert solution.minMaxDifference(71606680) == 90000000
assert solution.minMaxDifference(67843589) == 90000000
assert solution.minMaxDifference(10344888) == 90000000
assert solution.minMaxDifference(9328869) == 9600009
assert solution.minMaxDifference(77972366) == 99090000
assert solution.minMaxDifference(58075000) == 90009000
assert solution.minMaxDifference(11203312) == 99000090
assert solution.minMaxDifference(9721803) == 9200000
assert solution.minMaxDifference(88519650) == 99000000
assert solution.minMaxDifference(35311185) == 90900000
assert solution.minMaxDifference(73485407) == 90000009
assert solution.minMaxDifference(53399079) == 90000000
assert solution.minMaxDifference(40396996) == 90000000
assert solution.minMaxDifference(73423339) == 90000000
assert solution.minMaxDifference(93006462) == 96000000
assert solution.minMaxDifference(20414996) == 90000000
assert solution.minMaxDifference(94505792) == 95000090
assert solution.minMaxDifference(70651245) == 90000000
assert solution.minMaxDifference(83715582) == 90000090
assert solution.minMaxDifference(85934423) == 90000000

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass