# Problem 2734: Lexicographically Smallest String After Substring Operation
# Difficulty: Medium
# Description:
# <p>You are given a string <code>s</code> consisting of only lowercase English letters. In one operation, you can do the following:</p>
# <ul>
# 	<li>Select any non-empty substring of <code>s</code>, possibly the entire string, then replace each one of its characters with the previous character of the English alphabet. For example, &#39;b&#39; is converted to &#39;a&#39;, and &#39;a&#39; is converted to &#39;z&#39;.</li>
# </ul>
# <p>Return <em>the <strong>lexicographically smallest</strong> string you can obtain after performing the above operation <strong>exactly once</strong>.</em></p>
# <p>A <strong>substring</strong> is a contiguous sequence of characters in a string.</p>
# A string <code>x</code> is <strong>lexicographically smaller</strong> than a string <code>y</code> of the same length if <code>x[i]</code> comes before <code>y[i]</code> in alphabetic order for the first position <code>i</code> such that <code>x[i] != y[i]</code>.
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;cbabc&quot;
# <strong>Output:</strong> &quot;baabc&quot;
# <strong>Explanation:</strong> We apply the operation on the substring starting at index 0, and ending at index 1 inclusive. 
# It can be proven that the resulting string is the lexicographically smallest. 
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;acbbc&quot;
# <strong>Output:</strong> &quot;abaab&quot;
# <strong>Explanation:</strong> We apply the operation on the substring starting at index 1, and ending at index 4 inclusive. 
# It can be proven that the resulting string is the lexicographically smallest. 
# </pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;leetcode&quot;
# <strong>Output:</strong> &quot;kddsbncd&quot;
# <strong>Explanation:</strong> We apply the operation on the entire string. 
# It can be proven that the resulting string is the lexicographically smallest. 
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
# 	<li><code>s</code> consists of lowercase English letters</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random


class Solution:
    def smallestString(self, s: str) -> str:
        # Convert the string into a list for easier modification.
        s_list = list(s)
        n = len(s_list)

        # Indicator to check if we have made a transformation.
        transformed = False

        for i in range(n):
            # Start the operation at the first character that is not 'a'
            if s_list[i] != 'a':
                # Continue transforming until we encounter an 'a' or reach the end.
                while i < n and s_list[i] != 'a':
                    # Replace the character with its preceding letter.
                    s_list[i] = chr(ord(s_list[i]) - 1)
                    i += 1
                transformed = True
                break

        # If no transformation has been done (all letters are 'a'),
        # then we must transform the last letter.
        if not transformed:
            s_list[-1] = 'z'

        # Return the modified list as a string.
        return "".join(s_list)


def generate_test_case():
    solution = Solution()
    
    # Generate random string
    s = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(1, 10)))
    
    # Calculate the expected result using the provided Solution class
    expected_result = solution.smallestString(s)

    return s, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        s, expected_result = generate_test_case()
        solution = Solution()
        assert solution.smallestString(s) == expected_result
        print(f"assert solution.smallestString('{s}') == '{expected_result}'")
        test_case_generator_results.append(f"assert solution.smallestString('{s}') == '{expected_result}'")
    return test_case_generator_results
solution = Solution()
if __name__ == "__main__":
    num_tests = 100  # You can change this to generate more test cases
    test_case_generator_results = test_generated_test_cases(num_tests)

# --------------------------------------
# Test Cases:
assert solution.smallestString('xzxhko') == 'wywgjn'
assert solution.smallestString('k') == 'j'
assert solution.smallestString('seeep') == 'rdddo'
assert solution.smallestString('etkfgbcned') == 'dsjefabmdc'
assert solution.smallestString('xcep') == 'wbdo'
assert solution.smallestString('mnhp') == 'lmgo'
assert solution.smallestString('yfgswwrxo') == 'xefrvvqwn'
assert solution.smallestString('jypeyqg') == 'ixodxpf'
assert solution.smallestString('xihhfurb') == 'whggetqa'
assert solution.smallestString('ltfmhjuox') == 'kselgitnw'
assert solution.smallestString('abevx') == 'aaduw'
assert solution.smallestString('whcmz') == 'vgbly'
assert solution.smallestString('zyvpbxfv') == 'yxuoaweu'
assert solution.smallestString('pji') == 'oih'
assert solution.smallestString('w') == 'v'
assert solution.smallestString('mula') == 'ltka'
assert solution.smallestString('fi') == 'eh'
assert solution.smallestString('wkoja') == 'vjnia'
assert solution.smallestString('bmdlfut') == 'alckets'
assert solution.smallestString('zmn') == 'ylm'
assert solution.smallestString('jlbjmhtcp') == 'ikailgsbo'
assert solution.smallestString('ruafvx') == 'qtafvx'
assert solution.smallestString('avqjcpfg') == 'aupiboef'
assert solution.smallestString('rrvommbfek') == 'qqunllaedj'
assert solution.smallestString('xqpc') == 'wpob'
assert solution.smallestString('mccucbumk') == 'lbbtbatlj'
assert solution.smallestString('zyecmrdyc') == 'yxdblqcxb'
assert solution.smallestString('osq') == 'nrp'
assert solution.smallestString('v') == 'u'
assert solution.smallestString('nfrboqflc') == 'meqanpekb'
assert solution.smallestString('urolg') == 'tqnkf'
assert solution.smallestString('muajx') == 'ltajx'
assert solution.smallestString('fwck') == 'evbj'
assert solution.smallestString('zh') == 'yg'
assert solution.smallestString('zirxf') == 'yhqwe'
assert solution.smallestString('y') == 'x'
assert solution.smallestString('vaf') == 'uaf'
assert solution.smallestString('zlt') == 'yks'
assert solution.smallestString('ffqtfumsql') == 'eepsetlrpk'
assert solution.smallestString('byre') == 'axqd'
assert solution.smallestString('ptkpruqbr') == 'osjoqtpaq'
assert solution.smallestString('tsswyxwg') == 'srrvxwvf'
assert solution.smallestString('ntp') == 'mso'
assert solution.smallestString('lrhklqpp') == 'kqgjkpoo'
assert solution.smallestString('ii') == 'hh'
assert solution.smallestString('wal') == 'val'
assert solution.smallestString('hrzneyz') == 'gqymdxy'
assert solution.smallestString('asm') == 'arl'
assert solution.smallestString('xa') == 'wa'
assert solution.smallestString('nvg') == 'muf'
assert solution.smallestString('xhesndlgv') == 'wgdrmckfu'
assert solution.smallestString('n') == 'm'
assert solution.smallestString('plkzp') == 'okjyo'
assert solution.smallestString('fbomn') == 'eanlm'
assert solution.smallestString('qaklm') == 'paklm'
assert solution.smallestString('omqknlbs') == 'nlpjmkar'
assert solution.smallestString('zsj') == 'yri'
assert solution.smallestString('qizarcut') == 'phyarcut'
assert solution.smallestString('emvvi') == 'dluuh'
assert solution.smallestString('jskzzbwlb') == 'irjyyavka'
assert solution.smallestString('ql') == 'pk'
assert solution.smallestString('k') == 'j'
assert solution.smallestString('l') == 'k'
assert solution.smallestString('oy') == 'nx'
assert solution.smallestString('thenbya') == 'sgdmaxa'
assert solution.smallestString('lwryds') == 'kvqxcr'
assert solution.smallestString('tzxwaowo') == 'sywvaowo'
assert solution.smallestString('rvcsh') == 'qubrg'
assert solution.smallestString('grsxrb') == 'fqrwqa'
assert solution.smallestString('sa') == 'ra'
assert solution.smallestString('xprdqi') == 'woqcph'
assert solution.smallestString('xmepb') == 'wldoa'
assert solution.smallestString('wedbnofi') == 'vdcamneh'
assert solution.smallestString('lpk') == 'koj'
assert solution.smallestString('lzizjxzq') == 'kyhyiwyp'
assert solution.smallestString('br') == 'aq'
assert solution.smallestString('zcjs') == 'ybir'
assert solution.smallestString('bwdetalqng') == 'avcdsalqng'
assert solution.smallestString('z') == 'y'
assert solution.smallestString('gtrv') == 'fsqu'
assert solution.smallestString('mcqks') == 'lbpjr'
assert solution.smallestString('et') == 'ds'
assert solution.smallestString('fcpgn') == 'ebofm'
assert solution.smallestString('xhaxa') == 'wgaxa'
assert solution.smallestString('ncabpzmn') == 'mbabpzmn'
assert solution.smallestString('xf') == 'we'
assert solution.smallestString('upf') == 'toe'
assert solution.smallestString('jqocutkg') == 'ipnbtsjf'
assert solution.smallestString('ehnm') == 'dgml'
assert solution.smallestString('smkbiej') == 'rljahdi'
assert solution.smallestString('twazzlfkz') == 'svazzlfkz'
assert solution.smallestString('ernps') == 'dqmor'
assert solution.smallestString('qelnjb') == 'pdkmia'
assert solution.smallestString('bq') == 'ap'
assert solution.smallestString('mcnrpv') == 'lbmqou'
assert solution.smallestString('cvprlcgq') == 'buoqkbfp'
assert solution.smallestString('gipm') == 'fhol'
assert solution.smallestString('m') == 'l'
assert solution.smallestString('qmqa') == 'plpa'
assert solution.smallestString('uj') == 'ti'

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
