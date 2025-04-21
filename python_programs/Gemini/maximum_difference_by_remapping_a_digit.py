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

import math

import math

class Solution:
    """
    Calculates the difference between the maximum and minimum values achievable 
    by remapping exactly one digit (0-9) in the input number to another digit (0-9).

    When remapping a digit d1 to d2, all occurrences of d1 are replaced by d2.
    Bob can remap different digits for obtaining minimum and maximum values respectively. 
    The resulting number after remapping can contain leading zeroes, which are 
    handled correctly during integer conversion.
    """
    def minMaxDifference(self, num: int) -> int: # Renamed method from maxDiff to minMaxDifference
        """
        Finds the maximum and minimum possible values after remapping exactly one 
        digit and returns their difference.

        Args:
            num: The input integer (Constraints: 1 <= num <= 10^8).

        Returns:
            The difference between the maximum (a) and minimum (b) remapped values.
        """
        s = str(num)
        n = len(s)

        # Helper function for performing the digit replacement and converting the result to an integer.
        def replace_and_convert(original_s: str, digit_to_replace: str, replace_with: str) -> int:
            """
            Replaces all occurrences of digit_to_replace with replace_with 
            in original_s and converts the resulting string to an integer.

            Args:
                original_s: The original number as a string.
                digit_to_replace: The character digit ('0'-'9') to be replaced.
                replace_with: The character digit ('0'-'9') to replace with.

            Returns:
                The integer value after replacement. Handles leading zeros automatically.
            """
            # String's replace method handles cases where digit_to_replace is not found (no change).
            new_s = original_s.replace(digit_to_replace, replace_with)
            # int() handles conversion and leading zeros correctly (e.g., int("00890") == 890).
            return int(new_s)

        # --- Calculate maximum value (a) ---
        # To achieve the maximum value, we want to replace a digit with '9'.
        # To maximize the effect, we should choose the leftmost digit that is not already '9'.
        # If all digits are '9', no replacement can increase the value, so the maximum is the number itself.
        
        a = num # Initialize max value with the original number.
        digit_to_replace_max = '' 
        for digit in s:
            # Find the first digit from the left that is not '9'.
            if digit != '9':
                digit_to_replace_max = digit
                break 
        
        # If we found a digit that is not '9', replace all its occurrences with '9'.
        if digit_to_replace_max: 
             a = replace_and_convert(s, digit_to_replace_max, '9')
        # Otherwise (all digits are '9'), 'a' remains the original 'num'.

        # --- Calculate minimum value (b) ---
        # To achieve the minimum value, we want to replace a digit with '0' or '1'.
        # We consider two main strategies that prioritize changes affecting the most significant digits.

        # Strategy 1 (min_b1): Replace the first digit s[0] with '0'.
        # This generally yields the smallest number if we target '0' as the replacement,
        # as it affects the most significant position.
        min_b1 = replace_and_convert(s, s[0], '0')

        # Strategy 2 (min_b2): Try replacing a digit with '1'. 
        # This is particularly relevant if the first digit is already small (like '1') 
        # or if replacing a later digit with '1' is more beneficial than Strategy 1.
        # We find the *first* digit `d` (from the left) that is not '0' and not '1'. 
        # Replacing this `d` with '1' is the best candidate for minimization using '1'.
        
        min_b2 = num # Initialize this candidate with the original number.
                      # If no suitable digit is found, this value will be used in the final min comparison.
        digit_to_replace_min = ''
        for digit in s:
             # Find the first digit that is greater than '1'.
             if digit != '0' and digit != '1':
                 digit_to_replace_min = digit
                 break
        
        # If we found such a digit (i.e., the number is not composed only of '0's and '1's),
        # replace all its occurrences with '1'.
        if digit_to_replace_min: 
            min_b2 = replace_and_convert(s, digit_to_replace_min, '1')
        # Otherwise, min_b2 remains 'num'. This handles cases like "100", "111", etc., correctly.

        # The overall minimum value (b) is the minimum result achieved by either Strategy 1 or Strategy 2.
        b = min(min_b1, min_b2)

        # Return the difference between the maximum (a) and minimum (b) values.
        return a - b
    
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