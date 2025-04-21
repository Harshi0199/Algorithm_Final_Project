# Problem 527: Word Abbreviation
# Difficulty: Hard
# Description:
# <p>Given an array of <strong>distinct</strong> strings <code>words</code>, return <em>the minimal possible <strong>abbreviations</strong> for every word</em>.</p>
# <p>The following are the rules for a string abbreviation:</p>
# <ol>
# 	<li>The <strong>initial</strong> abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.</li>
# 	<li>If more than one word shares the <strong>same</strong> abbreviation, then perform the following operation:
# 	<ul>
# 		<li><strong>Increase</strong> the prefix (characters in the first part) of each of their abbreviations by <code>1</code>.
# 		<ul>
# 			<li>For example, say you start with the words <code>[&quot;abcdef&quot;,&quot;abndef&quot;]</code> both initially abbreviated as <code>&quot;a4f&quot;</code>. Then, a sequence of operations would be <code>[&quot;a4f&quot;,&quot;a4f&quot;]</code> -&gt; <code>[&quot;ab3f&quot;,&quot;ab3f&quot;]</code> -&gt; <code>[&quot;abc2f&quot;,&quot;abn2f&quot;]</code>.</li>
# 		</ul>
# 		</li>
# 		<li>This operation is repeated until every abbreviation is <strong>unique</strong>.</li>
# 	</ul>
# 	</li>
# 	<li>At the end, if an abbreviation did not make a word shorter, then keep it as the original word.</li>
# </ol>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre><strong>Input:</strong> words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
# <strong>Output:</strong> ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# </pre><p><strong class="example">Example 2:</strong></p>
# <pre><strong>Input:</strong> words = ["aa","aaa"]
# <strong>Output:</strong> ["aa","aaa"]
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= words.length &lt;= 400</code></li>
# 	<li><code>2 &lt;= words[i].length &lt;= 400</code></li>
# 	<li><code>words[i]</code> consists of lowercase English letters.</li>
# 	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random
from typing import List

class Trie:
    __slots__ = ["children", "cnt"]

    def __init__(self):
        self.children = [None] * 26
        self.cnt = 0

    def insert(self, w: str):
        node = self
        for c in w:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.cnt += 1

    def search(self, w: str) -> int:
        node = self
        cnt = 0
        for c in w:
            cnt += 1
            idx = ord(c) - ord("a")
            node = node.children[idx]
            if node.cnt == 1:
                return cnt
        return len(w)


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        tries = {}
        for w in words:
            m = len(w)
            if (m, w[-1]) not in tries:
                tries[(m, w[-1])] = Trie()
            tries[(m, w[-1])].insert(w)
        ans = []
        for w in words:
            cnt = tries[(len(w), w[-1])].search(w)
            ans.append(
                w if cnt + 2 >= len(w) else w[:cnt] + str(len(w) - cnt - 1) + w[-1]
            )
        return ans


def generate_test_case():
    solution = Solution()
    words = []
    for _ in range(random.randint(1, 10)):
        word = ""
        for _ in range(random.randint(1, 10)):
            word += chr(random.randint(ord("a"), ord("z")))
        words.append(word)
    expected_result = solution.wordsAbbreviation(words)
    return words, expected_result

def test_generated_test_cases(num_tests):
    test_case_generator_results = []
    for i in range(num_tests):
        words, expected_result = generate_test_case()
        solution = Solution()
        assert solution.wordsAbbreviation(words) == expected_result
        print(f'assert solution.wordsAbbreviation({words}) == {expected_result}')
        test_case_generator_results.append(f'assert solution.wordsAbbreviation({words}) == {expected_result}')
    return test_case_generator_results

if __name__ == "__main__":
    num_tests = 100 
    test_case_generator_results = test_generated_test_cases(num_tests)

solution=Solution()
# --------------------------------------
# Test Cases:
assert solution.wordsAbbreviation(['ggkgzjpf', 'xovkwx', 'olbn']) == ['g6f', 'x4x', 'o2n']
assert solution.wordsAbbreviation(['el', 'dqh', 'laahe']) == ['el', 'dqh', 'l3e']
assert solution.wordsAbbreviation(['jfckrtx', 'gbpugdalt', 'ehot', 'febj', 'by', 'ff', 'uyvucfcypo', 'srcrttymku']) == ['j5x', 'g7t', 'e2t', 'f2j', 'by', 'ff', 'u8o', 's8u']
assert solution.wordsAbbreviation(['bboftpag', 'lzavexquoo', 'ocgzcjsw', 'usoxqccu', 'eybqbso', 'nlnrhm']) == ['b6g', 'l8o', 'o6w', 'u6u', 'e5o', 'n4m']
assert solution.wordsAbbreviation(['yrnb', 'reszfvzwsm', 'mvzmydsttc', 'iejtazaek', 'psxaajcy', 'ubx', 'ardicpegz', 'ov', 'hsydbtn']) == ['y2b', 'r8m', 'm8c', 'i7k', 'p6y', 'ubx', 'a7z', 'ov', 'h5n']
assert solution.wordsAbbreviation(['dyumohkw', 'eisqidxb', 'qjirmuq', 'aefs', 'pce', 'ophnshe', 'svnjpafmf', 'xkhi']) == ['d6w', 'e6b', 'q5q', 'a2s', 'pce', 'o5e', 's7f', 'x2i']
assert solution.wordsAbbreviation(['brhwkgbjw', 'wfqk', 'krnc', 's', 'zaran']) == ['b7w', 'w2k', 'k2c', 's', 'z3n']
assert solution.wordsAbbreviation(['thhjjqwl', 'rxd', 'vhvc', 'tc', 'bfp']) == ['t6l', 'rxd', 'v2c', 'tc', 'bfp']
assert solution.wordsAbbreviation(['hhhhant', 'nkewfqslty', 'ftuohdrnbf', 'hvvl', 'soyjujiy']) == ['h5t', 'n8y', 'f8f', 'h2l', 's6y']
assert solution.wordsAbbreviation(['ogkaqgsj', 'htswg', 'v', 'mgbredffy', 'jyokzsor', 'cl', 'gmrtldc', 'dbvcqlew']) == ['o6j', 'h3g', 'v', 'm7y', 'j6r', 'cl', 'g5c', 'd6w']
assert solution.wordsAbbreviation(['angxlx', 'pfcpkamubh', 'gyhsjpz']) == ['a4x', 'p8h', 'g5z']
assert solution.wordsAbbreviation(['csjref', 'sadlrsv', 'ycchhqoh', 'mencdaqbqd', 'jw', 'elc', 'uwcpjdxq', 'agimsu', 'xw', 'pethiffkj']) == ['c4f', 's5v', 'y6h', 'm8d', 'jw', 'elc', 'u6q', 'a4u', 'xw', 'p7j']
assert solution.wordsAbbreviation(['fkgkg', 'wdswngruig', 'dhgwnh', 'jpiuhsikom', 'opbhcxylx']) == ['f3g', 'w8g', 'd4h', 'j8m', 'o7x']
assert solution.wordsAbbreviation(['qcpo', 'qdztkh', 'ol', 'zpvycps', 'a', 'th', 'yezp', 'lbvnaxks', 'z']) == ['q2o', 'q4h', 'ol', 'z5s', 'a', 'th', 'y2p', 'l6s', 'z']
assert solution.wordsAbbreviation(['a', 'dlkga', 'qoyfgnruo', 'mzabw']) == ['a', 'd3a', 'q7o', 'm3w']
assert solution.wordsAbbreviation(['yul', 'bxjeaaazb', 'mfayvkhhem', 'ibicq', 'mwfbqdfy', 'dcu']) == ['yul', 'b7b', 'm8m', 'i3q', 'm6y', 'dcu']
assert solution.wordsAbbreviation(['zsyqvqdvt', 'psqe', 'lncu', 'rl', 'reaj', 'm', 'zrezljst', 'cpta']) == ['z7t', 'p2e', 'l2u', 'rl', 'r2j', 'm', 'z6t', 'c2a']
assert solution.wordsAbbreviation(['ckif', 'gkcezglzrz', 'ugosfeg']) == ['c2f', 'g8z', 'u5g']
assert solution.wordsAbbreviation(['mrf', 'srlozoucm', 'epwitgfj', 'of', 'npnaylqtzx', 'bwon']) == ['mrf', 's7m', 'e6j', 'of', 'n8x', 'b2n']
assert solution.wordsAbbreviation(['jsing', 'r', 'fxztsnsltq', 'acaji']) == ['j3g', 'r', 'f8q', 'a3i']
assert solution.wordsAbbreviation(['gusswb', 'vigm', 'asblgztq', 'etcvr', 'pfxgt']) == ['g4b', 'v2m', 'a6q', 'e3r', 'p3t']
assert solution.wordsAbbreviation(['zrrbcvt', 'vmsegboz', 'zgpgqkqk', 'vlwie']) == ['z5t', 'v6z', 'z6k', 'v3e']
assert solution.wordsAbbreviation(['ga']) == ['ga']
assert solution.wordsAbbreviation(['ak', 'ylxhjvls', 'ilcuxt', 'shykr', 'bdfcvirfr', 'r', 'a', 'rv', 'y', 'fren']) == ['ak', 'y6s', 'i4t', 's3r', 'b7r', 'r', 'a', 'rv', 'y', 'f2n']
assert solution.wordsAbbreviation(['ekdincjqs', 'j', 'oidluzgraa', 'dsmtkryfkw', 'msjjrqwxev', 'yerjiv']) == ['e7s', 'j', 'o8a', 'd8w', 'm8v', 'y4v']
assert solution.wordsAbbreviation(['tzv', 'vj', 'ucfgfg', 'qhylpqjj']) == ['tzv', 'vj', 'u4g', 'q6j']
assert solution.wordsAbbreviation(['bjst', 'mzeog', 'apmakt', 'xuxmfdj', 'espkm', 'hqhmk', 'rv', 'tk', 'f', 'mutmvtk']) == ['b2t', 'm3g', 'a4t', 'x5j', 'e3m', 'h3k', 'rv', 'tk', 'f', 'm5k']
assert solution.wordsAbbreviation(['dlvmicsms', 'm', 'bbedlizj', 'npfcaks', 'sld', 'afmbbc', 'ykibdzqdwl', 'ib']) == ['d7s', 'm', 'b6j', 'n5s', 'sld', 'a4c', 'y8l', 'ib']
assert solution.wordsAbbreviation(['fxzo', 'jgmaezcmm', 'hpbog', 'hcduavfujy', 'zq']) == ['f2o', 'j7m', 'h3g', 'h8y', 'zq']
assert solution.wordsAbbreviation(['x', 'ccxloqsz', 'sxxjdouv', 'uqfc', 'th', 'hvomgqmeae', 'ktfqeys', 'iiypdqb']) == ['x', 'c6z', 's6v', 'u2c', 'th', 'h8e', 'k5s', 'i5b']
assert solution.wordsAbbreviation(['v', 'vxxat', 'kwdmqqm', 'uusawokva', 'olnoudwaxc', 'z', 'zspwt']) == ['v', 'v3t', 'k5m', 'u7a', 'o8c', 'z', 'z3t']
assert solution.wordsAbbreviation(['rmt', 'n']) == ['rmt', 'n']
assert solution.wordsAbbreviation(['gdovdfajx', 'bwkzsnkbn', 'fhjskjxaj']) == ['g7x', 'b7n', 'f7j']
assert solution.wordsAbbreviation(['ddkpc', 'quwgfcbtnd', 'x', 'ewmrlfhrj', 'gccvxvc']) == ['d3c', 'q8d', 'x', 'e7j', 'g5c']
assert solution.wordsAbbreviation(['nxowfcmxm']) == ['n7m']
assert solution.wordsAbbreviation(['dcwxaapevh', 'bimepjaa', 'avcnd', 'fvbt', 'rcvttyysq']) == ['d8h', 'b6a', 'a3d', 'f2t', 'r7q']
assert solution.wordsAbbreviation(['zi', 'uehgjxkm', 'vpj']) == ['zi', 'u6m', 'vpj']
assert solution.wordsAbbreviation(['vnilrswrsf', 'cjln', 'awkydzpxy']) == ['v8f', 'c2n', 'a7y']
assert solution.wordsAbbreviation(['nruspible', 'vo', 'koaawwlz', 'cl', 'answpyw', 'bqqxuegs']) == ['n7e', 'vo', 'k6z', 'cl', 'a5w', 'b6s']
assert solution.wordsAbbreviation(['xj', 'twawvdqb', 'vhc', 'wutlaot', 'nivlvr', 'sulgxmu', 'hyrlquy', 'rnjvgnbxd', 'zsest', 'ahusglqkhu']) == ['xj', 't6b', 'vhc', 'w5t', 'n4r', 's5u', 'h5y', 'r7d', 'z3t', 'a8u']
assert solution.wordsAbbreviation(['qmrmpumy', 'xd', 'y', 'sclp', 'alubdldjg', 'wdagy', 'pbytyo', 'tak', 'vgyyjq', 'kfxaxkw']) == ['q6y', 'xd', 'y', 's2p', 'a7g', 'w3y', 'p4o', 'tak', 'v4q', 'k5w']
assert solution.wordsAbbreviation(['st', 'wdhyeu', 'uuxxvubbhh', 'mtnvsdns']) == ['st', 'w4u', 'u8h', 'm6s']
assert solution.wordsAbbreviation(['wxzjkl']) == ['w4l']
assert solution.wordsAbbreviation(['blmkn', 'ohyychm']) == ['b3n', 'o5m']
assert solution.wordsAbbreviation(['uhc', 'rekcsecx']) == ['uhc', 'r6x']
assert solution.wordsAbbreviation(['qrollpghk', 'lzffbjbjs', 'jjjwnpv', 'rcvz', 'qpxjd', 'wexnjiu', 'bfumw', 'dgvrlzhn', 'feenqfg']) == ['q7k', 'l7s', 'j5v', 'r2z', 'q3d', 'w5u', 'b3w', 'd6n', 'f5g']
assert solution.wordsAbbreviation(['ebf', 'ivqtqxuj', 'wptsvdatix', 'wncl', 'ozflzm']) == ['ebf', 'i6j', 'w8x', 'w2l', 'o4m']
assert solution.wordsAbbreviation(['jkumw', 'm', 'exldl', 'fotxp', 'twsh', 'lahtdmw']) == ['j3w', 'm', 'e3l', 'f3p', 't2h', 'l5w']
assert solution.wordsAbbreviation(['cxlgglpd', 'b', 'y', 'klydtvv', 'o', 'pml', 'negvqeeq', 'eexxgn', 'igqoyku', 'zqbolowgfc']) == ['c6d', 'b', 'y', 'k5v', 'o', 'pml', 'n6q', 'e4n', 'i5u', 'z8c']
assert solution.wordsAbbreviation(['yamjrgjxxx', 'oajb']) == ['y8x', 'o2b']
assert solution.wordsAbbreviation(['spra', 'rcpljwq']) == ['s2a', 'r5q']
assert solution.wordsAbbreviation(['qc', 'pmpkve', 'byi', 'lja', 'wawwd', 'ftrmkyehdm', 'eaoi', 'ugflhcufe', 'zs', 'yumpwm']) == ['qc', 'p4e', 'byi', 'lja', 'w3d', 'f8m', 'e2i', 'u7e', 'zs', 'y4m']
assert solution.wordsAbbreviation(['cx', 'fgfooudzzv', 'ulrmvcgf', 'ft', 'qpytbkbim', 'lapt', 'rdvqwa', 'ltxnal', 'yaw']) == ['cx', 'f8v', 'u6f', 'ft', 'q7m', 'l2t', 'r4a', 'l4l', 'yaw']
assert solution.wordsAbbreviation(['gowt', 'icxlh', 'otveyrlkt', 'qxziflb', 'syqn', 'pqbb']) == ['g2t', 'i3h', 'o7t', 'q5b', 's2n', 'p2b']
assert solution.wordsAbbreviation(['yucvq']) == ['y3q']
assert solution.wordsAbbreviation(['cuouxago', 'juhm', 'icuzuq', 'th', 'mchkrbpk', 'ckqduurd', 'lbuzbjtl']) == ['c6o', 'j2m', 'i4q', 'th', 'm6k', 'c6d', 'l6l']
assert solution.wordsAbbreviation(['vpxjssups', 'mlrjzuoqt', 'cxg', 'rdof', 'qzvnc']) == ['v7s', 'm7t', 'cxg', 'r2f', 'q3c']
assert solution.wordsAbbreviation(['rjerxysjzz', 'zvnpmjxz', 'fkvzkbpfu', 'johkinv']) == ['r8z', 'z6z', 'f7u', 'j5v']
assert solution.wordsAbbreviation(['kvqyu', 'xnuiplrlk', 'we', 'nawuhrqxyk']) == ['k3u', 'x7k', 'we', 'n8k']
assert solution.wordsAbbreviation(['crz', 'gqzvkddn', 'guiamhr', 'qyexmt', 'xh', 'qwpsoe', 'qfmnmr', 'dwdjeiqgmm']) == ['crz', 'g6n', 'g5r', 'q4t', 'xh', 'q4e', 'q4r', 'd8m']
assert solution.wordsAbbreviation(['bpzep']) == ['b3p']
assert solution.wordsAbbreviation(['mg']) == ['mg']
assert solution.wordsAbbreviation(['ngadfeenr', 'vyhlk', 'nkmprnhqx']) == ['n7r', 'v3k', 'n7x']
assert solution.wordsAbbreviation(['meyesm', 'g', 'n']) == ['m4m', 'g', 'n']
assert solution.wordsAbbreviation(['dcnuy', 'kzx', 'qbooypyzwf', 'xwaawt', 'bc', 'mngoqnwvxy', 'hyyocnr', 'sgvwsr']) == ['d3y', 'kzx', 'q8f', 'x4t', 'bc', 'm8y', 'h5r', 's4r']
assert solution.wordsAbbreviation(['oxit', 'xyvmpchmk', 'cgwmkfvo', 'ewpbqweq']) == ['o2t', 'x7k', 'c6o', 'e6q']
assert solution.wordsAbbreviation(['euwnjr', 'x', 'urhzpvimag', 'fblwweobf', 'wpatkgal', 'qxfnunkvep', 'ykyaut', 'gznrkc', 't']) == ['e4r', 'x', 'u8g', 'f7f', 'w6l', 'q8p', 'y4t', 'g4c', 't']
assert solution.wordsAbbreviation(['o', 'xdilp']) == ['o', 'x3p']
assert solution.wordsAbbreviation(['bv', 'gtobomlteq', 'qhhvtdp', 'ks', 'fsdxpz', 'mjn', 'l']) == ['bv', 'g8q', 'q5p', 'ks', 'f4z', 'mjn', 'l']
assert solution.wordsAbbreviation(['mgkjsya', 'pjgkwcoi', 'qv', 'yp', 'ymbtznqd', 'wrrkamxvp']) == ['m5a', 'p6i', 'qv', 'yp', 'y6d', 'w7p']
assert solution.wordsAbbreviation(['wl', 'cikdlvmfy', 'oz']) == ['wl', 'c7y', 'oz']
assert solution.wordsAbbreviation(['mwjmnbk']) == ['m5k']
assert solution.wordsAbbreviation(['yzexb', 'zwqxir', 'xsacdkoojs', 'wi', 'xcqeelras', 'md', 'tyzbmubvao', 'syusfgq', 'ffqqdlp', 'nvzgpmp']) == ['y3b', 'z4r', 'x8s', 'wi', 'x7s', 'md', 't8o', 's5q', 'f5p', 'n5p']
assert solution.wordsAbbreviation(['mljznd', 'nn', 'uvmu', 'mulftpflef', 'alt']) == ['m4d', 'nn', 'u2u', 'm8f', 'alt']
assert solution.wordsAbbreviation(['w', 'iehv', 'fclvlg', 't', 'gglxwfra', 'p', 'taqcxlfth', 'xtwmphsl']) == ['w', 'i2v', 'f4g', 't', 'g6a', 'p', 't7h', 'x6l']
assert solution.wordsAbbreviation(['gbhkofutaf', 'rdmu', 'wmhajrebsi', 'oojdpwi']) == ['g8f', 'r2u', 'w8i', 'o5i']
assert solution.wordsAbbreviation(['ocemrmicyg', 'ke', 'mkbofkm', 'fxlpafx', 'uoa', 'qhrk', 'fx', 'xpdmv', 'wuexalu']) == ['o8g', 'ke', 'm5m', 'f5x', 'uoa', 'q2k', 'fx', 'x3v', 'w5u']
assert solution.wordsAbbreviation(['pzo', 'ntaxmdu', 'stzwi']) == ['pzo', 'n5u', 's3i']
assert solution.wordsAbbreviation(['sm', 'a', 'mjgbvsub', 'tnrhccz', 'nrbouxf', 'a']) == ['sm', 'a', 'm6b', 't5z', 'n5f', 'a']
assert solution.wordsAbbreviation(['cnltnoythi', 'g', 'swagnpil', 'ijwr']) == ['c8i', 'g', 's6l', 'i2r']
assert solution.wordsAbbreviation(['fp', 'ddkl', 'ejsqxucvp', 'rjfyd', 'vhl', 'qnmng', 'gf']) == ['fp', 'd2l', 'e7p', 'r3d', 'vhl', 'q3g', 'gf']
assert solution.wordsAbbreviation(['auvsddr', 'axewnsfrwl', 'nmoyilhou', 'te', 'gogu']) == ['a5r', 'a8l', 'n7u', 'te', 'g2u']
assert solution.wordsAbbreviation(['sqsplfdlw']) == ['s7w']
assert solution.wordsAbbreviation(['nktmmm', 'yeyrdmi', 'kraeljw', 'yhbrdarrbn', 'xr', 'xxg', 'ozsjexejf', 'oon']) == ['n4m', 'y5i', 'k5w', 'y8n', 'xr', 'xxg', 'o7f', 'oon']
assert solution.wordsAbbreviation(['dvqwgu', 'semeqsa', 'nrns', 'slzyhgv', 'bughcpjis', 'ju']) == ['d4u', 's5a', 'n2s', 's5v', 'b7s', 'ju']
assert solution.wordsAbbreviation(['bxrwzhbe', 'jjbd', 'gtcgppp', 'bowbut', 'wqypc', 'l', 'brhphla', 'lkpuay', 'qu']) == ['b6e', 'j2d', 'g5p', 'b4t', 'w3c', 'l', 'b5a', 'l4y', 'qu']
assert solution.wordsAbbreviation(['txev', 'n']) == ['t2v', 'n']
assert solution.wordsAbbreviation(['zi', 'ubzetbeqve', 'lrfw', 'iadwrchixl', 'g', 'zteyvx']) == ['zi', 'u8e', 'l2w', 'i8l', 'g', 'z4x']
assert solution.wordsAbbreviation(['pmnh', 'xj', 'hzxob', 'wffvqjtvw']) == ['p2h', 'xj', 'h3b', 'w7w']
assert solution.wordsAbbreviation(['xxkr', 'tscvs', 'tpstcoo', 'bqnhcyaj', 'fy', 'ayvuburup']) == ['x2r', 't3s', 't5o', 'b6j', 'fy', 'a7p']
assert solution.wordsAbbreviation(['tgvivfnt', 'coswvpci', 'caypozgvcr', 'mqi', 'jqccftjiw']) == ['t6t', 'c6i', 'c8r', 'mqi', 'j7w']
assert solution.wordsAbbreviation(['rzn', 'oz']) == ['rzn', 'oz']
assert solution.wordsAbbreviation(['ake', 'e', 'waxyzjye', 'y', 'jrhtjxcemm', 'exmrwlofq', 'fppn']) == ['ake', 'e', 'w6e', 'y', 'j8m', 'e7q', 'f2n']
assert solution.wordsAbbreviation(['rdsjma', 'ibmkeyffi', 'zwcbli']) == ['r4a', 'i7i', 'z4i']
assert solution.wordsAbbreviation(['xkdwjqs', 'xhwjuewix', 'a']) == ['x5s', 'x7x', 'a']
assert solution.wordsAbbreviation(['vec']) == ['vec']
assert solution.wordsAbbreviation(['ee', 'crrok', 'ntrxaac', 'en', 'qyczicmj', 'kbr', 'mutcqt', 'kfgypuzh', 'z']) == ['ee', 'c3k', 'n5c', 'en', 'q6j', 'kbr', 'm4t', 'k6h', 'z']
assert solution.wordsAbbreviation(['vkvwezvbm', 'tk', 'orwuwmm', 'rimo', 'n', 'hn', 'hznj', 'j', 'bxmbl']) == ['v7m', 'tk', 'o5m', 'r2o', 'n', 'hn', 'h2j', 'j', 'b3l']
assert solution.wordsAbbreviation(['kyfubgfav', 'yudbg', 'i']) == ['k7v', 'y3g', 'i']
assert solution.wordsAbbreviation(['fifzxbyya', 'dexmf', 'qyvvwua', 'ilex', 'aw', 'eeaxket', 'pdrwchmuw', 'fukvia', 'gowagjkzm']) == ['f7a', 'd3f', 'q5a', 'i2x', 'aw', 'e5t', 'p7w', 'f4a', 'g7m']

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
