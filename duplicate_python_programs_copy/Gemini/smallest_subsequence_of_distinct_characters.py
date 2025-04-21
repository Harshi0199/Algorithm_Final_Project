# Problem 1081: Smallest Subsequence of Distinct Characters
# Difficulty: Medium
# Description:
# <p>Given a string <code>s</code>, return <em>the </em><span data-keyword="lexicographically-smaller-string"><em>lexicographically smallest</em></span> <span data-keyword="subsequence-string"><em>subsequence</em></span><em> of</em> <code>s</code> <em>that contains all the distinct characters of</em> <code>s</code> <em>exactly once</em>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;bcabc&quot;
# <strong>Output:</strong> &quot;abc&quot;
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> s = &quot;cbacdcbc&quot;
# <strong>Output:</strong> &quot;acdb&quot;
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
# 	<li><code>s</code> consists of lowercase English letters.</li>
# </ul>
# <p>&nbsp;</p>
# <strong>Note:</strong> This question is the same as 316: <a href="https://leetcode.com/problems/remove-duplicate-letters/" target="_blank">https://leetcode.com/problems/remove-duplicate-letters/</a>
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []
        seen = set()

        for i, char in enumerate(s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())

                stack.append(char)
                seen.add(char)

        return "".join(stack)

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.smallestSubsequence('zzkixyest') == 'zkixyest'
assert solution.smallestSubsequence('hpkxhx') == 'hpkx'
assert solution.smallestSubsequence('qhx') == 'qhx'
assert solution.smallestSubsequence('lnxgxhi') == 'lngxhi'
assert solution.smallestSubsequence('s') == 's'
assert solution.smallestSubsequence('pz') == 'pz'
assert solution.smallestSubsequence('a') == 'a'
assert solution.smallestSubsequence('svymdtbj') == 'svymdtbj'
assert solution.smallestSubsequence('winj') == 'winj'
assert solution.smallestSubsequence('lj') == 'lj'
assert solution.smallestSubsequence('lsjqnd') == 'lsjqnd'
assert solution.smallestSubsequence('vkdxopfr') == 'vkdxopfr'
assert solution.smallestSubsequence('yvvrkovj') == 'yrkovj'
assert solution.smallestSubsequence('zqe') == 'zqe'
assert solution.smallestSubsequence('khd') == 'khd'
assert solution.smallestSubsequence('oszmfgh') == 'oszmfgh'
assert solution.smallestSubsequence('iho') == 'iho'
assert solution.smallestSubsequence('kvcepo') == 'kvcepo'
assert solution.smallestSubsequence('vxyeshedpv') == 'vxyeshdp'
assert solution.smallestSubsequence('xqye') == 'xqye'
assert solution.smallestSubsequence('uhdkmjjfla') == 'uhdkmjfla'
assert solution.smallestSubsequence('rvslihrjr') == 'rvslihj'
assert solution.smallestSubsequence('tlg') == 'tlg'
assert solution.smallestSubsequence('bhdskbmmp') == 'bhdskmp'
assert solution.smallestSubsequence('pulqjcpp') == 'pulqjc'
assert solution.smallestSubsequence('iuj') == 'iuj'
assert solution.smallestSubsequence('lwld') == 'lwd'
assert solution.smallestSubsequence('imdvzggtw') == 'imdvzgtw'
assert solution.smallestSubsequence('drr') == 'dr'
assert solution.smallestSubsequence('fnkgslxf') == 'fnkgslx'
assert solution.smallestSubsequence('myz') == 'myz'
assert solution.smallestSubsequence('ydgp') == 'ydgp'
assert solution.smallestSubsequence('ao') == 'ao'
assert solution.smallestSubsequence('zskm') == 'zskm'
assert solution.smallestSubsequence('pkqq') == 'pkq'
assert solution.smallestSubsequence('zvkomemdh') == 'zvkoemdh'
assert solution.smallestSubsequence('jmdcpgrur') == 'jmdcpgru'
assert solution.smallestSubsequence('zki') == 'zki'
assert solution.smallestSubsequence('auasjbq') == 'ausjbq'
assert solution.smallestSubsequence('tbsvse') == 'tbsve'
assert solution.smallestSubsequence('qbarmodyvx') == 'qbarmodyvx'
assert solution.smallestSubsequence('tirtwpcd') == 'irtwpcd'
assert solution.smallestSubsequence('ghluhgvrdy') == 'ghluvrdy'
assert solution.smallestSubsequence('schsvo') == 'chsvo'
assert solution.smallestSubsequence('zlofqw') == 'zlofqw'
assert solution.smallestSubsequence('fppt') == 'fpt'
assert solution.smallestSubsequence('m') == 'm'
assert solution.smallestSubsequence('p') == 'p'
assert solution.smallestSubsequence('e') == 'e'
assert solution.smallestSubsequence('xdv') == 'xdv'
assert solution.smallestSubsequence('pbpt') == 'bpt'
assert solution.smallestSubsequence('p') == 'p'
assert solution.smallestSubsequence('y') == 'y'
assert solution.smallestSubsequence('doh') == 'doh'
assert solution.smallestSubsequence('svqif') == 'svqif'
assert solution.smallestSubsequence('el') == 'el'
assert solution.smallestSubsequence('wbohjcmm') == 'wbohjcm'
assert solution.smallestSubsequence('l') == 'l'
assert solution.smallestSubsequence('sfwdlo') == 'sfwdlo'
assert solution.smallestSubsequence('v') == 'v'
assert solution.smallestSubsequence('hbpwbwspti') == 'hbpwsti'
assert solution.smallestSubsequence('kqwfukhsb') == 'kqwfuhsb'
assert solution.smallestSubsequence('zlbrun') == 'zlbrun'
assert solution.smallestSubsequence('zj') == 'zj'
assert solution.smallestSubsequence('evky') == 'evky'
assert solution.smallestSubsequence('s') == 's'
assert solution.smallestSubsequence('jsah') == 'jsah'
assert solution.smallestSubsequence('gc') == 'gc'
assert solution.smallestSubsequence('fdhtk') == 'fdhtk'
assert solution.smallestSubsequence('xojwv') == 'xojwv'
assert solution.smallestSubsequence('jdl') == 'jdl'
assert solution.smallestSubsequence('elaogj') == 'elaogj'
assert solution.smallestSubsequence('tnawufks') == 'tnawufks'
assert solution.smallestSubsequence('mnqeakq') == 'mneakq'
assert solution.smallestSubsequence('easvdstlf') == 'easvdtlf'
assert solution.smallestSubsequence('l') == 'l'
assert solution.smallestSubsequence('dcbczgoz') == 'dbcgoz'
assert solution.smallestSubsequence('vfadhsqe') == 'vfadhsqe'
assert solution.smallestSubsequence('ttsqwm') == 'tsqwm'
assert solution.smallestSubsequence('sitywthvul') == 'sitywhvul'
assert solution.smallestSubsequence('qsdolf') == 'qsdolf'
assert solution.smallestSubsequence('wszvtk') == 'wszvtk'
assert solution.smallestSubsequence('tlztnst') == 'lznst'
assert solution.smallestSubsequence('ts') == 'ts'
assert solution.smallestSubsequence('e') == 'e'
assert solution.smallestSubsequence('pciwnsxfai') == 'pciwnsxfa'
assert solution.smallestSubsequence('eabp') == 'eabp'
assert solution.smallestSubsequence('lxozsq') == 'lxozsq'
assert solution.smallestSubsequence('wvgsqkc') == 'wvgsqkc'
assert solution.smallestSubsequence('vsrfxdofz') == 'vsrfxdoz'
assert solution.smallestSubsequence('l') == 'l'
assert solution.smallestSubsequence('tppmet') == 'pmet'
assert solution.smallestSubsequence('cgscjbi') == 'cgsjbi'
assert solution.smallestSubsequence('smp') == 'smp'
assert solution.smallestSubsequence('qtjlom') == 'qtjlom'
assert solution.smallestSubsequence('uwd') == 'uwd'
assert solution.smallestSubsequence('qtkgigfqw') == 'qtkgifw'
assert solution.smallestSubsequence('immugbznc') == 'imugbznc'
assert solution.smallestSubsequence('pb') == 'pb'
assert solution.smallestSubsequence('jjzewqx') == 'jzewqx'

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
