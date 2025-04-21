# Problem 1903: Largest Odd Number in String
# Difficulty: Easy
# Description:
# <p>You are given a string <code>num</code>, representing a large integer. Return <em>the <strong>largest-valued odd</strong> integer (as a string) that is a <strong>non-empty substring</strong> of </em><code>num</code><em>, or an empty string </em><code>&quot;&quot;</code><em> if no odd integer exists</em>.</p>
# <p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> num = &quot;52&quot;
# <strong>Output:</strong> &quot;5&quot;
# <strong>Explanation:</strong> The only non-empty substrings are &quot;5&quot;, &quot;2&quot;, and &quot;52&quot;. &quot;5&quot; is the only odd number.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> num = &quot;4206&quot;
# <strong>Output:</strong> &quot;&quot;
# <strong>Explanation:</strong> There are no odd numbers in &quot;4206&quot;.
# </pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre>
# <strong>Input:</strong> num = &quot;35427&quot;
# <strong>Output:</strong> &quot;35427&quot;
# <strong>Explanation:</strong> &quot;35427&quot; is already an odd number.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
# 	<li><code>num</code> only consists of digits and does not contain any leading zeros.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if (int(num[i]) & 1) == 1:
                return num[: i + 1]
        return ''
# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.largestOddNumber('584') == '5'
assert solution.largestOddNumber('3826166635') == '3826166635'
assert solution.largestOddNumber('57409') == '57409'
assert solution.largestOddNumber('79532556') == '7953255'
assert solution.largestOddNumber('140602379') == '140602379'
assert solution.largestOddNumber('7322') == '73'
assert solution.largestOddNumber('99') == '99'
assert solution.largestOddNumber('5521') == '5521'
assert solution.largestOddNumber('458995') == '458995'
assert solution.largestOddNumber('91') == '91'
assert solution.largestOddNumber('54') == '5'
assert solution.largestOddNumber('4984') == '49'
assert solution.largestOddNumber('3451426') == '3451'
assert solution.largestOddNumber('7973802') == '7973'
assert solution.largestOddNumber('580705') == '580705'
assert solution.largestOddNumber('41') == '41'
assert solution.largestOddNumber('14109') == '14109'
assert solution.largestOddNumber('717') == '717'
assert solution.largestOddNumber('473') == '473'
assert solution.largestOddNumber('5178960903') == '5178960903'
assert solution.largestOddNumber('448524') == '4485'
assert solution.largestOddNumber('052351375') == '052351375'
assert solution.largestOddNumber('2824373144') == '28243731'
assert solution.largestOddNumber('885') == '885'
assert solution.largestOddNumber('7') == '7'
assert solution.largestOddNumber('6580052054') == '658005205'
assert solution.largestOddNumber('3') == '3'
assert solution.largestOddNumber('592109') == '592109'
assert solution.largestOddNumber('738229') == '738229'
assert solution.largestOddNumber('51') == '51'
assert solution.largestOddNumber('7145') == '7145'
assert solution.largestOddNumber('0894768') == '08947'
assert solution.largestOddNumber('1871584714') == '187158471'
assert solution.largestOddNumber('52') == '5'
assert solution.largestOddNumber('3') == '3'
assert solution.largestOddNumber('021') == '021'
assert solution.largestOddNumber('62854') == '6285'
assert solution.largestOddNumber('9704') == '97'
assert solution.largestOddNumber('6301') == '6301'
assert solution.largestOddNumber('9500273') == '9500273'
assert solution.largestOddNumber('754') == '75'
assert solution.largestOddNumber('85979618') == '8597961'
assert solution.largestOddNumber('85906174') == '8590617'
assert solution.largestOddNumber('122') == '1'
assert solution.largestOddNumber('2080499') == '2080499'
assert solution.largestOddNumber('4735506') == '47355'
assert solution.largestOddNumber('15325793') == '15325793'
assert solution.largestOddNumber('296491922') == '2964919'
assert solution.largestOddNumber('58566352') == '5856635'
assert solution.largestOddNumber('1617') == '1617'
assert solution.largestOddNumber('7947') == '7947'
assert solution.largestOddNumber('9456946') == '94569'
assert solution.largestOddNumber('761') == '761'
assert solution.largestOddNumber('27781329') == '27781329'
assert solution.largestOddNumber('2316167693') == '2316167693'
assert solution.largestOddNumber('8846574') == '884657'
assert solution.largestOddNumber('5215731656') == '521573165'
assert solution.largestOddNumber('6299810914') == '629981091'
assert solution.largestOddNumber('7907') == '7907'
assert solution.largestOddNumber('0618638') == '061863'
assert solution.largestOddNumber('96646108') == '966461'
assert solution.largestOddNumber('95563') == '95563'
assert solution.largestOddNumber('0211276') == '021127'
assert solution.largestOddNumber('998849') == '998849'
assert solution.largestOddNumber('6029') == '6029'
assert solution.largestOddNumber('4459088106') == '44590881'
assert solution.largestOddNumber('25333') == '25333'
assert solution.largestOddNumber('503983482') == '503983'
assert solution.largestOddNumber('9720622') == '97'
assert solution.largestOddNumber('1192620') == '119'
assert solution.largestOddNumber('35502494') == '3550249'
assert solution.largestOddNumber('3413360') == '34133'
assert solution.largestOddNumber('9') == '9'
assert solution.largestOddNumber('3555') == '3555'
assert solution.largestOddNumber('748') == '7'
assert solution.largestOddNumber('7536387848') == '7536387'
assert solution.largestOddNumber('409239164') == '4092391'
assert solution.largestOddNumber('81175662') == '81175'
assert solution.largestOddNumber('964283356') == '96428335'
assert solution.largestOddNumber('852362') == '8523'
assert solution.largestOddNumber('3186229') == '3186229'
assert solution.largestOddNumber('866274') == '86627'
assert solution.largestOddNumber('774751929') == '774751929'
assert solution.largestOddNumber('126496818') == '12649681'
assert solution.largestOddNumber('5') == '5'
assert solution.largestOddNumber('365942422') == '3659'
assert solution.largestOddNumber('76') == '7'
assert solution.largestOddNumber('53') == '53'
assert solution.largestOddNumber('7799') == '7799'
assert solution.largestOddNumber('1616425821') == '1616425821'
assert solution.largestOddNumber('506') == '5'
assert solution.largestOddNumber('11') == '11'
assert solution.largestOddNumber('73229') == '73229'

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
