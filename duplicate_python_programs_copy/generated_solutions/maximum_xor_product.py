# Problem 2939: Maximum Xor Product
# Difficulty: Medium
# Description:
# <p>Given three integers <code>a</code>, <code>b</code>, and <code>n</code>, return <em>the <strong>maximum value</strong> of</em> <code>(a XOR x) * (b XOR x)</code> <em>where</em> <code>0 &lt;= x &lt; 2<sup>n</sup></code>.</p>
# <p>Since the answer may be too large, return it <strong>modulo</strong> <code>10<sup>9 </sup>+ 7</code>.</p>
# <p><strong>Note</strong> that <code>XOR</code> is the bitwise XOR operation.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> a = 12, b = 5, n = 4
# <strong>Output:</strong> 98
# <strong>Explanation:</strong> For x = 2, (a XOR x) = 14 and (b XOR x) = 7. Hence, (a XOR x) * (b XOR x) = 98. 
# It can be shown that 98 is the maximum value of (a XOR x) * (b XOR x) for all 0 &lt;= x &lt; 2<sup>n</sup><span style="font-size: 10.8333px;">.</span>
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> a = 6, b = 7 , n = 5
# <strong>Output:</strong> 930
# <strong>Explanation:</strong> For x = 25, (a XOR x) = 31 and (b XOR x) = 30. Hence, (a XOR x) * (b XOR x) = 930.
# It can be shown that 930 is the maximum value of (a XOR x) * (b XOR x) for all 0 &lt;= x &lt; 2<sup>n</sup>.</pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre>
# <strong>Input:</strong> a = 1, b = 6, n = 3
# <strong>Output:</strong> 12
# <strong>Explanation:</strong> For x = 5, (a XOR x) = 4 and (b XOR x) = 3. Hence, (a XOR x) * (b XOR x) = 12.
# It can be shown that 12 is the maximum value of (a XOR x) * (b XOR x) for all 0 &lt;= x &lt; 2<sup>n</sup>.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>0 &lt;= a, b &lt; 2<sup>50</sup></code></li>
# 	<li><code>0 &lt;= n &lt;= 50</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        mod = 10**9 + 7
        ax, bx = (a >> n) << n, (b >> n) << n
        for i in range(n - 1, -1, -1):
            x = a >> i & 1
            y = b >> i & 1
            if x == y:
                ax |= 1 << i
                bx |= 1 << i
            elif ax > bx:
                bx |= 1 << i
            else:
                ax |= 1 << i
        return ax * bx % mod

# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.maximumXorProduct(1072297517651408, 437909297928259, 4) == 696951069
assert solution.maximumXorProduct(1033502817572754, 488258145285387, 42) == 844189533
assert solution.maximumXorProduct(518879363354668, 725525769136565, 20) == 181761524
assert solution.maximumXorProduct(654900607063220, 466335341060603, 28) == 643919678
assert solution.maximumXorProduct(826450770778027, 867136941188534, 12) == 415177565
assert solution.maximumXorProduct(700678274300664, 769548099450701, 33) == 938654257
assert solution.maximumXorProduct(397598115702457, 204672362163535, 26) == 987698790
assert solution.maximumXorProduct(1097841846801464, 942725371171660, 50) == 345884015
assert solution.maximumXorProduct(969452539351867, 332606312268392, 32) == 495917257
assert solution.maximumXorProduct(29422950828494, 731762355234832, 39) == 304789559
assert solution.maximumXorProduct(1101097809561480, 380213794675945, 5) == 6382931
assert solution.maximumXorProduct(667915746854870, 450007859840576, 3) == 460504849
assert solution.maximumXorProduct(787660584180687, 168444700260349, 35) == 756304458
assert solution.maximumXorProduct(312375492019315, 490354229181653, 41) == 78272329
assert solution.maximumXorProduct(391134531156899, 658855268414999, 16) == 370609176
assert solution.maximumXorProduct(743426035010468, 807133177488047, 14) == 960093736
assert solution.maximumXorProduct(560068222046417, 429285438627351, 22) == 419067783
assert solution.maximumXorProduct(763480868153226, 946676677483128, 35) == 975250074
assert solution.maximumXorProduct(420088758374810, 927989109200234, 41) == 778227856
assert solution.maximumXorProduct(95645909735962, 10338370925609, 17) == 887043891
assert solution.maximumXorProduct(796282827280100, 8874996766822, 27) == 900511890
assert solution.maximumXorProduct(170775523879794, 314871106704711, 44) == 818229408
assert solution.maximumXorProduct(627347861913805, 472629228650153, 7) == 999180965
assert solution.maximumXorProduct(829781725833832, 450703023473662, 14) == 21742337
assert solution.maximumXorProduct(788593490518101, 268237254433313, 10) == 714905339
assert solution.maximumXorProduct(531658128965829, 325066226516685, 13) == 652676106
assert solution.maximumXorProduct(100937327722561, 456658291463885, 23) == 983594444
assert solution.maximumXorProduct(331200320885478, 271844955051261, 31) == 910418372
assert solution.maximumXorProduct(843378067423714, 484310757596490, 25) == 506005389
assert solution.maximumXorProduct(203760229129029, 1124825083343402, 27) == 951680397
assert solution.maximumXorProduct(339834935828847, 321186460813546, 6) == 789221036
assert solution.maximumXorProduct(612352393335707, 244516879877840, 15) == 815274715
assert solution.maximumXorProduct(872543236915592, 179827392879336, 29) == 534406712
assert solution.maximumXorProduct(803095300890258, 742568869089440, 21) == 45894424
assert solution.maximumXorProduct(996374453396746, 404581895697689, 12) == 250225661
assert solution.maximumXorProduct(874748174756546, 85857691856644, 44) == 916656125
assert solution.maximumXorProduct(85116862200763, 578638427374268, 46) == 487235215
assert solution.maximumXorProduct(544485660360036, 800422342219480, 9) == 486196567
assert solution.maximumXorProduct(1108918416626529, 840723815837531, 32) == 268700939
assert solution.maximumXorProduct(219316146094518, 1058828050792091, 3) == 194199083
assert solution.maximumXorProduct(45610741644662, 233928383128931, 13) == 842237278
assert solution.maximumXorProduct(1044804860709206, 1029760728921526, 12) == 13904422
assert solution.maximumXorProduct(999764635623176, 847940243043950, 50) == 208965262
assert solution.maximumXorProduct(688255673330577, 366502380713411, 3) == 829464240
assert solution.maximumXorProduct(627398714169132, 269785264548658, 33) == 704657686
assert solution.maximumXorProduct(238752995224281, 1035716933823171, 12) == 905275916
assert solution.maximumXorProduct(1082347772288279, 274382888467673, 39) == 890086209
assert solution.maximumXorProduct(983761301631143, 743385330301828, 43) == 700141527
assert solution.maximumXorProduct(230098844144865, 990977388267374, 6) == 109852093
assert solution.maximumXorProduct(1115260610028227, 977449122586201, 34) == 113425365
assert solution.maximumXorProduct(1048838400405412, 186520597487547, 45) == 277644487
assert solution.maximumXorProduct(569112426615430, 1083637526547606, 44) == 117014975
assert solution.maximumXorProduct(547856503204782, 993461852275023, 11) == 392351443
assert solution.maximumXorProduct(7437566012331, 80623093990443, 15) == 786843234
assert solution.maximumXorProduct(750865566982240, 630017751646327, 2) == 475511493
assert solution.maximumXorProduct(478310508852007, 38515044567465, 22) == 938731931
assert solution.maximumXorProduct(937900527243321, 302777165626772, 35) == 564471231
assert solution.maximumXorProduct(425082875245149, 343666146435417, 42) == 437809769
assert solution.maximumXorProduct(337911447238655, 910177495456008, 8) == 881837588
assert solution.maximumXorProduct(774639190894842, 529058968678775, 27) == 546989426
assert solution.maximumXorProduct(722391364489478, 250980209963292, 19) == 145039622
assert solution.maximumXorProduct(127240250267758, 835363975617236, 50) == 714337983
assert solution.maximumXorProduct(1018182975829804, 278244705720631, 21) == 20126339
assert solution.maximumXorProduct(427249603162522, 369512855813026, 45) == 226795484
assert solution.maximumXorProduct(218573276037437, 1114114836184006, 17) == 159144030
assert solution.maximumXorProduct(658161236352517, 681675346707992, 8) == 293049165
assert solution.maximumXorProduct(468245781742769, 593867089900481, 45) == 160043908
assert solution.maximumXorProduct(277209483026234, 1045349542272787, 30) == 44777918
assert solution.maximumXorProduct(820404816926934, 497848987371104, 45) == 904807003
assert solution.maximumXorProduct(122662763981566, 504185108856459, 28) == 174906514
assert solution.maximumXorProduct(822109040580783, 936314864226149, 4) == 309879920
assert solution.maximumXorProduct(452262842766477, 399200537286430, 1) == 230164959
assert solution.maximumXorProduct(1024070885455763, 1047410006047987, 43) == 177118443
assert solution.maximumXorProduct(389141855749614, 851979168434115, 46) == 791027632
assert solution.maximumXorProduct(31712117393495, 994244727053476, 4) == 965744384
assert solution.maximumXorProduct(686769374638043, 848424785551404, 8) == 483958242
assert solution.maximumXorProduct(647629592894412, 1110900304191293, 10) == 607609690
assert solution.maximumXorProduct(681457005585267, 879586462464566, 10) == 600116073
assert solution.maximumXorProduct(197172691833528, 271836775067096, 4) == 776233285
assert solution.maximumXorProduct(756174133285343, 789671286633870, 34) == 265272775
assert solution.maximumXorProduct(348448535937691, 985920086216184, 9) == 596423755
assert solution.maximumXorProduct(661113285321727, 47695205597191, 50) == 400164403
assert solution.maximumXorProduct(18411385288982, 685688754172722, 40) == 806702368
assert solution.maximumXorProduct(573270951294456, 1113186861771050, 42) == 175270245
assert solution.maximumXorProduct(693138501105207, 946567840521116, 38) == 818209074
assert solution.maximumXorProduct(675196341945111, 785945052238984, 21) == 893550384
assert solution.maximumXorProduct(667575052463022, 459329314622523, 34) == 259101913
assert solution.maximumXorProduct(736895470122350, 523379128444538, 20) == 958923572
assert solution.maximumXorProduct(143264960187493, 209110344585824, 34) == 392601280
assert solution.maximumXorProduct(81840884774170, 20923923145432, 8) == 902869663
assert solution.maximumXorProduct(672973140251249, 835001226551257, 37) == 561052352
assert solution.maximumXorProduct(838380109629443, 1064363853907903, 35) == 569744154
assert solution.maximumXorProduct(914847818988869, 423313918049902, 10) == 389348345
assert solution.maximumXorProduct(507833715676562, 1074440098645452, 17) == 797787764
assert solution.maximumXorProduct(541210169472388, 384553158040798, 23) == 142059200
assert solution.maximumXorProduct(21183842377751, 1076233478546107, 22) == 834355212
assert solution.maximumXorProduct(702370413886316, 971150213477422, 37) == 261905846
assert solution.maximumXorProduct(79128961300669, 526805306649494, 17) == 89155330
assert solution.maximumXorProduct(98384883586577, 371406695654412, 30) == 405733264
assert solution.maximumXorProduct(158993952040548, 27876746854952, 23) == 279129968

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
