from typing import List

class Solution:
    """
    Given an array of distinct strings words, return the minimal possible abbreviations for every word.
    The following are the rules for a string abbreviation:
    The initial abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.
    If more than one word shares the same abbreviation, then perform the following operation:
    Increase the prefix (characters in the first part) of each of their abbreviations by 1.
    For example, say you start with the words ["abcdef","abndef"] both initially abbreviated as "a4f". Then, a sequence of operations would be ["a4f","a4f"] -> ["ab3f","ab3f"] -> ["abc2f","abn2f"].
    This operation is repeated until every abbreviation is unique.
    At the end, if an abbreviation did not make a word shorter, then keep it as the original word.

    Example 1:
    Input: words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]
    Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
    Example 2:
    Input: words = ["aa","aaa"]
    Output: ["aa","aaa"]

    Constraints:
    1 <= words.length <= 400
    2 <= words[i].length <= 400
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
    """

    def generate_abbreviation(self, word: str, prefix_len: int) -> str:
        """
        Generates the abbreviation for a given word with a specified prefix length.

        Args:
            word: The input string to be abbreviated.
            prefix_len: The length of the prefix to be included in the abbreviation.

        Returns:
            The abbreviated string.
        """
        # If the abbreviation length (prefix + number + last char) would be >= original length,
        # return the original word.
        # Length of number part: len(str(len(word) - prefix_len - 1))
        # Abbreviation length: prefix_len + len(str(len(word) - prefix_len - 1)) + 1
        # This check is simplified below, but the core idea is to avoid longer abbreviations.
        if prefix_len >= len(word) - 2:
            return word

        # Generate the abbreviation string
        abbr_middle = str(len(word) - prefix_len - 1)
        return word[:prefix_len] + abbr_middle + word[-1]


    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        """
        Calculates the minimal unique abbreviations for a list of words.

        Args:
            words: A list of distinct strings.

        Returns:
            A list of strings representing the minimal unique abbreviations for each word.
        """
        n = len(words)
        # Initialize abbreviations with prefix length 1 (first char, count, last char)
        # Note: generate_abbreviation expects prefix_len, which is 1 initially.
        # The initial prefix *is* the first character.
        abbreviations = [self.generate_abbreviation(word, 1) for word in words]
        prefix_lens = [1] * n # Keep track of the current prefix length for each word

        # Loop until all abbreviations are unique
        for i in range(n):
            while True:
                # Find all indices that have the same abbreviation as the current word `i`
                duplicates = set()
                for j in range(i + 1, n):
                    if abbreviations[i] == abbreviations[j]:
                        duplicates.add(j) # Add index `j` to the set of duplicates

                # If no duplicates are found for abbreviations[i] among the subsequent words, break the inner loop
                if not duplicates:
                    break

                # If duplicates were found, add the current index `i` to the set as well
                duplicates.add(i)

                # Increase the prefix length for all words involved in the collision
                for k in duplicates:
                    prefix_lens[k] += 1
                    abbreviations[k] = self.generate_abbreviation(words[k], prefix_lens[k])


        # Final check: If an abbreviation is not shorter than the original word, revert to the original word.
        for i in range(n):
            if len(abbreviations[i]) >= len(words[i]):
                abbreviations[i] = words[i]

        return abbreviations

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
