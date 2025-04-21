# Problem 2591: Distribute Money to Maximum Children
# Difficulty: Easy
# Description:
# <p>You are given an integer <code>money</code> denoting the amount of money (in dollars) that you have and another integer <code>children</code> denoting the number of children that you must distribute the money to.</p>
# <p>You have to distribute the money according to the following rules:</p>
# <ul>
# 	<li>All money must be distributed.</li>
# 	<li>Everyone must receive at least <code>1</code> dollar.</li>
# 	<li>Nobody receives <code>4</code> dollars.</li>
# </ul>
# <p>Return <em>the <strong>maximum</strong> number of children who may receive <strong>exactly</strong> </em><code>8</code> <em>dollars if you distribute the money according to the aforementioned rules</em>. If there is no way to distribute the money, return <code>-1</code>.</p>
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre>
# <strong>Input:</strong> money = 20, children = 3
# <strong>Output:</strong> 1
# <strong>Explanation:</strong> 
# The maximum number of children with 8 dollars will be 1. One of the ways to distribute the money is:
# - 8 dollars to the first child.
# - 9 dollars to the second child. 
# - 3 dollars to the third child.
# It can be proven that no distribution exists such that number of children getting 8 dollars is greater than 1.
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre>
# <strong>Input:</strong> money = 16, children = 2
# <strong>Output:</strong> 2
# <strong>Explanation:</strong> Each child can be given 8 dollars.
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
# <ul>
# 	<li><code>1 &lt;= money &lt;= 200</code></li>
# 	<li><code>2 &lt;= children &lt;= 30</code></li>
# </ul>

# --------------------------------------
# Test Case Generator Code:
import random


class Solution:
    def distMoney(self, money: int, children: int) -> int:
        # It is impossible to distribute money if we don't have at least 1 dollar per child.
        if money < children:
            return -1

        # Give every child 1 dollar. The remaining extra amount.
        extra = money - children

        # Let x be the number of children who receive exactly 8 dollars.
        # Since every child already got 1 dollar, these x children must get an extra 7 dollars each.
        # Thus, a candidate x is feasible only if extra >= 7*x.
        # Moreover, let T = extra - 7*x be the remaining extra dollars to distribute over the other (children - x) kids.
        # These children will end up with 1 + (their extra). We have the constraint that no child can end up with 4 dollars,
        # i.e. no child can get exactly 3 extra dollars.
        #
        # For groups of children where (children - x) >= 2, we can always partition T (≥ 0) among them
        # in such a way to avoid any one child receiving exactly 3 extra dollars.
        # The only delicate case is when there is exactly one remaining child (children - x == 1).
        # In that case the single child would have to receive all of T. If T equals 3 then that child's total becomes 4,
        # which is forbidden.
        #
        # Also, when x == children (i.e. everyone gets exactly 8 dollars) then the leftover T must be 0.

        # The maximum potential x (ignoring the leftover partition constraint) is bounded by:
        max_possible = min(children, extra // 7)

        # Try from the maximum candidate x downward until we find one that allows a valid partition of the remaining extra dollars.
        for x in range(max_possible, -1, -1):
            remaining_children = children - x  # children who are NOT getting exactly 8 dollars
            leftover = extra - 7 * x  # remaining extra dollars after giving x children an extra 7 dollars

            if remaining_children == 0:
                # In this case all children get exactly 8 dollars,
                # so the leftover extra dollars must be exactly 0.
                if leftover == 0:
                    return x
                else:
                    continue

            if remaining_children == 1:
                # With one child, that child must get all leftover dollars.
                # If leftover equals 3 then that child's total will be 1 + 3 = 4 dollars, which is forbidden.
                if leftover == 3:
                    continue
                else:
                    return x

            # For two or more remaining children, we can always partition leftover among them
            # while ensuring that none of them ends up receiving exactly 3 extra dollars.
            return x

        return -1


# --------------------------------------
# Test Cases:
solution = Solution()
assert solution.distMoney(33, 14) == 2
assert solution.distMoney(66, 27) == 5
assert solution.distMoney(137, 15) == 14
assert solution.distMoney(105, 23) == 11
assert solution.distMoney(28, 15) == 1
assert solution.distMoney(124, 25) == 14
assert solution.distMoney(33, 20) == 1
assert solution.distMoney(67, 30) == 5
assert solution.distMoney(185, 30) == 22
assert solution.distMoney(129, 2) == 1
assert solution.distMoney(127, 6) == 5
assert solution.distMoney(88, 18) == 10
assert solution.distMoney(161, 22) == 19
assert solution.distMoney(3, 8) == -1
assert solution.distMoney(4, 23) == -1
assert solution.distMoney(100, 23) == 11
assert solution.distMoney(104, 11) == 10
assert solution.distMoney(54, 9) == 6
assert solution.distMoney(162, 25) == 19
assert solution.distMoney(41, 21) == 2
assert solution.distMoney(140, 25) == 16
assert solution.distMoney(114, 16) == 14
assert solution.distMoney(193, 31) == 23
assert solution.distMoney(99, 4) == 3
assert solution.distMoney(47, 7) == 5
assert solution.distMoney(146, 15) == 14
assert solution.distMoney(180, 28) == 21
assert solution.distMoney(106, 22) == 12
assert solution.distMoney(48, 17) == 4
assert solution.distMoney(79, 8) == 7
assert solution.distMoney(38, 9) == 4
assert solution.distMoney(144, 27) == 16
assert solution.distMoney(71, 21) == 7
assert solution.distMoney(159, 27) == 18
assert solution.distMoney(81, 18) == 9
assert solution.distMoney(62, 11) == 7
assert solution.distMoney(144, 13) == 12
assert solution.distMoney(34, 21) == 1
assert solution.distMoney(38, 13) == 3
assert solution.distMoney(38, 20) == 2
assert solution.distMoney(97, 11) == 10
assert solution.distMoney(149, 31) == 16
assert solution.distMoney(130, 19) == 15
assert solution.distMoney(89, 13) == 10
assert solution.distMoney(125, 20) == 15
assert solution.distMoney(123, 31) == 13
assert solution.distMoney(63, 28) == 5
assert solution.distMoney(148, 8) == 7
assert solution.distMoney(183, 26) == 22
assert solution.distMoney(128, 25) == 14
assert solution.distMoney(32, 21) == 1
assert solution.distMoney(175, 18) == 17
assert solution.distMoney(54, 22) == 4
assert solution.distMoney(83, 17) == 9
assert solution.distMoney(87, 26) == 8
assert solution.distMoney(196, 26) == 24
assert solution.distMoney(71, 19) == 7
assert solution.distMoney(53, 4) == 3
assert solution.distMoney(138, 8) == 7
assert solution.distMoney(154, 22) == 18
assert solution.distMoney(82, 27) == 7
assert solution.distMoney(153, 29) == 17
assert solution.distMoney(42, 28) == 2
assert solution.distMoney(95, 11) == 10
assert solution.distMoney(5, 13) == -1
assert solution.distMoney(73, 28) == 6
assert solution.distMoney(50, 30) == 2
assert solution.distMoney(93, 16) == 11
assert solution.distMoney(81, 25) == 8
assert solution.distMoney(144, 10) == 9
assert solution.distMoney(38, 19) == 2
assert solution.distMoney(36, 22) == 2
assert solution.distMoney(83, 30) == 7
assert solution.distMoney(140, 31) == 15
assert solution.distMoney(53, 28) == 3
assert solution.distMoney(58, 19) == 5
assert solution.distMoney(193, 5) == 4
assert solution.distMoney(53, 8) == 6
assert solution.distMoney(6, 18) == -1
assert solution.distMoney(129, 5) == 4
assert solution.distMoney(91, 24) == 9
assert solution.distMoney(94, 3) == 2
assert solution.distMoney(180, 25) == 22
assert solution.distMoney(106, 7) == 6
assert solution.distMoney(93, 26) == 9
assert solution.distMoney(45, 7) == 5
assert solution.distMoney(23, 30) == -1
assert solution.distMoney(69, 9) == 8
assert solution.distMoney(108, 2) == 1
assert solution.distMoney(31, 9) == 3
assert solution.distMoney(18, 22) == -1
assert solution.distMoney(171, 19) == 18
assert solution.distMoney(95, 10) == 9
assert solution.distMoney(175, 31) == 20
assert solution.distMoney(68, 20) == 6
assert solution.distMoney(77, 30) == 6
assert solution.distMoney(168, 21) == 21
assert solution.distMoney(66, 22) == 6
assert solution.distMoney(26, 4) == 3
assert solution.distMoney(9, 21) == -1

if __name__ == '__main__':
    # To run the generated test cases or custom testing code, modify below.
    # For example:
    # num_tests = 100
    # test_generated_test_cases(num_tests)
    pass
