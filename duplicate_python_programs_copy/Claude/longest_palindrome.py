# Problem 409: Longest Palindrome
# Difficulty: Easy
# Description:
# <p>Given a string <code>s</code> which consists of lowercase or uppercase letters, return <em>the length of the <strong>longest palindrome</strong></em>&nbsp;that can be built with those letters.</p>
# <p>Letters are <strong>case sensitive</strong>, for example,&nbsp;<code>&quot;Aa&quot;</code> is not considered a palindrome here.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;abccccdd&quot;
# <strong>Output:</strong> 7
# <strong>Explanation:</strong> One longest palindrome that can be built is &quot;dccaccd&quot;, whose length is 7.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;a&quot;
# <strong>Output:</strong> 1
# <strong>Explanation:</strong> The longest palindrome that can be built is &quot;a&quot;, whose length is 1.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
# 	<li><code>s</code> consists of lowercase <strong>and/or</strong> uppercase English&nbsp;letters only.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from collections import Counter

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count occurrences of each character
        char_counts = Counter(s)
        
        length = 0
        odd_count_exists = False
        
        # For each character count
        for count in char_counts.values():
            # If count is even, we can use all of them
            if count % 2 == 0:
                length += count
            else:
                # If count is odd, we can use (count-1) characters
                length += count - 1
                odd_count_exists = True
        
        # If there's at least one character with odd count,
        # we can put one in the middle
        if odd_count_exists:
            length += 1
            
        return length

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.longestPalindrome("GxyDLlAh") == 1
assert solution.longestPalindrome("HcEbNV") == 1
assert solution.longestPalindrome("DNQeW") == 1
assert solution.longestPalindrome("Rm") == 1
assert solution.longestPalindrome("aMOqIUDZZ") == 3
assert solution.longestPalindrome("WHtu") == 1
assert solution.longestPalindrome("IKOqqJaucR") == 3
assert solution.longestPalindrome("ig") == 1
assert solution.longestPalindrome("LeUzsYoEbT") == 1
assert solution.longestPalindrome("XgZSa") == 1
assert solution.longestPalindrome("YVxpSr") == 1
assert solution.longestPalindrome("uTSVyofy") == 3
assert solution.longestPalindrome("oENUy") == 1
assert solution.longestPalindrome("f") == 1
assert solution.longestPalindrome("E") == 1
assert solution.longestPalindrome("fzNDsJ") == 1
assert solution.longestPalindrome("mN") == 1
assert solution.longestPalindrome("rI") == 1
assert solution.longestPalindrome("oBbosiCYs") == 5
assert solution.longestPalindrome("pK") == 1
assert solution.longestPalindrome("dNw") == 1
assert solution.longestPalindrome("pdGJJclhF") == 3
assert solution.longestPalindrome("hLfgZ") == 1
assert solution.longestPalindrome("sVKmuaeuQG") == 3
assert solution.longestPalindrome("suYnZmKrt") == 1
assert solution.longestPalindrome("WAG") == 1
assert solution.longestPalindrome("kG") == 1
assert solution.longestPalindrome("ih") == 1
assert solution.longestPalindrome("iB") == 1
assert solution.longestPalindrome("gpu") == 1
assert solution.longestPalindrome("mVQsrMf") == 1
assert solution.longestPalindrome("Ld") == 1
assert solution.longestPalindrome("gRu") == 1
assert solution.longestPalindrome("utBH") == 1
assert solution.longestPalindrome("gLcMUCH") == 1
assert solution.longestPalindrome("QuuAaPQJ") == 5
assert solution.longestPalindrome("nWqtUfCs") == 1
assert solution.longestPalindrome("NNrGZ") == 3
assert solution.longestPalindrome("YeBA") == 1
assert solution.longestPalindrome("B") == 1
assert solution.longestPalindrome("g") == 1
assert solution.longestPalindrome("csCBgple") == 1
assert solution.longestPalindrome("ruKYUiZyF") == 1
assert solution.longestPalindrome("Mct") == 1
assert solution.longestPalindrome("UtJbblK") == 3
assert solution.longestPalindrome("PNDtlcAPLM") == 3
assert solution.longestPalindrome("wbgB") == 1
assert solution.longestPalindrome("F") == 1
assert solution.longestPalindrome("FvFi") == 3
assert solution.longestPalindrome("esERdj") == 1
assert solution.longestPalindrome("cAxNAht") == 3
assert solution.longestPalindrome("dgBRVk") == 1
assert solution.longestPalindrome("vaGRLv") == 3
assert solution.longestPalindrome("vZp") == 1
assert solution.longestPalindrome("vkfXfx") == 3
assert solution.longestPalindrome("vwuHH") == 3
assert solution.longestPalindrome("ZYfi") == 1
assert solution.longestPalindrome("T") == 1
assert solution.longestPalindrome("IzdYDFaQV") == 1
assert solution.longestPalindrome("ZKSocSBIHS") == 3
assert solution.longestPalindrome("r") == 1
assert solution.longestPalindrome("RIM") == 1
assert solution.longestPalindrome("hwtyCpSr") == 1
assert solution.longestPalindrome("B") == 1
assert solution.longestPalindrome("ngF") == 1
assert solution.longestPalindrome("KBiuCkFQJ") == 1
assert solution.longestPalindrome("ESginoagsp") == 3
assert solution.longestPalindrome("x") == 1
assert solution.longestPalindrome("UGeMpu") == 1
assert solution.longestPalindrome("oM") == 1
assert solution.longestPalindrome("zhAzOTU") == 3
assert solution.longestPalindrome("rm") == 1
assert solution.longestPalindrome("W") == 1
assert solution.longestPalindrome("wTf") == 1
assert solution.longestPalindrome("Uh") == 1
assert solution.longestPalindrome("NVMTWj") == 1
assert solution.longestPalindrome("xllqx") == 5
assert solution.longestPalindrome("mSYqucQZ") == 1
assert solution.longestPalindrome("nc") == 1
assert solution.longestPalindrome("NmEdWL") == 1
assert solution.longestPalindrome("ji") == 1
assert solution.longestPalindrome("mTng") == 1
assert solution.longestPalindrome("MWB") == 1
assert solution.longestPalindrome("p") == 1
assert solution.longestPalindrome("lOZdZD") == 3
assert solution.longestPalindrome("ZRPmTOObzh") == 3
assert solution.longestPalindrome("iD") == 1
assert solution.longestPalindrome("eaARO") == 1
assert solution.longestPalindrome("GoGSCG") == 3
assert solution.longestPalindrome("Hki") == 1
assert solution.longestPalindrome("YQjMohunH") == 1
assert solution.longestPalindrome("mXaURIS") == 1
assert solution.longestPalindrome("v") == 1
assert solution.longestPalindrome("iTTzsg") == 3
assert solution.longestPalindrome("QAC") == 1
assert solution.longestPalindrome("cCW") == 1
assert solution.longestPalindrome("SyR") == 1
assert solution.longestPalindrome("uCKQvx") == 1
assert solution.longestPalindrome("UVtYfIQsyU") == 3
assert solution.longestPalindrome("VAGueWdib") == 1

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass